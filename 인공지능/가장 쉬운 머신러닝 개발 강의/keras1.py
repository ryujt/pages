import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, BatchNormalization
from keras.optimizers import Adam

def generate_false_data(num_samples):
    false_data = []
    target_pattern = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])

    while len(false_data) < num_samples:
        sample = np.random.randint(0, 2, (3, 3))
        if not np.array_equal(sample, target_pattern):
            false_data.append(sample)

    return np.array(false_data)

# 모델 구조 변경 및 정규화 기법 적용
model = Sequential([
    Flatten(input_shape=(3, 3)),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# 옵티마이저 변경 및 학습률 조정
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# True 데이터
X_true = np.array([[[0, 1, 0], [0, 1, 0], [0, 1, 0]]])
y_true = np.array([1])

num_false_samples = 1000
X_false = generate_false_data(num_false_samples)
y_false = np.zeros((num_false_samples,))

# 훈련 데이터와 레이블을 합칩니다.
X_train = np.concatenate((X_true, X_false), axis=0)
y_train = np.concatenate((y_true, y_false), axis=0)

# 학습 파라미터 조정 (에포크 수 및 배치 크기 조정)
model.fit(X_train, y_train, epochs=200, batch_size=32)

# 첫 번째 테스트 케이스 (True가 예상됨)
X_test1 = np.array([[[0, 1, 0], [0, 1, 0], [0, 1, 0]]])
predictions1 = model.predict(X_test1)

# 예측 결과를 출력합니다.
print("---------------------------------------")
print("Test Case 1 Predictions:", predictions1 > 0.5)

# 두 번째 테스트 케이스 (False가 예상됨)
X_test2 = np.array([[[0, 1, 1], [0, 1, 0], [0, 1, 0]]])
predictions2 = model.predict(X_test2)

# 예측 결과를 출력합니다.
print("---------------------------------------")
print("Test Case 2 Predictions:", predictions2 > 0.5)
