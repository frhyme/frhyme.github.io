---
title: python - static type checking - mypy
category: python
tags: python static-type type-checking mypy
---

## Background) Static-type and Dynamic-typed checking

- python이전에 비교적 전통적인 프로그래밍 언어에 속하는 c, c++, java 등의 언어를 사용해보신 분들은 다음과 같은 형태로 코드를 작성하는 것이 익숙했습니다. 

```c
int a = 10
```

- 하지만, 우리 위대한 python의 경우는 다음과 같죠. 아주 짧고 간편해집니다.

```python
a = 10
a = "string"
```

- 앞에 해당 variable의 type이 무엇인지 알려주지 않아도 된다는 것. 이 것이 사소한 차이일 수도 있지만, 이 간편함이 python이 지금처럼 많은 대중들에게 관심을 끌게 된 원인 중 하나라고 저는 생각해요. 하지만, 위처럼 코드가 짧다면 문제가 되지 않지만, 코드가 길어지고 다른 사람들과 코드가 공유되기 시작하면 점차 문제가 생겨 납니다.

### Static-type checking

- 아무튼, C와 같이, 미리 각 '변수'와 변수들을 처리하는 '함수'들에 대해서 코드 작성시에 type이 정의되는 것을 요구하는 언어들을 정적 타입 언어라고 합니다. 그리고 이를 runtime(코드 실행) 이전인 컴파일 타임에서 type을 체크하고 넘어가게 되죠. 이를 통해, 조금은 빠르게 해당 코드에서 발생할 수 있는 문제점들을 파악할 수 있습니다. 
- 물론, haskell의 경우는 예외적으로 type을 미리 선언하지 않더라도, 어느 정도는 "타입추론"을 할 수 있다고 합니다. 이는, 해당 "(타입이 알려지지 않은) 변수"가 "어떤 타입의 변수와 관련되어 있는지", 그리고 "어떤 타입의 함수들과 연결되어 있는지"등을 통해 어느 정도는 파악해낼 수 있다고 하는데, 어떤 의미에서, 이는 dynamic-type chekcing과 유사하다고 느껴지기도 해요(다만, 이 부분은 제 정보가 충분하지 않으므로 넘어가겠습니다).
- 여기에 속하는 언어들로, C, C++, Go, Haskell, Java, Kotlin, Rust, Scala 등이 있습니다. 

### Dynamic-type checking

- 반대로 python처럼, 각 변수들의 type을 정의하지 않고도 코드를 작성할 수 있는 경우를 동적타입언어라고 합니다. 즉, 미리 정의되어 있지 않기 때문에 "돌려봐야 문제가 있는지 알 수 있다"라는 말입니다. 만약, 1번 돌리는데 10시간이 걸리는 코드가 있다면, 이를 dynamic-type으로 코딩하여, 5시간이 지난 다음에야 알 수 있다면, 좀 무섭겠죠? 
- 여기에 속하는 언어들로는 python, Ruby, javascript, lisp 등이 있습니다.

### Hybrid type checking

- python은 dynamic-type checking 언어로 시작되었습니다만, 오늘 말할것과 같이, 점점 type을 미리 지정하면서 코딩하는 방향으로 나아가고 있습니다. 프로젝트의 규모가 커져가면서 유지보수 문제로 인해서 그럴 가능성이 높다, 라고 저는 생각되어요. 보통, dynamic-type 에서 static-type으로 가는 경우는 잘 없습니다.
- 존재하는 모든 코드에 대해서 static-type의 형태로 코딩되어야 함을 강제하는 것은 좀 어려운 일이죠. 처음부터 그렇게 했으면 모를까. 그래서, 할 수 있는 부분만 static-type checking을 통해 불확실성을 줄이자, 라는 것이 이러한 섞여 있는 type checking인 셈이죠. 

### type conversion

- implicit type converstion(프로그래머 몰래 알아서 형을 변경하는 것)과 explict type conversion(프로그래머가 "바꿔!"라고 하는 것)으로 구분됩니다. 디버깅시에 발생하는 문제를 없애려면, 가능한 explicit한 것이 더 좋기는 하죠. 


## Back to Python: Type hinting

- 아무튼, python으로 다시 돌아와서 보겠습니다. 앞서 말한 것처럼 python은 동적 타입언어입니다. 아래처럼 타입 지정하지 않고 아무 값이나 막 집어넣어도 되죠. 

