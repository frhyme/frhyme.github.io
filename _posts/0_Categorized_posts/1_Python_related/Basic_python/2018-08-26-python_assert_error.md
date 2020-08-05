---
title: python에서 assert 사용하기 
category: python-basic
tags: python python-basic exception
---

## assert: 강하게 주장하기 

- `assert`는 한국말로 "강하게 주장한다" 정도로 번역될 수 있습니다. 코드에서 `assert`도 비슷합니다. 어떤 조건이 부합되지 않을 경우 강하게 문제가 발생했다는 것을 전달하는 명령어를 말합니다.
- 간단하게, 아래와 같이 사용하죠. 아래 코드에서는 `assert` 뒤의 결과가 `True`가 나오기 때문에, 코드가 문제없이 흘러갑니다. 
- 즉, `assert` 뒤에는, 절대로 성립해서는 안되는 오류를 미리 방지하기 위한 코드가 논리연산자가 들어간다고 보시면 됩니다.

```python
assert 1==1
```

- 다음과 같은 아주 간단한 예시를 들 수 있는데요. 

```python
def inc(inputA):
    ## 인풋의 타입이 제대로 들어오지 않았을 때 에러를 출력
    assert type(inputA)==int, 'not integer'
    return inputA+2 

## 함수가 적합한 값을 만들지 않을때 에러를 출력 
## error condition, error message 순으로 전달
assert inc(10)==(10+1), 'function problem'
```

- 위 코드를 수행하면 다음처럼 되는 것을 알 수 있습니다. 

```plaintext
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-70-66bb23f20d9a> in <module>()
      3     return inputA+2
      4 
----> 5 assert inc(10)==(10+1), 'function problem'

AssertionError: function problem
```

## wrap-up

- 슬슬 작성해야 하는 코드의 양이 늘어나고 있고, 그러함에도 저는 코딩을 너무 대충 하는 경향성이 있는 것 같아요. 
- 단순히 `assert`만 잘 써도 에러 핸들링을 더 잘하게 될텐데 말이져. 앞으로는 잘 쓰도록 하겠습니다.
