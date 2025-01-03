# 함수형 프로그래밍을 OOP 코드베이스에 적용하기

## 키워드
* 함수형 프로그래밍
* 객체 지향 프로그래밍(OOP)
* 불변성(Immutability)
* 순수 함수(Pure functions)
* 부작용(Side effects)
* 클래스(Class)
* 캡슐화(Encapsulation)

## 핵심 내용
* 함수형 프로그래밍은 상태 의존성을 최소화하고, 불변성, 순수 함수, 부작용을 피하는 것에 중점을 둔다.
* 객체 지향 프로그래밍(OOP)은 상태를 캡슐화하여 관리하며, 클래스를 통해 상태와 그 상태를 조작하는 행위를 그룹화한다.
* 불변성은 프로그램 내의 변수를 변경하지 않는 관행을 의미한다.
* 순수 함수는 동일한 입력에 대해 항상 동일한 출력을 반환하며, 부작용이 없고, 불변성을 존중하는 함수다.
* 부작용은 외부 세계와의 상호작용을 포함하는 계산을 의미하며, 가능한 한 분리하여 관리해야 한다.
* OOP 코드베이스 내에서도 함수형 개념을 적용하여 코드를 단순화하고 예측 가능하게 만들 수 있다.

## 줄거리 요약
이 글은 함수형 프로그래밍의 열렬한 지지자가 되어가는 과정과, 객체 지향 프로그래밍(OOP) 코드베이스 내에서 함수형 프로그래밍 개념을 어떻게 적용할 수 있는지에 대한 경험을 공유한다. 함수형 프로그래밍은 상태 의존성을 최소화하며 불변성, 순수 함수, 부작용 최소화에 중점을 둔다. 반면, OOP는 상태 관리를 위해 캡슐화를 강조하지만, 작성자는 OOP 내에서도 함수형 패턴을 사용하여 코드를 더 깨끗하고 분리된 형태로 만들 수 있음을 주장한다. 이를 통해 어떤 패러다임이 더 낫다는 논쟁을 넘어 좋은 아이디어를 조합하고 점점 더 나은 코드를 생산하기를 희망한다.

## 함수형 프로그래밍의 시작

함수형 프로그래밍 패러다임은 1958년 Lisp 언어의 등장과 함께 시작되었습니다. 그 기원은 Alonzo Church의 람다 계산법으로 거슬러 올라갈 수 있습니다. 함수형 프로그래밍의 핵심 원칙은 코드베이스 내에서 상태에 대한 의존성을 최소화하는 데 집중합니다.

객체 지향 프로그래밍(OOP)이 상태를 허용하되 캡슐화를 강조하는 것과 대조적으로, 함수형 프로그래머들은 상태가 없는 컴포넌트를 작성하는 것을 우선시합니다. 이러한 접근 방식은 외부 상태 변수에 독립적인 코드의 생성을 촉진합니다.

또한, 상태가 도입될 때에도, 불변성, 함수의 순수성, 부작용 피하기 등을 생각하면서 작성하는 것이 중요합니다. 이러한 모든 개념들은 기사가 진행됨에 따라 더 자세히 다룰 예정입니다.

OOP로 들어가며, 이 패러다임은 무엇인가에 대한 고찰에서부터 시작해, 클래스가 무엇이며 우리가 이를 어떻게 다르게 생각할 수 있는지, 변형할 것인지 말 것인지에 대한 불변성의 개념, 침대 밑의 괴물이라 할 수 있는 부작용이 무엇인지, 모든 것을 격리하는 순수 함수의 개념 등을 차례로 살펴보게 됩니다.

함수형 프로그래밍은 이러한 개념들을 기반으로 하여, 코드를 더 단순하게 만들고 결과를 더 쉽게 예측할 수 있도록 도와주며, 단위 테스트를 작성하기가 매우 쉽다는 장점이 있습니다. 이러한 방식으로 함수형 프로그래밍의 개념을 이미 작성된 OOP 코드 내에서 사용하는 방안을 제안하고자 합니다. 이를 통해 어떤 패러다임이 더 나은지에 대한 논쟁을 멈추고, 좋은 아이디어를 조합하여 매번 더 나은 코드를 생산하기 시작할 수 있기를 바랍니다.

## 객체 지향 프로그래밍(OOP) 소개

객체 지향 프로그래밍(Object-Oriented Programming, OOP)은 1967년에 등장한 프로그래밍 패러다임으로, Simula, Smalltalk, Java와 같은 언어들이 이 패러다임의 대표적인 예시입니다. 객체 지향 프로그래밍의 핵심적인 사고 과정은 "전역적" 상태의 양을 줄이고, 해당 상태와 그것을 수정하는 행위를 공통의 "엔티티"나 "객체"로 묶는 캡슐화 관행을 강화함으로써 이루어집니다.