```python
var_int = 10
var_str = "33"
var_float = 1.333
```

- 하지만, 이렇게 하지 않고 type을 알려주면서 코딩을 하려고 합니다. 다만, type을 알려줄 뿐, type checking을 하지는 않습니다. 즉, 그냥 "주석"다는 것처럼 각 변수와 함수에 대해서 type을 적어주는 것이죠. 해당 내용은 [PEP-484](https://www.python.org/dev/peps/pep-0484/)에 작성되어 있으며, 간단한 형식은 다음과 같습니다. `:`을 사용해서 뒤에 type을 적어주면 됩니다. python native type이라고 할 수 있는 거의 대부분의 type들, `bool/str/int/float/list/dict/tuple`에 대해서 지정해줄 수 있습니다. 

```python
# bool/str/int/float/list/dict/tuple
def greeting(param1: str, param2: int) -> str:
    # explicit type conversion for parma2
    return "Hi "+ param1+str(param2) 
########################################
var1: str = "aaa"
var2: int = 1000
var3: float = 14.5
########################################
print(
    greeting(var1, var2)
)
print(
    greeting(var1, var3)
)
```

- 실행 결과는 다음과 같습니다. python은 type-hinting, 즉 type이 무엇인지 적기는 하지만, type-checking을 하지는 않아요. 따라서, 위의 함수에서 `param2`에서 원래는, `int`들어야 하는데, `float`이 들어와도, 문제가 없이 실행됩니다.

```
Hi aaa1000
Hi aaa14.5
```

### mypy: type-checking 

- 하지만, 우리는 type-checking을 하고 프로그램을 돌리고 싶습니다. 이를 위해서는 [`mypy`](https://mypy.readthedocs.io/en/stable/getting_started.html)라는 다른 라이브러리를 설치해줘야 하죠. 
- 일단 `mypy`를 설치합니다.

```
pip install mypy
```

- 그리고, 아래와 같이 해당 파일에 대해서 커맨드라인에서 돌려보면 됩니다.
```
mypy test.py
```

- 간단하지만, 오류를 잡아줬죠.

```
test.py:29: error: Argument 2 to "greeting" has incompatible type "float"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## wrap-up

- 사실 처음 프로그래밍을 배울 때는 dynamic-type이 편하지만, 시간이 갈수록 어느 정도는 static으로 처리하기를 바랄 때가 있습니다. 스스로를 믿지 못하기 때문에, 나의 실수를 미리 막아줄 수 있기를 바라는 마음도 있고요. 
- static type으로 처리할 때의 강점이라면, 아니, 최소한 annotation으로 변수와 함수의 타입을 정의하면서 코딩할 때의 강점이라면, 그 함수의 파이프라인이 어떤 형태로 되는지, 대략은 구상할 수 있다는 것이죠. 예를 들어, 다음 두 함수를 본다면, type-hinting을 할때 "코드의 가독성"이 상당히 올라감을 알 수 있습니다(물론 변수명을 사용해서 type hinting을 할 수도 있긴 합니다만)

```python
def func_without_typehinting(a, b, c, d):
    return [ str(a)+str(b)+x+c for x in d]
def func_with_typehinting(a:int, b:float, c:str, d:list):
    return [ str(a)+str(b)+x+c for x in d]
```

- 다시 말하지만, 저렇게 써준다고 해서, python을 실행시킬 때 알아서 type을 잡아주는 것은 아닙니다. 그래도, "제가 직접 static-type checking을 할 수 있다"라는 것이 크고, 이로 인해 코드의 버그를 상당히 줄일 수 있겠죠. 
- 물론, 다시 생각해본다면, python으로 코딩하는 경우는 대부분 데이터 분석을 목적으로 할때 이고, 이 때 주로 사용하는 `numpy`, `pandas`등의 경우는 이미 dtype들이 지정된 상태로 진행되죠. 이렇게 생각하니, 또 굳이, type을 선언해주는 게 필요한가 라는 생각이 들기도 하네요.




## reference

- <https://ahnheejong.name/articles/types-basic-concepts/>
- <https://mypy.readthedocs.io/en/stable/getting_started.html>
- <https://realpython.com/python-type-checking/#static-type-checking>