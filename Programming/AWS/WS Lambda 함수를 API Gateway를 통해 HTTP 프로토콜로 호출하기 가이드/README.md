# AWS Lambda 함수를 API Gateway를 통해 HTTP 프로토콜로 호출하기 가이드

다음은 AWS Lambda 함수를 API Gateway를 통해 HTTP 프로토콜로 호출하는 전체 과정을 정리한 가이드 문서입니다. 이 문서는 실제 구현 과정에서 겪은 시행착오와 최종적인 성공 사례를 토대로 정리되었습니다.

---

## 목차

1. 개요  
2. 사전 준비 사항  
3. Lambda 함수 작성 시 주의사항  
4. API Gateway 설정 단계  
5. 권한 설정  
6. 요청/응답 형식 점검  
7. 디버깅 방법  
8. 최종 테스트  
9. 추가 팁

---

## 1. 개요

AWS Lambda를 AWS API Gateway를 통해 호출하면, 외부에서 HTTP(REST) 프로토콜을 통해 Lambda 함수를 직접 호출할 수 있습니다. 이를 통해 서버리스 아키텍처를 구현할 수 있으며, API Gateway를 엔드포인트로 사용하여 인증, 로깅, 모니터링, 트래픽 관리 등을 쉽게 수행할 수 있습니다.

---

## 2. 사전 준비 사항

- **AWS 계정 및 권한**: Lambda, API Gateway, CloudWatch 로그에 접근할 수 있어야 합니다.  
- **AWS CLI 설치 및 설정**: 터미널에서 `aws configure` 명령을 통해 자격 증명(Access Key, Secret Key)과 리전을 설정합니다.  
- **Node.js Lambda 함수**: 예제 코드에서는 Node.js로 작성된 Lambda 함수를 가정합니다.

---

## 3. Lambda 함수 작성 시 주의사항

Lambda 함수는 API Gateway를 통해 호출될 때, **`event`** 객체의 구조가 Lambda URL 또는 다른 호출 방식과 다를 수 있습니다.

- **`event.body` 타입 차이**:  
  API Gateway를 사용할 때 `event.body`는 일반적으로 **문자열(JSON 문자열)** 형태로 전달됩니다. 반면 Lambda Function URL 호출 시 `event.body`가 이미 파싱된 객체로 전달될 수도 있습니다.
  
- **JSON 파싱 로직 추가**:  
  `event.body`가 문자열인지, 객체인지 구분한 후 적절히 파싱하는 방어적 코드가 필요합니다.

예시 코드(최종 성공 사례):

```javascript
exports.handler = async (event) => {
    try {
        let body;
        if (event.body) {
            // event.body가 문자열인 경우
            if (typeof event.body === 'string') {
                body = JSON.parse(event.body);
            } else {
                // 이미 파싱된 상태일 경우
                body = event.body;
            }
        }

        const { room_id } = body || {};
        
        return {
            statusCode: 200,
            body: JSON.stringify({
                message: 'Public IP retrieved and room updated successfully',
                room_id: room_id,
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ message: 'Internal Server Error', error: error.message }),
            headers: {
                'Content-Type': 'application/json'
            }
        };
    }
};
```

---

## 4. API Gateway 설정 단계

1. **HTTP API 생성**:  
   ```bash
   aws apigatewayv2 create-api \
       --name "my-http-api" \
       --protocol-type "HTTP" \
       --target "arn:aws:lambda:ap-northeast-2:ACCOUNT_ID:function:FUNCTION_NAME"
   ```
   이 명령으로 HTTP 프로토콜을 사용하는 API를 생성하고, Lambda 함수를 기본 타겟으로 설정합니다.

2. **Integration 생성**(AWS_PROXY):  
   Lambda를 호출하기 위한 Integration 생성:
   ```bash
   aws apigatewayv2 create-integration \
       --api-id "YOUR_API_ID" \
       --integration-type "AWS_PROXY" \
       --integration-uri "arn:aws:lambda:ap-northeast-2:ACCOUNT_ID:function:FUNCTION_NAME" \
       --payload-format-version "2.0"
   ```

3. **라우트(Route) 생성**:  
   예: POST 메서드로 `/get-room-info` 라우트 생성
   ```bash
   aws apigatewayv2 create-route \
       --api-id "YOUR_API_ID" \
       --route-key "POST /get-room-info" \
       --target "integrations/YOUR_INTEGRATION_ID"
   ```

