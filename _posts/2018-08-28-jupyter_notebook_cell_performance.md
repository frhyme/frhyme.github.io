---
title: jupyter notebook에서 현재 cell performance 체크하기 
category: python-lib
tags: python python-lib timeit jupyter-notebook 
---

## 성능을 체크합시다. 

- 저는 jupyter notebook에서 대부분의 코드를 작성합니다. 남들처럼 vs code를 쓰거나 atom을 쓰거나 하지 않고 jupyter notebook을 고집하는 이유는, 결과를 바로바로 확인하면서 코딩하기 편해서겠죠. 
- 또 jupyter notebook은 하나의 cell별로 코드를 따로 굴릴 수 있어요. 물론 이전의 셀에서 선언한 변수가 다음 셀에서도 살아있는등의 문제가 있어서 가끔 문제가 생길때도 있지만, cell별로 코드를 따로 굴리니까 일정이상 코드가 늘어나면 알아서 함수로 변경하고 줄이고 그런 습관이 생기는 것 같아요. 쓸데없이 코드가 길어지지 않는다는 것, 그거 매우 좋은 습관이라고 생각하구요. 
- 여기서 잠깐, 앞서 말한 것처럼 셀별로 코드를 쓰고 코드가 잘쓰여졌는지 테스트하면서 코드를 씁니다. 
- 이 과정에서 가장 많이 하게 되는 것은 아마도 성능 체크죠. 얘가 충분히 빠른가, 다른 애가 더 빠른것은 아닌가? 비교를 해야 하니까요. 

## %%timeit

- 간단합니다. 아래처럼 하시면 됩니다. 참고삼아 말씀드리면, `%`가 하나인 경우는 line command, `%%`인 경우는 cell command에요. 즉 아래처럼 `%%`인 경우는 해당 커맨드 아래의 모든 코드를 실행한다고 보시면 되는 거죠. 
    - `-r`은 몇 회, `-n`은 회당 몇 번 수행할 것인지를 말하는 command 변수입니다. 

```python
%%timeit -n 500 -r 10
def test_func(s):
    return sum([i for i in range(0, s)])
test_func(100)
```

```
8.64 µs ± 2.72 µs per loop (mean ± std. dev. of 10 runs, 500 loops each)
```

## %%time

- 한번만 실행하고 싶을 때는 다음처럼 하시면 됩니다. `%%timeit`를 사용했을 때 보다 값이 미묘하게 커진 느낌이 있는데, 이유는 모르겠네요. 그냥 모를려구요 하하하하핫

```python
%%time
def test_func(s):
    return sum([i for i in range(0, s)])
test_func(100)
```

```
CPU times: user 18 µs, sys: 1 µs, total: 19 µs
Wall time: 22.9 µs
```


## wrap-up

- `%%timeit`를 사용해서 셀별로 코드가 적당히 빠르게 돌아가는지를 파악하면서 진행해봅시다. 