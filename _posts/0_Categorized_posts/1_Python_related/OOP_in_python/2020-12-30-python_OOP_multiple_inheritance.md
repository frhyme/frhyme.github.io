---
title: python - OOP - multiple Inheritance
category: python
tags: python OOP inheritance
---

## python - multiple Inheritance

- python에서는 multiple inheritance(다중 상속)이 가능합니다. 다중 상속은 말 그대로 "2개 이상의 class를 상속받는 것"을 말하죠.
- 다음 코드에서 class `AABB`는 `AA` Class 와 `BB` Class를 모두 상속 받습니다. 이런게 바로 multiple inheritance죠.

```python
class AA:
    def print(self):
        print("This is AA")

class BB:
    def print(self):
        print("This is BB")

class AABB(AA, BB):
    def print(self):
        print("This is AABB")
```

## Method Resolution Order (MRO)

- 다만, 다음과 같이, `AABB`는 `AA`, `BB`의 순서로 상속받고, `BBAA`는 `BB`, `AA`로 상속받습니다.
- 그리고 두 class의 `print` method에서는 모두 `super().print()`를 통해 상위 class의 `print()` 메소드를 호출하죠.
- 그렇다면, 이렇게 다중상속이 발생한 경우에 `super()`는 어떤 class를 가리킬까요?

```python
class AA:
    def print(self):
        print("This is AA")

class BB:
    def print(self):
        print("This is BB")

class AABB(AA, BB):
    def print(self):
        # 여기서 super()는 어떤 class를 가리킬까요?
        super().print()
        print("This is AABB")

class BBAA(BB, AA):
    def print(self):
        # 여기서 super()는 어떤 class를 가리킬까요?
        super().print()
        print("This is BBAA")

## Class Definition Done
print("== AABB class instance")
aabb = AABB()
aabb.print()
print("==============================")
print("== BBAA class instance")
bbaa = BBAA()
bbaa.print()
```

- 수행 결과는 다음과 같습니다.
- `AABB`의 super class는 `AA`이고, `BBAA`의 super class는 `BB` 라는 것이죠.
- 이는 사실상 다중상속이라고 되어 있지만, class 간에 충돌이 발생할 경우, 우선순위가 존재한다, 라는 것이죠. 사실 매우 당연한 이야기입니다. 컴퓨터는 확실한 걸 좋아하기 때문에 우선순위를 정해놓아야 하는 것이죠.

```plaintext
== AABB class instance
This is AA
This is AABB
==============================
== BBAA class instance
This is BB
This is BBAA
```

- 다중상속 상황에서 충돌이 발생했을 때 실행되는 우선순위를 MRO(Method Resolution Order)라고 합니다. 
- MRO를 정하는 방법은 다양하지만, python의 경우 [C3 Lineariation](https://en.wikipedia.org/wiki/C3_linearization)를 사용하죠.
- 아래에서 확인해보면, `AABB`와 `BBAA`의 mro는 서로 다른 것을 알 수 있죠. 
- 즉, python에서 다중상속을 정할 때는 먼저 오는 class가 충돌시 우선순위를 가지게 됩니다.

```python
print( AABB.__mro__ )
# (<class '__main__.AABB'>, <class '__main__.AA'>, <class '__main__.BB'>, <class 'object'>)
print("==============================")
print( BBAA.__mro__ )
# (<class '__main__.BBAA'>, <class '__main__.BB'>, <class '__main__.AA'>, <class 'object'>)
```

## MRO with Diamond Problem

- 이번에는 Class의 관계가 다음과 같이 Diamond Problem으로 구성되어 있는 경우를 고려해보겠습니다.
- `BASE`는 `AA`, `BB`에 상속되고, `AA`, `BB`는 `AABB`, `BBAA`에 다시 상속되므로 각각 다이아몬드 패턴이 생성되죠.
- 그리고 모든 `print()` method는 내부에서 `super().print()`를 통해서 상위 클래스의 `print()`메소드를 호출합니다.

```python
class BASE:
    def print(self):
        print("This is BASE")

class AA(BASE):
    def print(self):
        super().print()
        print("This is AA")

class BB(BASE):
    def print(self):
        super().print()
        print("This is BB")

class AABB(AA, BB):
    def print(self):
        super().print()
        print("This is AABB")

class BBAA(BB, AA):
    def print(self):
        super().print()
        print("This is BBAA")
```

- 그럼, 여기서 다시 `BBAA`와, `AABB`의 mro를 확인해보겠습니다.
  - `AABB`는 AA, BB, BASE의 순으로 MRO가 구성되어 있고
  - `BBAA`는 BB, AA, BASE의 순으로 MRO가 구성되어 있죠. 
- 그렇다면, 아마 그 역순에 맞춰서, `print` method가 실행되겠죠.

```python
print( AABB.__mro__ )
(<class '__main__.AABB'>, <class '__main__.AA'>, <class '__main__.BB'>, <class '__main__.BASE'>, <class 'object'>)

print( BBAA.__mro__ )
(<class '__main__.BBAA'>, <class '__main__.BB'>, <class '__main__.AA'>, <class '__main__.BASE'>, <class 'object'>)
```

- 네, mro와 동일한 순서로 실행되는 군요.

```python
aabb = AABB()
aabb.print()
# This is BASE
# This is BB
# This is AA
# This is AABB

bbaa = BBAA()
bbaa.print()
# This is BASE
# This is AA
# This is BB
# This is BBAA
```
