---
title: Python - Object Interning
category: python-basic
tags: python python-basic Interning
---

## Intro - 같은 Object는 여러 번 생성하지 말자 

- 다음의 파이썬 코드를 봅니다.
- 분명 서로 다른 변수이므로 다른 메모리 공간에 존재해야 하는데, 같은 메모리 공간을 가지고 있는 것을 알 수 있죠.

```python
a = "abc"
b = "abc"

print(id(a)) # 4412807472
print(id(b)) # 4412807472
```

- 이게, 본 글을 쓰게 된 이유입니다. 왜 서로 다른 변수인데, 같은 메모리 주소에 존재하는가? 

## Object interning

- 결론부터 말하자면, python은 **Object interning**이라는 기법을 사용하고 있기 때문입니다
- Object Interning은 **"변하지 않는(immutable)한 객체에 대해서 하나의 동일한 값만을 메모리에 저장하여 메모리를 효율적으로 관리하는 방식"**을 말합니다.
- 즉, String을 동시에 여러 변수에 복사하여 배치함으로써, 메모리를 낭비시키지 말고, 하나의 스트링을 만들고, 다른 변수들이 동시에 이 아이를 가리키도록 함으로써, 메모리 공간을 효율적으로 사용하는 것을 목적으로 하죠. 

## Python Default Interning

- python의 경우 기본적으로 문자열과 정수에 대해서 interning을 통해 관리합니다.
  - 문자열: 20자 미만의 공백을 포함하지 않은 문자열 
  - 정수: -5부터 256 사이의 숫자
- 실제로 REPL(Ipython)에서는 위를 정확하게 따릅니다. 
- 하지만, VScode에서 파이썬 코드를 작성하고 컴파일해서 진행할 경우에는 다음과 같이 매우 긴 문자열에 대해서도 interning이 적용됩니다 

```python
a = "abc aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aa"
b = "abc aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aa"
id(a)==id(b) # True
```

- 이 내용은 [파이썬의 효과적인 메모리 재활용 방법 - Interning](https://nephtyws.github.io/python/interning/)에 매우 효과적으로 적용되어 있는데요. 
- 이를 요약하자면, "REPL의 경우 한줄 한줄을 처리하기 때문에, 두 변수, `a`와 `b`가 같다는 것을 알지 못하고, 반면 byte 코드로 변경하는 경우에는 이를 알 수 있기 때문에, Interning을 해서 처리한다"는 이야기입니다.
- 또한, 모든 경우에 대해서 다 Interning이 되는 것은 아니고, 다음의 코드의 경우, 컴파일을 해도, 두 변수가 같은 값을 가지는 지 알기 어렵기 때문에, 다른 메모리 주소를 가진다. 라는 것이죠.

```python
a = "abc"
b = "".join(['a', 'b', 'c'])
id(a)==id(b) # False
```

## bug in python 3.7

- 당연하지만, REPL이 아닌, 코드 전체를 컴파일해서 처리하는 경우에는 코드를 읽으면서 더 효율적으로 만들 수 있는(string을 interning하여 메모리를 효과적으로 처리할 수 있는) 방법을 찾을 것이고, 그로 인해 알아서 잘 해줄겁니다. 
- 다만, [파이썬의 효과적인 메모리 재활용 방법 - Interning](https://nephtyws.github.io/python/interning/)의 말미에 작성된 것처럼, python 3.7에서는 특정한 경우에 intering이 잘 되지 않는 경우가 발생했고, 해당 문제는 버그로 이미 리포트되어 수정되어 있다고 하네요. 
- 3.8에서는 문제가 없지만, 3.7에서는 스트링 interning이 안되는 다음과 같은 문제가 있습니다. 
  - 앞서 말한 바와 같이, 특수문자인 `!`를 포함하고 있으므로 원래는 Interning이 안되는 것이 맞습니다만, 컴파일러 단에서 얘네는 같다는 것을 알아차리고, 알아서 Interning을 해주는 것이 맞습니다. 
  - 다만, 3.7에서는 tuple을 string으로 각각 변환해서 뿌려주는 단계에서 버그가 있고, 이 과정에서 다음과 같이, Interning이 되지 않죠.

```python
a, b = 'python!', 'python!'

print(id(a)==id(b))# False
```

- 다만, 흥미로운 것은 아래와 리스트로 변환한 다음, 진행을 하면 interning이 잘 되고.

```python
a, b = ['python!', 'python!']

print(id(a)==id(b))# True
```

- 아래와 같이 각각의 변수로 넣어줘도 문제없이 Interning이 된다는 것이죠.

```python
a = 'python!'
b = 'python!'

print(id(a)==id(b))# True
```

- 따라서, 메모리를 효과적으로 관리하기 위해서 interning을 사용하시려면, python 3.8로 업데이트를 하시거나, 아니면 tuple로 동시에 넣어주는 형태의 작업은 하시지 않는 것이 좋겠습니다.

## wrap-up 

- python에 대해서 이제 꽤 잘알고 있다고 생각했는데, 공부는 하면 할수록 늘어나는 군요 호호호. 
- 그래도, 이 내용을 정리한 덕분에, python에서 메모리 공간을 어떠한 방식으로 할당해주고, 컴파일러가 메모리를 효과적으로 관리하기 위해서 어떠한 짓을 하는지에 대해서 이해하게 된 것 같습니다. 
- 더불어, 저도 자연어 처리를 하는 과정에서 Intering을 통해 효과적으로 메모리를 확보해야할 필요가 있는데, 이를 위해서는 현재 Intering이 잘 되고 있는지를 확인하는 것이 필요하겠네요.

## Reference

- [파이썬의 효과적인 메모리 재활용 방법 - Interning](https://nephtyws.github.io/python/interning/)
