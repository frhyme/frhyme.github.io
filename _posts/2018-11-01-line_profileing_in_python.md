---
title: line profiler를 사용하여 파이썬의 각 라인이 어떻게 돌아가는지를 알아보자. 
category: python-libs
tags: python line_profiler python-libs 
---

## intro

- 요즘 저는 시뮬레이션을 돌리는 작업을 좀 하고 있는데, 속도가 너무 느려서 걱정입니다. 여러 번 돌려야 하는데, 속도가 너무 느리다보니, 좀 빠르게 진행하지 못하고 있어요. 
- 아무튼 그 과정중에, 현재 코드가 연산이 빠른지 어떤지를 파악하려면 어떻게 해야하나 찾아보다가, [line_profiler](https://github.com/rkern/line_profiler)라는 놈을 발견했습니다. 

## line_profiler

> line_profiler is a module for doing line-by-line profiling of functions. 

- 함수에 대해서 라인별로 얼마나 시간이 소요되는지를 정리해주는 함수입니다. jupyter notebook에서는 magic-command 로 쓸 수도 있구요 
- 긴 말하지 않고 바로 써보겠습니다. 

## do it

- 일단 설치를 합니다. 
- `!pip install line_profiler`는처음 라인은 jupyter notebook에서 필요한 라이브러리인 line_profiler를 설치하는 것이고요
- `%load_ext line_profiler`는 설치한 다음, 익스텐션을 로드하는 것입니다. 
    - 이걸 해주지 않으면, 테스트하고 싶은 함수마다 앞에 데코레이터를 붙여줘야 합니다. 귀찮으므로, 그냥 이걸 해주는게 좋습니다. 

```bash 
!pip install line_profiler 
%load_ext line_profiler
```

- 다음처럼, 테스트해줄 간단한 함수를 만듭니다. 

```python
def function_for_line_profiling(n=1000):
    s = 0 
    for i in range(0, n):
        s+=i 
        s+=i**2
    return s
```

- 그리고 아래를 실행합니다. 
    - `%lprun`: jupyter notebook에서 `line_profiler`를 실행하기 위한 매직커맨드 
    - `-f`: 함수 이름 argument 
    - 그리고 함수 이름을 넣고, 함수를 실행해봅니다. 

```python
%lprun -f function_for_line_profiling function_for_line_profiling()
```

- 결과는 다음처럼 나옵니다. 
    - 어떤 라인에서 얼마나 오래 걸리는지 정리해줍니다. 
    - 이걸, 보고 어떤 라인이 바틀넥인지를 파악하고 처리할 수 있겠죠. 

```
Timer unit: 1e-06 s

Total time: 0.001703 s
File: <ipython-input-51-4d5ac3345113>
Function: function_for_line_profiling at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def function_for_line_profiling(n):
     2         1          2.0      2.0      0.1      s = 0 
     3      1001        309.0      0.3     18.1      for i in range(0, n):
     4      1000        363.0      0.4     21.3          s+=i 
     5      1000       1028.0      1.0     60.4          s+=i**2
     6         1          1.0      1.0      0.1      return s
```

- 또한, 사소한 것일지 모르지만, 아래에서처럼 연산을 두 줄로 나누어서 하도록 하지 않고, 한 줄로 합쳤더니, 연산이 40%정도 빨라졌습니다. 
    - 아마, CPU에 연산할 내용을 한번에 넘겨서 그런것이 아닐까 싶은데, 아무튼 중요한 것 같아요. 

```python
def function_for_line_profiling(n):
    s = 0 
    for i in range(0, n):
        s+=i + i**2
    return s

N = 1000
%lprun -f function_for_line_profiling function_for_line_profiling(N)
```

```
Timer unit: 1e-06 s

Total time: 0.001183 s
File: <ipython-input-56-290e6ba3e5ea>
Function: function_for_line_profiling at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def function_for_line_profiling(n):
     2         1          2.0      2.0      0.2      s = 0 
     3      1001        502.0      0.5     42.4      for i in range(0, n):
     4      1000        678.0      0.7     57.3          s+=i + i**2
     5         1          1.0      1.0      0.1      return s
```

## wrap-up

- 종종 `line_profiler`로 테스트를 해보도록 합시다 하하핫.



## reference

- <https://mortada.net/easily-profile-python-code-in-jupyter.html>