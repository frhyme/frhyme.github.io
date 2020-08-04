---
title: python에서 enum을 어떻게 쓸 수 있는가?
category: python-basic
tags: python-libs python python-basic enumeration
---

## what is enum?

- C로 프로그래밍을 입문하신 분들은 `enum`을 한번쯤은 사용해보신 적이 있을 것 같습니다. 물론, 이게 딱히 시험에 나오는 놈도 아니고 하니까, 굳이 기억해두지 않기는 해요. 별로 필요하지 않기도 하고요.
- 하지만, `enum`을 쓰면 코딩할때의 가독성이 올라감은 물론, 에러를 발생시킬 확률 또한 줄어듭니다. 오히려 C에서는 `enum`이 제대로 관리되지 않아서, 문제가 있는데, 다른 언어들(가령 java, swift)에서는 `enum`을 효과적으로 다룰 수 있는 것 같아요.
- 아무튼, 사실 `enum`은 그냥 필요한 혹은 특별한 값들을 상수로 정의한 것 뿐입니다. 가령, 우리가 요일별로 각 명령을 다르게 수행한다고 생각해보겠습니다. 그럼 대략 다음처럼 코드를 짤 수 있겠죠.

```python
# 0, 1, 2, 3 => EAST, WEST, SOUTH, NORTH
CurrDirection = 0
if CurrDirection == 0:
    printf("EAST")
    # 생략
```

- 뭐, 이렇게 하는 것도 문제는 없습니다만, 주석과 코드가 합쳐져서 관리되지 않기 때문에 좀 문제가 있습니다. 추가로, 0이 아닌 string으로서 관리해도 괜찮을 수 있는데, 그럼 문자열 비교이므로 시간이 좀 더 걸리게 되죠.
- 따라서, 이런 경우에 enum을 사용해서 좀더 가독성 높게 처리해줄 수 있습니다. 아래와 같이, 4가지 방향을 상수화하여 처리해줍니다. 이렇게 함으로써, 가변적인 값을 비교하는 것이 아닌, 고정된 상수를 비교하게 되는 것이죠.
  - 다만, 아래처럼 정의할때 조금 귀찮은 것은, 매번 각 상수에 대해서 어떤 값이 들어가는지 정의해주어야 한다는 것이죠.
  - C의 경우는 이 값을 지정하지 않아도 알아서 0부터 시작되는 값을 지정해줍니다. swift도 마찬가지죠.
  - 하지만 python은 각 상수마다 그 값을 일일이 지정해줘야 합니다. 어차피 상수화시켰기 때문에, 해당 상수에 무슨 값이 들어가는지는, 전혀 중요한게 아님에도 그 값을 하나하나 쳐줘야 한다는게 매우 귀찮네요.

```python
import enum

class DIRECTION(enum.Enum):# enum.Enum을 상속받음
    EAST = 0 
    WEST = 1
    SOUTH = 2
    NORTH = 3
```

- 아무튼, 이렇게 정의를 해주고 나면, 아래처럼 상수로 접근하여 사용할 수 있습니다.
- 필요한 변수에 이 enum을 이용해서 값을 정의해주고, 그 값을 논리연산자들과 함께 비교하여, 코드의 흐름을 좀 더 명확하게 정의할 수 있죠.

```python
import enum

class DIRECTION(enum.Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3

CurrDir = DIRECTION.EAST

print(CurrDir) # DIRECTION.EAST
print(type(CurrDir)) # <enum 'DIRECTION'>
print(CurrDir == 0) # False
print(CurrDir == DIRECTION.EAST) # True
```

## wrap-up

- 누군가는 필요없다고 생각할지 모르겠지만, enum만 써도 코드의 가독성은 훨씬 올라갑니다. 다만, 이를 위해서는 코딩 전에 어느 정도 데이터 타입등에 대해서 설계가 완료되어 있어야겠죠.

## reference

- [enum — Support for enumerations](https://docs.python.org/3/library/enum.html)