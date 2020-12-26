---
title: python에서 getattr 덮어씌우기. 
category: python-basic
tags: python python-basic getattr class
---

## what is getattr?

- 우선 getattr에 대해서 먼저 알아봅시다. `getattr`은 그냥 각 오브젝트에서 해당 오브젝트의 attribute를 가져오는 펑션입니다. 기본적으로 파이썬에서 지원되는 built-in function이구요. 
- 간단하게 다음으로 보시면 되죠. 
- 각 오브젝트의 어트리뷰트를 직접 접근할 수도 있지만, 다음처럼 함수를 사용해서 접근할 수도 있습니다. 범용적인 측면에서는 `getattr`를 쓰는 것이 코드를 좀더 효율적으로 짤 수 있게 되죠. 

```python
class JustProperty(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp ## private attribute
        self.name = name

pro1 = JustProperty("shlee", "frhyme", 150, "seunghoonlee")
print(pro1.username)
print(pro1._id) 
print(getattr(pro1, "_id"))
print(getattr(pro1, "aaa")) #error because attribute name 'aaa' doesn't exist in the object
```

- 하지만 실행 결과를 보시면 제일 아래 쪽에 존재하지 않는 이름을 넣었을때 문제가 발생하는 것을 알 수 있습니다. 

```plaintext
shlee
frhyme
frhyme
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-13-eabf6bf709f8> in <module>()
     10 print(pro1._id)
     11 print(getattr(pro1, "_id"))
---> 12 print(getattr(pro1, "aaa"))

AttributeError: 'JustProperty' object has no attribute 'aaa'
```

- 사실 존재하지 않는 것을 넣는 것 자체가 문제일 수도 있지만, 이 경우 발생하는 에러 코드를 다른 식으로 구동할 수 있습니다. 어떻게 하냐면, 내부에 `gettattr`메소드를 만들어 주는 것이죠.

## define getattr method

- 아래와 같이 내부에 메소드를 하나 추가해줍니다. 
- 이렇게 하면, 내부에 없는 변수에 대해 `getattr`로 접근하면 특정한 코드를 만들어주게 되죠.

```python
class JustProperty(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp ## private attribute
        self.name = name
    def __getattr__(self, name):
        # getattr function is built-in function in python 
        return "{} attribute is not defined".format(name)

pro1 = JustProperty("shlee", "frhyme", 150, "seunghoonlee")
print(pro1.username)
print(pro1._id) 
print(getattr(pro1, "_id"))
print(getattr(pro1, "aaa")) #error because attribute name 'aaa' doesn't exist in the object
```

```plaintext
shlee
frhyme
frhyme
aaa attribute is not defined
```

## wrap-up

- 코드시그널에서 문제를 풀다가 알게 된 것인데, 사실 이후에 이걸 필요로 할 때가 있을지 솔직히 잘 모르겠습니다만, 아무튼 뭐 그렇다고 합니다.
