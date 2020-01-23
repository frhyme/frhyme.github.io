---
title: divmod in python
category: python-basic
tags: python python-basic divmod
---

## what is divmod? 

- `a`와 `b`라는 값이 있고, 몫과 나머지를 구한다고 해봅시다. 아마도 대부분의 사람들은 다음과 같이 코드를 짤 것 같습니다. 

```python
print(a//b, a%b)
```

- 매우 일반적이고, 당연한 것이기는 한데, python에서는 `divmod`라는 함수를 built-in function으로 지원합니다. 따라서, 다음처럼 하면 같은 방식으로 문제가 해결되죠. 

```python
print(divmod(a, b))
```

- 뭐, 다 좋은데요, 여기서 제가 가지는 의문은 **이걸 내장함수로서 따로 만들 필요가 있었는가**입니다. 기존의 방식이 좀더 직관적이고, 가독성이 좋다고 생각됩니다만, 
- 물론 속도 측면에서는 조금 차이가 있기는 합니다. `divmod`가 약 30% 더 빠르네요. 

```python
a = 32423423423523523529803293242342342352352352980329324234234235235235298032932423423423523523529803293242342342352352352980329
b = 334234534
%timeit divmod(a, b)
%timeit a//b, a%b
```

```
The slowest run took 5.73 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 411 ns per loop
1000000 loops, best of 3: 613 ns per loop
```

## wrap-up

- `divmod`가 왜 생겼는지를 좀 찾아보려고 했는데, 그런 부분은 따로 없는 것 같습니다. 꽤 오래 찾았는데 없어서 그냥 넘어갔습니다. 
- stackoverflow에도 물어봤는데 욕만 먹었습니다 하하하핫
- 그리고, 생각보다 built-in 함수의 source code를 보는건 성가신 것 같습니다. 오히려, 다른 모듈들, 예를 들면 `numpy`같은 모듈의 코드는 `inspect.getsource`를 활용하거나, jupyter notebook에서는 `numpy??`를 쳐서 쉽게 확인할 수 있는데, 빌트인함수는 어렵네요.