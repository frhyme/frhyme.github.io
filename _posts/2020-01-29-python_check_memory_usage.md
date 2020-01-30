---
title: psutil을 사용해서 python의 CPU, RAM의 사용량을 확인하자.
category: python
tags: python python-basic performance-checking psutil python-libs
---

## intro. 

- 코딩을 어느 정도 하다보면, "코드 자체를 생산하는 것"은 꽤 쉬운 일이라는 생각이 들때가 있습니다. 그 즈음에 드는 생각은 "어떻게 해야 더 효율적이고 빠른 코드를 만들 수 있을까?"죠. 
- 원론적으로 이를 해결하기 위해서는, 프로그래밍 기본에 대한 공부들을 하는 것이 좋습니다. 인간컴파일러가 되어서, 어떻게 돌아가는지를 이해한다면 좋겠지만, 보통 그런 경우는 없고, '일단 이 코드가 느린지 빠른지'를 먼저 체크하는 것이 필요하죠. 
- 이를 위해서는 기본적인 성능을 비교하는 것이 필요합니다. 그리고 그 성능이라는 것은 보통 '시간'과 'RAM 사용량'으로 결정되죠.
- 이 글에서는, 상대적으로 사용하기 쉬운 시간 비교는 무시하고, RAM 사용량을 체크해보려고 합니다. 같은 데이터를 담더라도, 어떤 자료 구조를 선택하느냐에 따라서, RAM 사용량이 다른 경우들이 존재하니까요. 

## Check RAM Usage. 

### sys.getsizeof

- 간단하게, 각 변수에 할당된 데이터의 크기가 어느 정도인지를 체크하기 위해서는 `sys.getsizeof`를 사용할 수 있습니다. 하지만, object 안에 object가 또 있는 경우, 특히 string으로 구성된 list에 대해서는 정확하게 비교해주지 못합니다. 즉, 그냥 `list of pointer`와 유사하게, shallow size를 출력해준다고 봐도 되겠네요. 

```python
###################################
# sys.getsizeof()
# Return the size of an object in bytes.
# 이를 사용하면, 간단하게 크기를 비교할 수 있다.
import sys
N = 1000
print("== sys.getsizeof")
# 그러나, 아래와 같이 string이 container의 내부 요소로 포함된 경우에는 정확한 크기를 측정하지 못한다.
# 이는 python에서 string은 object이며, 위치 정보(가령 pointer)만 저장하고 전체 크기까지 함께 저장하고 있지 않기 때문이다
# 만약 정확한 크기를 파악하고 싶다면, 내부 요소의 타입까지 고려하여 계산해야 한다.
assert sys.getsizeof(['aaaa', 1])==sys.getsizeof(['aaaa', 'asdfsdafdsfasf'])

test_lst_int = [i for i in range(0, N)]
test_lst_tuple = [(f"k{i}", i) for i in range(0, N)]
test_dict = {f"k{i}":i for i in range(0, N)}
# 내부 요소가 tuple로 되어 있는 경우인 test_lst_int 와 test_lst_tuple의 크기가 같다.
print(f"sys.getsizeof(test_lst): {sys.getsizeof(test_lst_int)}")
print(f"sys.getsizeof(test_lst): {sys.getsizeof(test_lst_tuple)}")
print(f"sys.getsizeof(test_dict): {sys.getsizeof(test_dict)}")
```

```
== sys.getsizeof
sys.getsizeof(test_lst): 9024
sys.getsizeof(test_lst): 9024
sys.getsizeof(test_dict): 36968
```

### Check RAM usage. 

- 이제 Ram의 사용량을 비교해봅시다. 기본적으로는 `pstuil`이라는 라이브러리를 사용하며, 현재 프로세스의 메모리 사용량을 체크하는 경우와, 제너럴한 메모리 사용량을 체크하는 경우로 구분되며, 사실상 큰 차이는 없습니다(성능을 비교할 때 다른 짓을 거의 하지 않는다는 전제 하에서)
- 코드 적으로 어려운 부분은 없으니, 자세한 설명은 제외하겠습니다.

```python
###################################
# memory check.
# 1) 그냥 현재 memory usage 정보를 그대로 가져오는 경우
# 2) 현재 process id를 통해 해당 프로세스의 memory usage를 정확하게 비교하는 경우
import psutil
import os

print("=="*20)
print("== memory usage check")

for exec_num in range(0, 2):
    # BEFORE code
    print(f"== {exec_num:2d} exec")
    # general RAM usage
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

    X = [i for i in range(0, 9000000)]
    # AFTER  code
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    del X
    print("--"*30)
```

- 결과는 다음과 같습니다.

```
========================================
== memory usage check
==  0 exec
BEFORE CODE: memory_usage_percent: 68.6%
BEFORE CODE: Current memory KB   :    10.156 KB
AFTER  CODE: memory_usage_percent: 74.9%
AFTER  CODE: Current memory KB   :   317.652 KB
------------------------------------------------------------
==  1 exec
BEFORE CODE: memory_usage_percent: 68.5%
BEFORE CODE: Current memory KB   :    14.332 KB
AFTER  CODE: memory_usage_percent: 75.0%
AFTER  CODE: Current memory KB   :   316.656 KB
------------------------------------------------------------
```

## wrap-up

- python으로 생성한 코드에 대해서 시간 뿐만 아니라 RAM의 사용량을 비교하기 위하여 `psutils`를 사용하여 메모리 사용량을 비교하는, 간단한 방법을 설명하였습니다.


## reference

- <https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python>