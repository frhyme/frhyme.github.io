---
title: python의 default parameter는 가변적(mutable)이다.
category: python-basic
tags: python python-basic default-parameter
---

## 2-line summary 

- `def func1(a=[])`이라고 해둔다고 해서 `a`라는 parameter의 value가 함수 콜마다 `[]`로 초기화되는 것이 아니다. 
- 저렇게 해두면 함수를 콜할 때마다 같은 object에 접근하게 됩니다.

## weird default parameter

- 예를 들어 설명하는 것이 더 좋습니다. 
- 다음과 같은 간단한 python code가 있다고 합시다. 매우 간단한 코드이며, `func1`은 `a`라는 parameter의 초기값(default value)를 `[]`로 가지며, 여기에 3을 추가한 list를 리턴하죠.

```python
def func1(a=[]):
    a.append(3)
    return a
print(func1())
print(func1())
print(func1())
```

- 매우 간단한 코드이며, 우리의 의도대로라면, 위 코드의 실행 결과는 모두 같아야 합니다. 그냥 `[3]`을 출력하는 형태가 되는 것이어야 합니다.
- 하지만 안타깝게도 결과를 보시면, 이전 함수에서의 기억을 그대로 가진 채로, 다음과 같이 출력됩니다. 마치, 함수 내부에서 함수 실행시마다 새롭게 a에 값을 할당하는 것이 아니라, 이전의 값을 계속 공유하게 되는것이죠.

```plaintext
[3]
[3, 3]
[3, 3, 3]
```

- 어 이상한데? "내가 파이썬의 거대한 버그를 발견한 것 같아!!"라는 생각이 드신다면 이 글을 읽으러 잘 오신 것이 맞습니다. 이건 문제가 아니라, 파이썬의 특성일 뿐이죠.

## function is also object in python

- python에서는 모든 것이 object입니다. function 또한 마찬가지죠. 돌아가는 것은 함수처럼 돌아가지만 그냥 class라고 봐도 상관없어요. 
- 그리고, parameter는 함수 `func1`의 parameter `a`는 class attribute로 존재합니다. 즉, 매 함수를 콜할때마다 새로운 instance를 만들어주는 것이 아니고, 동일한 값을 class 내부에 지정해두고 같은 값을 공유하게 되는 것이죠.

### 왜 그렇게 하느냐? 비효율적인것 아닌가? 

- 그럴 수도 있습니다만, 이는 오히려 여러 instance를 만든다고 할때 그 강점이 부각되죠. 예를 들어봅시다. 다음의 코드가 있다고 할게요. parameter value가 "함수"죠. 만약, 각 instance들에 대해서 따로따로 member attribute로 해당 값을 정의해준다면, 어떤 일이 발생할까요? 모든 함수별로 따로 함수를 정의하게 됩니다. 따라서, 함수 콜이 발생할대마다 해당 함수는 복제되고, 메모리는 터지게 되겠죠.
- 특히, 이렇게 parameter를 하나로서 관리하는 것은, recursion을 사용할 때 매우 탁월하게 사용될 수 있습니다.

```python
def func1(sin=np.sin, cos=np.cos):
    pass
```

- 따라서, 만약 parameter가 함수가 실행될때마다 매번 초기화되는 것을 원한다면, 함수 내부에 다음과 같이 작성해주는 것이 좋습니다.

```python
def func1(a=None):
    if a is None: 
        a = []
```

## check default parameter 

- 만약, 현재 default parameter value가 어떻게 변하는지 파악하고 싶다면 다음 메소드를 사용하면 됩니다.

```python
def func1(a=[]):
    a.append(3)
    return a

func1()
print(func1.__defaults__)
func1()
print(func1.__defaults__)
func1()
print(func1.__defaults__)
```

```plaintext
([3],)
([3, 3],)
([3, 3, 3],)
```

## wrap-up

- python으로 코딩을 정말 오래했는데도 불구하고, 이걸 이제 알았다니...부끄럽군요 호호호.

## reference

- [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm)
- [mutalbe default argument](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)
