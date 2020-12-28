---
title: python basic - super()
category: python
tags: python OOP super inheritance MRO
---

## python basic - super()

- `super()` function은 보통 상속(Inheritance)에서 상위 class의 method에 접근할 때 사용합니다.
- 가령 다음과 같이 간단한 `Child` class의 `print()` method를 사용할 수 있죠.

```python
class Parent():
    def print(self):
        print("This is Parent")

class Child(Parent):
    def print(self):
        # super()를 사용하여 상속받은 class인 Parent에 접근하여 
        # Parent.print()를 사용합니다.
        super().print()
        print("This is Child")

c = Child()
c.print()
#  This is Parent
#  This is Child
```

- 보통, 이렇게 간단하게 '바로 위의 부모 class'에 접근하기 위해서만 사용합니다만, 여기서는 좀 더 복잡한 예제를 만들어 보겠습니다.
- 우선 `super()`에 대한 좀 더 자세한 설명을 먼저 하겠습니다.

```python
def super(type, object_or_type):
    """
    - super function은 상속관계에서 근접한 object를 리턴하는 function이다.
    - 보통 상속 관계에서 Overriding이 발생한 경우 super function을 사용하여 method에 접근한다.
    - 첫번째 argument인 type은 탐색을 시작할 영역(exclusive)을 말하고,
    - 두번째 argument인 object_or_type의 경우, 검색 순서를 정하게 됩니다.
        - object인 경우에는 isinstance(object_or_type, type)이 true여야 하고
        - type인 경우에는 issubclass(object_or_type, type)이 ttrue여야 함.
    - Example
        - 상속 관계가 A -> B -> C -> D 로 되어 있다고 합시다.
        - 이때 super(A, a)를 실행할 경우
        type은 A 이고, object_or_type은 A의 Instance인 a를 받은 것이죠.
        - 따라서, a가 가지고 있는 검색의 순서(Method Resolution Order)를 참고합니다. 
        - 그런데, 얘는 선형적인 상속이므로(다중 상속이 없는), 
        순서가 그냥 A -> B -> C -> D로 구성되어 있죠.
        - 따라서 결과는 A의 다음인 B -> C -> D의 순서로 method를 검색하게 됩니다.
    """
```

- 무슨 말인지 모르겠죠? 네 저도 존나 모르겠습니다. 그러니, 예제를 통해 배워보도록 하죠 호호.
- 다음 코드에는 `GrandGrandParent` > `GrandParent`, `Parent` > `Child`로 이어지는 상속 관계가 있습니다.

```python
class GrandGrandParent():
    def __init__(self, name="GGP"):
        self.name = name

    def print(self):
        print("This is GrandGrandParent", self.name)

class GrandParent(GrandGrandParent):
    def __init__(self, name="GP"):
        self.name = name

    def print(self):
        print("This is GrandParent", self.name)

class Parent(GrandParent):
    def __init__(self, name="P"):
        self.name = name

    def print(self):
        print("This is Parent", self.name)

class Child(Parent):
    def __init__(self, name="C"):
        self.name = name

    def print(self):
        print("This is Child", self.name)
```

- 위 클래스의 상속 관계 상태에서, `super()`를 다양하게 실행해 보면 다음과 같죠.

```python
c = Child("CCC")
# 상속을 1차원으로 받았기 때문에
# instance c의 MRO는 
# Child > Parent > GrandParent > GrandGrandPareant > Object로 구성되어 있다.
print(Child.__mro__)
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.GrandParent'>, <class '__main__.GrandGrandParent'>, <class 'object'>)


# GrandParent부터 MRO에 따라 탐색을 시작하므로(시작점 제외)
# GrandGrandParent에 존재하는 method를 실행하게 된다.
super(GrandParent, c).print()
# This is GrandGrandParent CCC

# Parent부터 MRO에 따라 탐색을 시작하므로
# GrandParent에 존재하는 method를 실행하게 된다.
super(Parent, c).print()
# This is GrandParent CCC

# Child부터 MRO에 따라 탐색을 시작하므로
# Parent에 존재하는 method를 실행하게 된다.
super(Child, c).print()
# This is Parent CCC
```

- 물론 그냥 다음처럼 사용해도 되기는 합니다. 추천하지는 않습니다. 

```python
c = Child("c")
GrandGrandPareant.print(c)
# This is GrandGrandParent CCC
```

## Wrap-up

- 처음에는 그냥 "GrandParent에 `super()`를 사용해서 어떻게 접근하지?"가 궁금했던 것이었는데 하다보니 좀 파고들게 되었습니다.
- 사실 앞으로도 저는 그냥 바로 위에 있는 class에 접근하는 `super()`만을 사용할 것 같기는 합니다.
- 다만, 복잡한 상속관계가 존재할 때, MRO라고 하는 방식으로 적합한 method를 찾아낸다, 라는 것은 기억해 두어야 할 것 같아요.