4. **스테이지(Stage) 생성 및 배포**:
   ```bash
   aws apigatewayv2 create-stage \
       --api-id "YOUR_API_ID" \
       --stage-name "prod" \
       --auto-deploy
   ```

   `--auto-deploy`를 통해 이후 변경 사항이 자동으로 배포됩니다.  
   스테이지가 존재하지 않을 경우 `create-stage`로 먼저 생성해야 하며, 이후 `create-deployment` 명령을 통해 명시적으로 배포할 수도 있습니다.

---

## 5. 권한 설정

API Gateway가 Lambda를 호출할 수 있도록 Lambda에 Invoke 권한 부여:

```bash
aws lambda add-permission \
    --function-name "FUNCTION_NAME" \
    --principal "apigateway.amazonaws.com" \
    --statement-id "apigateway-invoke-permission" \
    --action "lambda:InvokeFunction" \
    --source-arn "arn:aws:execute-api:ap-northeast-2:ACCOUNT_ID:YOUR_API_ID/*/POST/get-room-info"
```

이로써 API Gateway에서 POST /get-room-info 라우트를 호출할 때 Lambda를 실행할 수 있습니다.

---

## 6. 요청/응답 형식 점검

- 요청 시 `Content-Type: application/json` 헤더를 반드시 추가합니다.  
- Lambda 함수 내에서 요청 payload를 파싱하고, 적절한 JSON 응답을 반환합니다.
- 응답 헤더에 `Content-Type: application/json`를 명시하면 클라이언트가 응답을 JSON으로 해석할 수 있습니다.

---

## 7. 디버깅 방법

문제가 발생했을 경우:

1. **CloudWatch Logs 확인**:  
   ```bash
   aws logs describe-log-streams \
       --log-group-name "/aws/lambda/FUNCTION_NAME"
   ```
   가장 최근 로그 스트림을 확인하고, 해당 로그 이벤트를 출력하여 에러 메시지를 확인합니다:
   ```bash
   aws logs get-log-events \
       --log-group-name "/aws/lambda/FUNCTION_NAME" \
       --log-stream-name "LOG_STREAM_NAME"
   ```

2. **Lambda 단독 테스트**:  
   ```bash
   aws lambda invoke \
       --function-name "FUNCTION_NAME" \
       --payload '{"room_id":"1943882142918418"}' \
       response.json
   ```
   `response.json`에 Lambda 결과를 저장하여 로직 오류를 확인합니다.

3. **API Gateway URL로 테스트**:  
   cURL 명령으로 API Gateway 호출:
   ```bash
   curl -X POST "https://YOUR_API_ID.execute-api.ap-northeast-2.amazonaws.com/prod/get-room-info" \
       -H "Content-Type: application/json" \
       -d '{"room_id": "1943882142918418"}'
   ```

4. Lambda Function URL과 비교하여 event 구조 차이를 확인하고, 코드에서 문자열/객체 처리를 유연하게 합니다.

---

## 8. 최종 테스트

- Lambda Function URL 호출:  
  ```bash
  curl -X POST "https://wqibycenhdc6om64tm2pea35w40melte.lambda-url.ap-northeast-2.on.aws/" \
      -H "Content-Type: application/json" \
      -d '{"room_id": "1943882142918418"}'
  ```

- API Gateway 호출:  
  ```bash
  curl -X POST "https://YOUR_API_ID.execute-api.ap-northeast-2.amazonaws.com/prod/get-room-info" \
      -H "Content-Type: application/json" \
      -d '{"room_id": "1943882142918418"}'
  ```

위 두 결과가 모두 기대한 JSON 응답을 반환한다면 설정이 완료된 것입니다.

---

## 9. 추가 팁

- **Lambda Proxy Integration 사용**:  
  Lambda Proxy Integration을 사용하면 API Gateway에서 받은 요청을 Lambda로 거의 그대로 전달하고, Lambda 응답을 API Gateway에서 변형 없이 그대로 클라이언트에 반환합니다. 이 방식을 사용하면 event 구조를 명확하게 이해하고 처리할 수 있습니다.
  
- **CORS 설정**:  
  브라우저 환경에서 호출 시 CORS 설정이 필요할 수 있습니다. API Gateway의 CORS 설정을 통해 특정 도메인에서의 호출을 허용할 수 있습니다.

---

## 결론

이 가이드는 Lambda 함수를 API Gateway를 통해 HTTP 프로토콜로 호출하기까지의 과정을 상세히 설명하고, event.body 처리 방식 차이로 인한 문제 해결방법을 제시했습니다. 이 단계를 통해 서버리스 아키텍처를 구현하는데 필요한 기본적이고 핵심적인 설정을 익힐 수 있습니다.