---
title: python의 default parameter는 가변적(mutable)이다.
category: python-basic
tags: python python-basic default-parameter
---

## 2-line summary 

- `def func1(a=[])`이라고 해둔다고 해서 `a`라는 parameter의 value가 함수 콜마다 `[]`로 초기화되는 것이 아니다. 
- 저렇게 해두면 함수를 콜할 때마다 같은 object

## weird default parameter

- 다음과 같은 간단한 python code가 있다고 합시다. 매우 간단한 코드이며, `func1`은 `a`라는 parameter의 초기값(default value)를 `[]`로 가지며, 여기에 3을 추가한 list를 리턴하죠.

```python
def func1(a=[]):
    a.append(3)
    return a
print(func1())
print(func1())
print(func1())
```

- 매우 간단합니다만, 결과를 보시면, 다음과 같습니다. 우리가 원래 알던 개념대로라면 `a`라는 parameter는 매번 함수 콜할 때마다 `[]`로 초기화되어야 하는데 그렇게 되지 않고, 마치 함수 외부에 선언해준 객체처럼 존재하게 되죠. 

```
[3]
[3, 3]
[3, 3, 3]
```

- 어 이상한데? "내가 파이썬의 거대한 버그를 발견한 것 같아!!"라는 생각이 드신다면 이 글을 읽으러 잘 오신 것이 맞습니다. 이건 문제가 아니라, 파이썬의 특성일 뿐이죠.

## function is also object in python.

- python에서는 모든 것이 object입니다. function 또한 마찬가지죠. 돌아가는 것은 함수처럼 돌아가지만 그냥 class라고 봐도 상관없어요. 
- 그리고, parameter는 함수 `func1`의 parameter `a`는 class attribute로 존재합니다. 즉, 매 함수를 콜할때마다 새로운 instance를 만들어주는 것이 아니고, 동일한 값을 class 내부에 지정해두고 같은 값을 공유하게 되는 것이죠.

### 왜 그렇게 하느냐? 비효율적인것 아닌가? 

- 그럴 수도 있습니다만, 이는 오히려 여러 instance를 만든다고 할때 그 강점이 부각되죠. 예를 들어봅시다. 다음의 코드가 있다고 할게요. parameter value가 "함수"죠. 만약, 각 instance들에 대해서 따로따로 member attribute로 해당 값을 정의해준다면, 어떤 일이 발생할까요? 메모리는 물론이고 아무튼 더 비효율적이 됩니다. 
- 특히, 이러한 강점은 recursion을 사용할 때, 더 탁월할 수 있죠. 

```python
def func1(sin=np.sin, cos=np.cos):
    pass
```

- 따라서, 만약 parameter가 함수별로 매번 정확하게 초기화가 되길 바란다면 다음의 형식으로 사용해주는 것이 좋습니다. 


```python
def func1(a=None):
     if a is None: 
        a = []
```

## check default parameter 

- 만약, 현재 default parameter value가 변하는지 어떤지를 파악하고 싶다면 다음 메소드를 사용하면 됩니다 

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

```
([3],)
([3, 3],)
([3, 3, 3],)
```

## wrap-up

- python으로 코딩을 정말 오래했는데도 불구하고, 이걸 이제 알았다니...부끄럽군요 호호호.


## reference

- [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm)
- [mutalbe default argument](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)