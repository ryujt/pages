# SOLID 원칙

[출처](https://dev.to/lukeskw/solid-principles-theyre-rock-solid-for-good-reason-31hn)

## SOLID란 무엇인가?

객체 지향 프로그래밍에서 SOLID는 소프트웨어의 이해, 개발, 유지 보수를 향상시키기 위해 고안된 다섯 가지 디자인 원칙을 나타내는 약어입니다. 이 원칙들을 적용함으로써 버그 감소, 코드 품질 향상, 더 조직적인 코드 생산, 결합도 감소, 리팩토링 개선, 코드 재사용 촉진과 같은 여러 이점을 경험할 수 있습니다.

### 1. S - 단일 책임 원칙(Single Responsibility Principle, SRP)
하나의 클래스는 하나, 그리고 오직 하나의 변경 이유만을 가져야 합니다. 이는 클래스가 여러 기능과 책임을 가지는 것을 방지하며, 코드의 유지보수를 용이하게 합니다.

### 2. O - 개방-폐쇄 원칙(Open-Closed Principle, OCP)
객체나 엔티티는 확장에는 열려 있어야 하지만, 수정에는 닫혀 있어야 합니다. 새로운 기능을 추가할 때는 기존 코드를 수정하는 대신 확장할 수 있어야 합니다.

### 3. L - 리스코프 치환 원칙(Liskov Substitution Principle, LSP)
파생 클래스는 그것의 기반 클래스로 대체될 수 있어야 합니다. 이 원칙은 파생 클래스가 기반 클래스의 행동을 정확히 모방해야 한다는 것을 의미합니다.

### 4. I - 인터페이스 분리 원칙(Interface Segregation Principle, ISP)
클래스는 사용하지 않는 인터페이스나 메소드를 구현하도록 강요되어서는 안 됩니다. 구체적인 인터페이스를 만드는 것이 크고 일반적인 하나를 만드는 것보다 낫습니다.

### 5. D - 의존성 역전 원칙(Dependency Inversion Principle, DIP)
추상화에 의존하고 구현체에 의존하지 않아야 합니다. 고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화에 의존해야 합니다.

이 원칙들을 채택함으로써 개발자들은 변화에 더욱 탄력적인 시스템을 만들 수 있으며, 유지보수를 용이하게 하고 시간이 지남에 따라 코드 품질을 개선할 수 있습니다.

### S - 단일 책임 원칙(Single Responsibility Principle, SRP)

단일 책임 원칙(SRP)은 객체 지향 디자인 원칙 중 하나로, 하나의 클래스는 하나의 기능만을 가지며, 오직 하나의 변경 이유만을 가져야 한다는 원칙입니다. 이 원칙은 클래스가 여러 기능을 가지는 것을 방지하며, 이를 통해 코드의 유지보수를 용이하게 합니다. SRP를 적용함으로써, 시스템의 복잡성을 줄이고, 코드의 가독성을 향상시킬 수 있습니다.

#### SRP의 중요성

- **유지보수성**: 단일 책임 원칙을 준수하는 클래스는 수정이 필요할 때 해당 기능과 직접적으로 관련된 부분만 수정하면 되므로, 유지보수가 훨씬 간단해집니다.
- **확장성**: 새로운 기능을 추가할 때 기존의 코드를 변경하지 않고도, 새로운 클래스를 추가함으로써 기능을 확장할 수 있습니다.
- **재사용성**: 하나의 클래스가 하나의 기능만을 담당하므로, 다른 시스템에서도 해당 클래스를 재사용하기 쉽습니다.
- **테스트 용이성**: 단일 책임을 가진 클래스는 테스트가 용이합니다. 하나의 기능만을 테스트하면 되므로, 테스트 케이스를 작성하기 쉽고, 테스트 과정에서 발생할 수 있는 오류의 범위를 줄일 수 있습니다.

#### SRP 위반 예시

```java
class ProfileManager {
  authenticateUser(String username, String password) {
    // 인증 로직
  }

  showUserProfile(String username) {
    // 사용자 프로필 보여주는 로직
  }

  updateUserProfile(String username) {
    // 사용자 프로필 업데이트 로직
  }

  setUserPermissions(String username) {
    // 사용자 권한 설정 로직
  }
}
```

위의 `ProfileManager` 클래스는 인증, 사용자 프로필 보기, 프로필 업데이트, 권한 설정 등 여러 기능을 가지고 있습니다. 이는 SRP를 위반하는 것으로, 각 기능을 별도의 클래스로 분리하는 것이 바람직합니다.

#### SRP 적용 예시

```java
class AuthenticationManager {
  authenticateUser(String username, String password) {
    // 인증 로직
  }
}

class UserProfileManager {
  showUserProfile(String username) {
    // 사용자 프로필 보여주는 로직
  }

  updateUserProfile(String username) {
    // 사용자 프로필 업데이트 로직
  }
}

class PermissionManager {
  setUserPermissions(String username) {
    // 사용자 권한 설정 로직
  }
}
```

위와 같이 각 기능을 별도의 클래스로 분리함으로써, 각 클래스는 단일 책임을 가지게 되며, 이는 코드의 유지보수성, 확장성, 재사용성, 테스트 용이성을 향상시킵니다.

### O - 개방-폐쇄 원칙(Open-Closed Principle, OCP)

개방-폐쇄 원칙(Open-Closed Principle, OCP)은 소프트웨어 엔지니어링에서 매우 중요한 원칙 중 하나입니다. 이 원칙은 "소프트웨어 개체(클래스, 모듈, 함수 등)는 확장에 대해서는 열려 있어야 하지만, 수정에 대해서는 닫혀 있어야 한다"는 아이디어에 기반을 두고 있습니다. 즉, 기존의 코드를 변경하지 않으면서도 시스템의 기능을 확장할 수 있어야 합니다.

#### OCP의 중요성

- **유연성**: 새로운 기능이나 요구사항이 생겼을 때, 기존 코드를 수정하지 않고도 확장할 수 있어야 합니다. 이는 시스템의 유연성을 향상시킵니다.
- **재사용성**: 기존의 잘 설계된 모듈을 쉽게 재사용할 수 있습니다. 이는 개발 시간과 비용을 절감합니다.
- **유지보수성**: 기존 코드에 대한 변경이 필요 없으므로, 버그 발생 위험이 줄어들고 유지보수가 용이해집니다.

#### OCP 적용 예시

고전적인 OCP 위반 예시로는 다양한 도형의 면적을 계산하는 클래스를 들 수 있습니다. 새로운 도형이 추가될 때마다 면적을 계산하는 클래스를 수정해야 한다면, 이는 OCP를 위반하는 것입니다.

```java
class AreaCalculator {
    public double calculateShapeArea(Shape shape) {
        if (shape instanceof Circle) {
            Circle circle = (Circle) shape;
            return Math.PI * circle.radius * circle.radius;
        } else if (shape instanceof Square) {
            Square square = (Square) shape;
            return square.length * square.length;
        }
        // 새로운 도형이 추가될 때마다 여기에 코드를 추가해야 함
    }
}
```

위 코드는 새로운 도형이 추가될 때마다 `calculateShapeArea` 메소드를 수정해야 하므로 OCP를 위반합니다.

OCP를 준수하는 설계는 다음과 같습니다.

```java
interface Shape {
    double area();
}

class Circle implements Shape {
    double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

class Square implements Shape {
    double length;

    public Square(double length) {
        this.length = length;
    }

    @Override
    public double area() {
        return length * length;
    }
}

class AreaCalculator {
    public double calculateTotalArea(Shape[] shapes) {
        double totalArea = 0;
        for (Shape shape : shapes) {
            totalArea += shape.area();
        }
        return totalArea;
    }
}
```

이 예시에서 `AreaCalculator` 클래스는 `Shape` 인터페이스의 `area` 메소드를 호출하여 면적을 계산합니다. 새로운 도형이 추가되더라도 `Shape` 인터페이스를 구현하면 되므로, `AreaCalculator` 클래스를 수정할 필요가 없습니다. 이는 OCP 원칙을 잘 따르는 설계입니다.

#### 정리

개방-폐쇄 원칙은 소프트웨어의 확장성과 유지보수성을 크게 향상시킬 수 있는 중요한 디자인 원칙입니다. 적절한 추상화와 인터페이스를 사용하여 시스템을 설계함으로써, 새로운 기능을 추가하거나 변경할 때 기존 코드를 수정하지 않고도 요구사항을 충족시킬 수 있습니다.

### L - 리스코프 치환 원칙(Liskov Substitution Principle, LSP)

리스코프 치환 원칙(LSP)은 객체 지향 프로그래밍의 SOLID 원칙 중 하나로, 파생 클래스는 기반 클래스의 대체 가능해야 한다는 원칙입니다. 이 원칙은 1987년 바바라 리스코프에 의해 소개되었으며, 파생 클래스가 기반 클래스의 행동을 정확히 모방해야 한다는 아이디어를 담고 있습니다. 즉, 기반 클래스의 인스턴스를 파생 클래스의 인스턴스로 대체해도 프로그램의 정확성이 변하지 않아야 합니다.

#### LSP의 중요성

- **호환성**: 파생 클래스는 기반 클래스와 호환되어야 하므로, 기반 클래스를 사용하는 기존 코드를 변경하지 않고도 파생 클래스를 사용할 수 있습니다.
- **재사용성**: 기반 클래스의 기능을 재사용하면서 새로운 기능이나 행동을 추가할 수 있습니다.
- **유지보수성**: 기반 클래스의 변경이 파생 클래스에 영향을 미치지 않으므로, 시스템의 유지보수가 용이해집니다.

#### LSP 위반 예시

```java
class Bird {
  fly() {
    // 날다
  }
}

class Penguin extends Bird {
  fly() {
    throw new Error("펭귄은 날 수 없습니다.");
  }
}
```

위 예시에서 `Penguin` 클래스는 `Bird` 클래스를 상속받지만, `fly` 메소드를 오버라이드하여 "펭귄은 날 수 없다"는 예외를 던집니다. 이는 LSP를 위반하는 것으로, `Bird` 클래스의 인스턴스를 `Penguin` 클래스의 인스턴스로 대체할 수 없게 만듭니다.

#### LSP 준수 예시

LSP를 준수하기 위해서는 공통된 행동을 가진 상위 클래스나 인터페이스를 정의하고, 각 하위 클래스에서 이를 구현하거나 확장하는 방법을 사용할 수 있습니다.

```java
interface Flyable {
  fly();
}

class Bird implements Flyable {
  fly() {
    // 날다
  }
}

class Eagle extends Bird {
  fly() {
    // 독수리 날다
  }
}

class Penguin extends Bird {
  swim() {
    // 펭귄 수영하다
  }
}
```

이 예시에서는 날 수 있는 새를 나타내는 `Flyable` 인터페이스를 정의하고, `Eagle` 클래스는 이 인터페이스를 구현하여 날 수 있음을 명시합니다. 반면, `Penguin` 클래스는 `Flyable` 인터페이스를 구현하지 않고, 대신 수영할 수 있다는 별도의 행동을 정의합니다. 이렇게 함으로써, 모든 새가 날 수 있다는 가정을 피하면서 LSP를 준수할 수 있습니다.

#### 정리

리스코프 치환 원칙은 객체 지향 설계에서 중요한 원칙 중 하나입니다. 이 원칙을 준수함으로써, 시스템의 유연성과 확장성을 향상시키고, 기존 코드의 재사용성을 높일 수 있습니다. 따라서, 설계 단계에서부터 LSP를 염두에 두고 클래스와 인터페이스를 설계하는 것이 중요합니다.

### I - 인터페이스 분리 원칙(Interface Segregation Principle, ISP)

인터페이스 분리 원칙(Interface Segregation Principle, ISP)은 객체 지향 프로그래밍의 SOLID 원칙 중 하나로, "클래스는 자신이 사용하지 않는 인터페이스는 구현하도록 강제되어서는 안 된다"는 원칙입니다. 이 원칙은 더 구체적인 인터페이스를 만드는 것이 크고 일반적인 하나를 만드는 것보다 낫다는 아이디어에 기반을 두고 있습니다.

#### ISP의 중요성

- **코드의 명확성과 간결성**: 각 인터페이스가 특정 기능에 집중하도록 함으로써, 코드의 명확성과 간결성을 향상시킵니다.
- **유연성과 재사용성 향상**: 필요한 인터페이스만을 구현함으로써, 클래스의 유연성과 재사용성이 향상됩니다.
- **유지보수 용이성**: 클래스가 필요하지 않은 기능을 구현하도록 강제되지 않으므로, 유지보수가 더 용이해집니다.

#### ISP 위반 예시

```java
interface Book {
  read();
  download();
}

class OnlineBook implements Book {
  public void read() {
    // 읽기 기능 구현
  }

  public void download() {
    // 다운로드 기능 구현
  }
}

class PhysicalBook implements Book {
  public void read() {
    // 읽기 기능 구현
  }

  public void download() {
    // 물리적인 책에 대한 다운로드는 의미가 없음
  }
}
```

위 예시에서 `PhysicalBook` 클래스는 `download` 메소드를 구현해야 하지만, 물리적인 책에 대해 다운로드 기능은 불필요하거나 의미가 없습니다. 이는 ISP를 위반하는 것입니다.

#### ISP 준수 예시

ISP를 준수하기 위해서는 인터페이스를 더 작고 구체적으로 분리할 수 있습니다.

```java
interface Readable {
  void read();
}

interface Downloadable {
  void download();
}

class OnlineBook implements Readable, Downloadable {
  public void read() {
    // 읽기 기능 구현
  }

  public void download() {
    // 다운로드 기능 구현
  }
}

class PhysicalBook implements Readable {
  public void read() {
    // 읽기 기능 구현
  }
}
```

이 예시에서는 `Readable`과 `Downloadable`이라는 두 개의 인터페이스로 분리하여 `OnlineBook`은 두 인터페이스 모두를, `PhysicalBook`은 `Readable` 인터페이스만을 구현합니다. 이로써 각 클래스는 자신에게 필요한 기능만을 구현하게 되며, ISP 원칙을 준수하게 됩니다.

#### 정리

인터페이스 분리 원칙은 클래스가 불필요한 의존성을 갖지 않도록 하여, 시스템의 유연성과 유지보수성을 향상시키는 중요한 디자인 원칙입니다. 각 인터페이스가 명확하고 구체적인 역할을 가지도록 설계함으로써, 더 깔끔하고 재사용 가능한 코드를 작성할 수 있습니다.

### D - 의존성 역전 원칙(Dependency Inversion Principle, DIP)

의존성 역전 원칙(Dependency Inversion Principle, DIP)은 객체 지향 프로그래밍의 SOLID 원칙 중 하나로, "추상화에 의존하고 구현체에 의존하지 않아야 한다"는 원칙입니다. 이 원칙은 고수준 모듈이 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화에 의존해야 한다고 주장합니다. 즉, 추상화는 세부 사항에 의존하지 않고, 세부 사항은 추상화에 의존해야 합니다.

#### DIP의 중요성

- **유연성**: 시스템의 구성요소 간의 의존성을 줄여, 시스템의 유연성을 증가시킵니다. 이는 나중에 구현체를 교체하거나 수정할 때, 고수준 모듈을 변경하지 않고도 가능하게 합니다.
- **재사용성**: 추상화를 통해 고수준 모듈을 재사용하기 쉽게 만듭니다. 다양한 저수준 모듈(구현체)와 함께 동일한 고수준 모듈을 사용할 수 있습니다.
- **테스트 용이성**: 추상화를 사용함으로써, 실제 구현 대신 모의 객체나 스텁을 사용하여 고수준 모듈을 쉽게 테스트할 수 있습니다.

#### DIP 위반 예시

```java
class MySQLDatabase {
    public String getUserData(int id) {
        // MySQL 데이터베이스에서 사용자 데이터를 가져오는 로직
    }
}

class UserService {
    private MySQLDatabase database = new MySQLDatabase();

    public String getUser(int id) {
        return database.getUserData(id);
    }
}
```

위 예시에서 `UserService` 클래스는 `MySQLDatabase` 클래스에 직접 의존하고 있습니다. 이는 DIP를 위반하는 것으로, 다른 데이터베이스로 전환하고자 할 때 `UserService` 클래스도 수정해야 합니다.

#### DIP 준수 예시

DIP를 준수하기 위해, 우선 데이터베이스 작업을 위한 추상화(인터페이스)를 정의합니다.

```java
interface Database {
    String getUserData(int id);
}

class MySQLDatabase implements Database {
    public String getUserData(int id) {
        // MySQL 데이터베이스에서 사용자 데이터를 가져오는 로직
    }
}

class PostgreSQLDatabase implements Database {
    public String getUserData(int id) {
        // PostgreSQL 데이터베이스에서 사용자 데이터를 가져오는 로직
    }
}

class UserService {
    private Database database;

    public UserService(Database database) {
        this.database = database;
    }

    public String getUser(int id) {
        return database.getUserData(id);
    }
}
```

이 예시에서 `UserService`는 구체적인 데이터베이스 구현체가 아닌 `Database` 인터페이스에 의존합니다. 이로써, MySQL이나 PostgreSQL 등 어떤 데이터베이스 구현체를 사용하더라도 `UserService` 클래스를 변경할 필요가 없게 됩니다. 이는 DIP 원칙을 잘 준수하는 설계입니다.

#### 정리

의존성 역전 원칙은 시스템의 결합도를 낮추고 유연성을 높여, 유지보수성과 확장성을 개선하는 데 도움을 줍니다. 추상화를 통해 고수준 모듈과 저수준 모듈 간의 직접적인 의존성을 제거함으로써, 시스템의 다양한 부분을 독립적으로 개발하고 테스트할 수 있게 됩니다.

## 결론

SOLID 원칙을 채택함으로써 개발자들은 변화에 더욱 탄력적인 시스템을 구축할 수 있으며, 유지보수를 용이하게 하고 시간이 지남에 따라 코드 품질을 개선할 수 있습니다. 이 다섯 가지 원칙은 소프트웨어 개발 과정에서 매우 중요한 역할을 하며, 각각은 다음과 같은 이점을 제공합니다:

1. **단일 책임 원칙(SRP)**은 클래스가 하나의 기능만을 가지도록 하여, 코드의 유지보수성과 가독성을 향상시킵니다. 이를 통해 시스템의 복잡성을 줄이고, 재사용성과 테스트 용이성을 높일 수 있습니다.

2. **개방-폐쇄 원칙(OCP)**은 기존 코드를 수정하지 않고도 시스템의 기능을 확장할 수 있도록 합니다. 이 원칙은 유연성, 재사용성, 유지보수성을 향상시키는 데 중요합니다.

3. **리스코프 치환 원칙(LSP)**은 파생 클래스가 기반 클래스의 대체 가능해야 함을 의미합니다. 이 원칙을 준수함으로써, 시스템의 유연성과 확장성을 향상시키고, 기존 코드의 재사용성을 높일 수 있습니다.

4. **인터페이스 분리 원칙(ISP)**은 클래스가 사용하지 않는 인터페이스를 구현하도록 강제되지 않도록 하여, 코드의 명확성과 간결성을 향상시킵니다. 이 원칙은 유연성과 재사용성을 증가시키고, 유지보수를 용이하게 합니다.

5. **의존성 역전 원칙(DIP)**은 고수준 모듈이 저수준 모듈에 의존하지 않고, 둘 다 추상화에 의존해야 한다고 주장합니다. 이 원칙은 시스템의 결합도를 낮추고 유연성을 증가시켜, 유지보수성과 확장성을 개선합니다.

각 원칙은 소프트웨어 개발의 다양한 측면에서 중요한 역할을 하며, 함께 사용될 때 시스템의 전반적인 설계와 구현을 크게 개선할 수 있습니다. 이러한 원칙들을 이해하고 적용함으로써, 개발자는 더욱 견고하고 유지보수가 쉬운 소프트웨어를 개발할 수 있으며, 이는 장기적으로 프로젝트의 성공에 크게 기여할 것입니다. 따라서, SOLID 원칙은 현대 소프트웨어 개발에서 필수적인 지침으로 여겨지며, 이를 통해 개발자들은 변화하는 요구사항과 기술의 발전에 효과적으로 대응할 수 있습니다.