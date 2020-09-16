---
title: python에서 Generator의 길이는 어떻게 계산하는게 좋을까요? 
category: python
tags: python python-basic len psutil sys
---

## Why need generator?

- 다른 사람이 잘 만들어둔 python library를 쓰다보면, 가끔 분명히 컨테이너인 것 같은데 `[]`로 접근되지 않는 경우가 있습니다. 보통 에러 코드는 다음과 같죠. 즉, 'generator'는 `subscriptable`하지 않다라는 이야기입니다. 그리고 이는 다시, '해당 객체에 `__get__`메소드가 구현되어 있지 않아서, `[]`를 통해 접근할 수 없다는 이야기입니다.

```plaintext
TypeError: 'generator' object is not subscriptable
```

- 그리고 보통 우리는 이럴 때, 아주 쉽게, `list()`등을 붙여서 리스트로 가져오곤 합니다. 그러나, `list`로 변환하면 아주 간편해지는 것은 모두 알고 있습니다. 그러함에도 **generator로 굳이** 만들어둔 것에는 합당한 이유가 있겠죠? 
- 다음을 보면 그 이유가 명확합니다. generator를 list로 만들면, 다음과 같이 저장해야 하는 용량이 급증하고, 이는 RAM에 과부하가 걸린다는 것을 의미하죠. 

```python
import sys

N = 10**6
gen_A = (i for i in range(0, N))
lst_A = [i for i in range(0, N)]
print(f"gen_A: {sys.getsizeof(gen_A)}")
print(f"lst_A: {sys.getsizeof(lst_A)}")
```

```plaintext
gen_A: 88
lst_A: 8697464
```

## Length of Generator?

- 하지만, 어쩔 수 없이, Generator의 길이를 체크해야 할 때가 있을 수 있죠. 그때는 두가지 방법이 있을 수 있습니다.
  1. generator를 list로 변형하고 `len()`함수를 사용해서 체크
  2. generator의 요소들을 하나씩 읽어들이면서, 1씩 증가하면서 체크. 
- 둘다 적절해보입니다만, **1)번의 경우 당연하지만, 리스트로 만들어야 하므로, 메모리에 문제가 발생할 수 있습니다**. 그리고, 비교해봤을 때, 그렇게 압도적으로 빠르지도 않아요. 그리고, 정확하게 RAM의 사용량을 체크하려면 다른 방법을 써야 하지만, 귀찮아서 그냥 코드 앞뒤를 비교하는 식으로 처리했습니다. 즉, 전체를 다 램에 올리는 것보다는 하나씩 처리하는 것이 훨씬 효율적이라는 이야기죠.

```plaintext
== METHOD 1: list materialization and use len
Before code: 81.6
After  code: 83.7
execution time: 1.442821979522705
========================================
== METHOD 2: loop with generator and cout
Before code: 80.3
After  code: 80.4
execution time: 1.683372974395752
== complete
```

- 코드는 다음과 같습니다. `psutil`을 사용해서 메모리의 사용량을 체크했으며, 앞에서 언급한 바와 같이, 해당 코드의 앞 뒤로 메모리사용량의 변화만을 체크하였습니다. 대략적인 변화만을 알기 위함이죠.

```python
"""
just wondering 
which one is faster
1) list materialization and use len
2) loop with generator and cout
"""

import time
import psutil
import sys

def print_virtual_memory_usage():
    # 현재의 메모시 사용량을 %로 출력하는 함수
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    return memory_usage_percent
    #print(f"memory_usage_percent: {memory_usage_percent}%")

########################################
N = 10**7

#######################################
# 1) list materialization and use len
print("== METHOD 1: list materialization and use len")
simple_gen = (i for i in range(0, N))
start_time = time.time()
print(f"Before code: {print_virtual_memory_usage()}")
simple_lst = list(simple_gen)
l1 = len(simple_lst)
print(f"After  code: {print_virtual_memory_usage()}")
del simple_lst
print(f"execution time: {time.time() - start_time}")
print("=="*20)

#######################################
# 2) loop with generator and count
print("== METHOD 2: loop with generator and cout")
simple_gen = (i for i in range(0, N))
start_time = time.time()
l2 = 0
print(f"Before code: {print_virtual_memory_usage()}")
for x in (i for i in range(0, N)):
    l2+=1
print(f"After  code: {print_virtual_memory_usage()}")
print(f"execution time: {time.time() - start_time}")
##########################################
assert l1==l2

print("== complete")
```

## built-in function len

- 또한, python에서 기본적으로 제공하는 built-in 함수인 `len`이 어떻게 구성되어 있는지도 체크해봤습니다. 
- built-in function은 [이 링크](https://github.com/python/cpython/blob/master/Python/bltinmodule.c)에 존재하며, `python -> cpython -> bitinmodule.c`에 존재합니다. 또 그 긴 코드 파일 내에서 `builtin_len`라는 이름으로 존재합니다. 
- 그리고, 해당 코드는 `PyObject`, 즉, C로 되어 있습니다. 누가 "왜 len이 그렇게 빠르냐?, native python으로는 그 속도를 낼 수 없냐?" 라고 묻는다면 없습니다. C로 되어 있으니까요 걔는. 

## wrap-up

- 결국, 이 내용은 다시, **"무분별한 `list`형태로의 변환을 지양하자"** 로 귀결되는 내용입니다. 편하다고, 그냥 list로 바꿀 경우 메모리에 문제가 생겨서 컴퓨터가 뻗을 수도 있는 것이죠. 
- 물론, 이후에 numba가 더 발전한다면, 가능할지도 모르는 일이기는 하죠.

## reference 

- [Stackoverflow - what does it mean if a python object is subscritable](https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not)