실제로, "객체 지향 프로그래밍"이라는 이름은 수년에 걸쳐 널리 논의되어 왔습니다. OOP의 창시자 중 한 명인 Alan Key는 이 패러다임의 메시징 측면에 더 집중하기를 원했습니다. 이는 캡슐화를 강조하고 객체 간의 상태와 행동을 통신할 수 있게 함을 의미합니다. 아마도 다른 우주에서는 "메시징 지향 프로그래밍"이라는 이름을 가질 수도 있었겠지만, 수년에 걸쳐 OOP라는 이름이 지속되어 왔습니다.

클래스란 실제 세계의 엔티티를 기술하는 청사진으로, 그 특성과 행동을 설명합니다. 하지만, 단순히 이러한 설명 대신, 클래스는 상태와 그 상태에 작동하는 행동들을 캡슐화하는 방법입니다라는 새로운 관점을 제안합니다. 이는 클래스를 실세계 엔티티로 생각하기보다는, 유사한 맥락의 상태를 함께 그룹화하고 그 상태를 조작하는 함수들을 노출하는 또 다른 방법으로 생각하도록 제안합니다.

이러한 추상화를 통해, 우리는 모듈과 같은 다른 구성을 가진 언어들의 코드를 능숙하게 읽을 수 있게 됩니다. 예를 들어, TypeScript에서 작성된 OOP 코드와 Elixir의 "모듈"을 사용하는 코드 사이에는 완전히 동등한 관계가 존재합니다. 이러한 인식을 통해, 우리는 함수형 개념들을 더 깊이 살펴보고 이러한 패러다임들의 융합에 대해 더 논의할 준비가 되었습니다.

## 함수형 개념과 OOP의 결합

함수형 프로그래밍과 객체 지향 프로그래밍(OOP)은 종종 상반되는 패러다임으로 여겨집니다. 그러나 이 둘을 결합함으로써, 우리는 각각의 장점을 취하고 단점을 보완하는 코드를 작성할 수 있습니다. 이 섹션에서는 함수형 개념과 OOP를 어떻게 결합할 수 있는지에 대하여 논의합니다.

함수형 프로그래밍은 순수 함수, 불변성, 부작용의 최소화와 같은 원칙에 초점을 맞추며, 이를 통해 예측 가능하고, 테스트하기 쉬운 코드를 작성할 수 있습니다. 반면, 객체 지향 프로그래밍은 데이터와 그 데이터를 조작하는 메서드를 하나의 단위로 묶는 캡슐화에 중점을 둡니다. 이 두 패러다임을 결합함으로써, 상태 관리의 이점과 함수형 프로그래밍의 명확성 및 간결성을 모두 활용할 수 있습니다.

함수형 프로그래밍과 OOP의 결합은 강력한 소프트웨어 설계 방식을 제공합니다. 순수 함수, 불변성, 고차 함수 등의 함수형 개념을 OOP의 구조와 결합함으로써, 유지 보수가 쉽고, 테스트하기 용이하며, 예측 가능한 코드를 작성할 수 있습니다. 이러한 접근 방식을 통해, 우리는 두 패러다임의 장점을 모두 활용할 수 있으며, 더 나은 소프트웨어를 만들기 위한 새로운 길을 탐색할 수 있습니다.

### 순수 함수와 메서드
클래스 내에서 순수 함수의 개념을 적용하여, 데이터를 변형하는 메서드를 작성할 때 입력에만 의존하고 외부 상태에 영향을 받지 않도록 할 수 있습니다. 이는 메서드의 예측 가능성을 높이고, 단위 테스트를 보다 쉽게 작성할 수 있게 합니다.

### 불변성의 적용
객체의 상태를 불변으로 유지하려는 노력은 OOP에서도 중요합니다. 객체의 상태가 생성 시점에만 설정되고, 이후에는 변경되지 않도록 함으로써, 부작용을 줄이고, 코드의 안정성을 높일 수 있습니다. 예를 들어, 객체의 필드를 final이나 readonly로 선언하고, 상태 변경이 필요한 경우 새로운 객체를 반환하는 방식으로 설계할 수 있습니다.

### 고차 함수와 전략 패턴의 결합
OOP의 전략 패턴은 런타임에 알고리즘을 선택할 수 있도록 해주며, 함수형 프로그래밍의 고차 함수는 함수를 인자로 받아 로직을 동적으로 변경할 수 있습니다. 이 두 개념을 결합함으로써, 유연하면서도 강력한 코드를 작성할 수 있습니다. 예를 들어, 정렬 알고리즘을 선택하거나, 데이터 처리 방식을 변경하는 등의 작업을 더 깔끔하게 수행할 수 있습니다.

### 부작용의 격리
함수형 프로그래밍은 부작용을 가능한 한 격리하고 순수 함수로 로직을 구성하려 합니다. OOP에서도 이 원칙을 적용하여, 부작용을 일으키는 코드를 명확히 구분하고, 나머지 시스템과 격리할 수 있습니다. 이를 통해 시스템의 안정성을 높이고, 테스트를 용이하게 만들 수 있습니다.

## 함수형 패턴을 전적으로 활용하지 않고 사용하기

