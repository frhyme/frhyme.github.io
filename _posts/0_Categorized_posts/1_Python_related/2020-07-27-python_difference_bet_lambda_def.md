---
title: python - lambda 함수와 def 함수의 차이
category: python-basic
tags: python python-basic lambda def function
---

## Intro - lambda 함수와 def 함수는 무엇이 다른가

- python에서 함수를 정의하는 방법은 2가지 입니다. `lambda` 식을 이용해서 변수에 assign해준다거나, 아니면 `def`구문을 이용해서 만들어준다거나 하는 방식이죠. 
- 이것이 lambda 식을 이용한 방식이지만, 사실 이런 식으로 lambda함수를 만드는 것은 좀 지양되고 있습니다. 자세한 내용은 [flake8 rules - E731](https://www.flake8rules.com/rules/E731.html)에 따르면 자세하게 알 수 있습니다.

```python
func1 = lambda x: x + 10
```

- 이것이 좀 더 보편적인 방식이고, `def`를 이용하죠. 한 줄에 표현하지 못해서 간단한 함수에 대해서는 사용하지 않죠.

```python
def func1(x):
    return x + 10
```

- 아무튼 오늘 정리하려는 것은 이 둘 간에 차이가 존재하느냐, 존재하지 않느냐에 대한 이야기입니다.

## lambda and def

- 아래와 같이, 함수 한 개는 `lambda` 구문을 사용하여, 변수에 할당하고, 다른 함수는 `def`를 사용하여 정의하였습니다. 

```python

func_defined_by_lambda = lambda x: x + 10 

def func_defined_by_def(x):
    return x+10 
```

- 그리고, 함수를 출력해보고, 각 함수의 이름을 출력해보면, 약간 이상한 점을 알수 있습니다. 
- `def`를 통해 만들어진 함수는 이름이 있는데, `lambda`를 통해 변수에 할당된 경우에는 이름이 없죠.

```plaintext
print(func_defined_by_lambda) # <function <lambda> at 0x7fbd87f424d0>
print(func_defined_by_def) # <function func_defined_by_def at 0x7ff2ce95f950>

print("----"*5)
print(func_defined_by_lambda.__name__) # <lambda>
print(func_defined_by_def.__name__) # func_defined_by_def
```

- 뭐, 그래도 두 함수 모두 type은 같으니까, 문제가 없겠지? 라는 생각이 들기는 합니다. 
- 그리고 매우 간단한 연산 비교를 해보기도 했으나, 둘 간에 유의미한 차이가 있다고 보기는 어렵더군요.

### 그렇다면 무슨 차이가 있는가?

- 하나의 차이는 `lambda` 함수의 경우, `pickle` 모듈을 통해서 serialization하는 것이 불가능합니다.
- 아래와 같이, 간단한 lambda 함수를 dictionary에 넣고, 이 아이를 pickling해보도록 합니다. 생각보다 이렇게 피클링하는 경우들이 종종 있을 수 있는데, 이렇게 실행할 경우 에러가 발생합니다.

```python
import pickle

func_defined_by_lambda = lambda x: x + 10 

dict_to_pickle = {
    "lambda": func_defined_by_lambda, 
}

with open("test.pickle", "wb") as f: 
    pickle.dump(dict_to_pickle, f)
```

- 에러를 보면, `__main__` 부분에서 함수 이름인 `<lambda>`가 정의되어 있지 않다는 이야기죠.

```plaintext
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    pickle.dump(dict_to_pickle, f)
_pickle.PicklingError: Can't pickle <function <lambda> at 0x7fe1de742560>: attribute lookup <lambda> on __main__ failed
```

## wrap-up

- 사실 결론은 하나입니다. "편하다고, lambda 함수를 마구 만들어서 쓰지 말자"라는 것이죠.
- lambda함수는 main 함수에서 어떤 이름으로 관리되는 놈이 아니며, 그냥 매우 임시로 잠깐 만들어지는 함수라고 보는 것이 타당합니다. 
- 만약 일정 주기 이상 유효해야 하고, 여러번 써먹는다면 가능하면 def로 만들어서 처리해주는 것이 훨씬 타당하다는 이야기죠.