함수형 프로그래밍을 전적으로 채택하지 않으면서도, 그 내에서 유용한 패턴을 객체 지향 프로그래밍(OOP) 코드에 적용하는 방법은 많은 개발자들이 관심을 가지는 주제입니다. 함수형 패턴을 완전히 활용하지 않는다는 것은 Haskell이나 Scala 같은 순수 함수형 언어의 모든 기능과 원칙을 엄격하게 따르지 않고, 대신 함수형 프로그래밍의 일부 개념을 OOP 코드에 통합하여 코드의 가독성, 유지 보수성, 테스트 용이성을 향상시키는 것을 의미합니다.

### 순수 함수의 적용

순수 함수는 주어진 입력에 대해서만 결과를 반환하며, 외부 상태를 변경하지 않고, 부작용(side effects)을 일으키지 않는 함수입니다. OOP 코드 내에서 순수 함수를 사용하면, 함수의 결과를 예측하기 쉽고, 단위 테스트를 작성하기가 더 용이해집니다. 예를 들어, 클래스의 메서드를 순수 함수로 구현하여, 외부 상태에 의존하지 않고 입력에만 의존하도록 설계할 수 있습니다.

### 불변성의 활용

불변 객체는 생성 후 그 상태가 변하지 않는 객체를 말합니다. OOP에서는 불변성을 적용하여 객체의 상태를 안정적으로 유지할 수 있습니다. 예를 들어, 객체의 필드를 final이나 const로 선언하여 불변성을 강제하고, 객체의 상태를 변경해야 할 때는 새로운 객체를 생성하여 반환하는 방식을 사용할 수 있습니다. 이렇게 하면, 부작용을 줄이고 코드의 예측 가능성을 높일 수 있습니다.

### 고차 함수의 적용

고차 함수는 다른 함수를 인자로 받거나, 함수를 결과로 반환하는 함수입니다. OOP에서는 전략 패턴과 같은 디자인 패턴을 고차 함수와 결합하여 사용할 수 있습니다. 이를 통해, 코드의 유연성을 높이고, 런타임에 동적으로 행동을 변경할 수 있는 기능을 구현할 수 있습니다.

### 부작용의 격리

함수형 프로그래밍에서는 부작용을 가진 코드를 순수 함수로부터 격리하는 것을 중요하게 여깁니다. OOP 코드 내에서도, 부작용을 일으키는 코드를 명확히 구분하고, 가능한 한 격리함으로써, 코드의 테스트와 유지 보수를 용이하게 할 수 있습니다. 예를 들어, 데이터베이스 접근이나 네트워크 요청과 같은 부작용을 일으키는 코드를 별도의 클래스나 메서드로 분리하여 관리할 수 있습니다.

이러한 방법을 통해, 함수형 프로그래밍의 원칙과 패턴을 OOP 코드에 접목시키면서도, 함수형 프로그래밍을 전적으로 채택하지 않는 개발자들도 코드의 품질을 향상시킬 수 있습니다. 이는 두 패러다임의 장점을 조화롭게 결합하여, 더욱 견고하고 유지 보수하기 쉬운 소프트웨어를 개발하는 데 도움이 됩니다.

## 결론

이 글은 함수형 프로그래밍에 대한 지식을 널리 퍼뜨리려는 시도입니다. 저는 함수형 프로그래밍 전문가가 아니며, 객체 지향 프로그래밍(OOP)을 알고 있으면서 함수형 프로그래밍에 관심이 있는 초보자를 대상으로 합니다. 이 글이 유용하기를 바라며, 필요한 도움을 드리겠습니다. 힘내세요 🍒

이 글을 통해, 함수형 프로그래밍의 원칙과 패턴을 OOP 코드에 통합하는 방법에 대해 논의하였습니다. 순수 함수, 불변성, 부작용의 격리와 같은 함수형 프로그래밍의 핵심 개념을 적용함으로써, 코드를 더 깔끔하고, 결합도가 낮게 만들 수 있습니다. Haskell이나 Scala 같은 순수 함수형 언어의 모든 기능과 원칙을 엄격하게 따르지 않아도 되며, 단순히 Ruby on Rails와 같은 기존의 OOP 언어와 프레임워크를 사용하면서도, 간단하고 효과적인 함수형 개념을 적용할 수 있습니다.

함수형 프로그래밍과 OOP의 결합은 강력한 소프트웨어 설계 방식을 제공합니다. 순수 함수, 불변성, 고차 함수 등의 함수형 개념을 OOP의 구조와 결합함으로써, 유지 보수가 쉽고, 테스트하기 용이하며, 예측 가능한 코드를 작성할 수 있습니다. 이러한 접근 방식을 통해, 우리는 두 패러다임의 장점을 모두 활용할 수 있으며, 더 나은 소프트웨어를 만들기 위한 새로운 길을 탐색할 수 있습니다.

이 시리즈의 이후 글들을 통해, 어떤 언어와 프레임워크를 선택하든, 코드베이스를 조합성과 단순성으로 개선하는 데 도움이 되기를 바랍니다. 함수형 프로그래밍의 원칙을 적용하여 좋은 아이디어를 조합하고, 매번 더 나은 코드를 생산하기 시작할 수 있기를 바랍니다.