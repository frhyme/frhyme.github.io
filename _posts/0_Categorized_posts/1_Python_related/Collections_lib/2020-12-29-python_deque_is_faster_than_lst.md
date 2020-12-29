---
title: python - collections - deque가 list보다 항상 빠른가?
category: python-lib
tags: python python-lib collections deque list queue stack
---

## python - collections - deque나 list보다 빠를까?

- 결론부터 말하자면, **Queue로 쓰이는 경우에만** `deque`가 `list`보다 빠릅니다. 일단 deque는 list처럼 `[i]`와 같이 index에 따른 접근이 불가하기 때문에, 중간에 있는 값에 접근하려면 list를 사용하는 것이 훨씬 효율적이죠. Stack으로 쓰이는 경우에는 별 차이 없습니다.
- `Queue`는 FirstInFirstOut이라고 하는, 우리가 흔히 서는 '대기줄'을 말하죠. 먼저 선 사람이 먼저 나가게 됩니다.
- 그리고 `deque`는 앞쪽으로 나올 수도 있고 들어갈 수도 있고, 뒤쪽으로 들어갈 수도 있고 나올 수도 있는 자료구조입니다. 따라서, 다음의 4가지 method를 가지고 있죠. 
  - `append(x)`: 오른쪽으로 새로운 원소 집어넣기
  - `appendleft(x)`: 왼쪽으로 새로운 원소 집어넣기
  - `pop(x)`: 오른쪽에서 원소 빼기
  - `popleft(x)`: 왼쪽에서 원소 빼기

## Stack - deque is not efficient than list

- 우선 stack으로 사용해보겠습니다. stack은 LastInFirstOut이라고 하는, "마지막에 들어온 사람이 먼저 나가는 자료 구조"를 말하죠. 접시를 쌓아두면 가장 나중에 쌓아놓은 접시를 먼저 빼야 하죠. 그런걸 말하는 겁니다.
- 아무튼, 간단하게 **deque, list로 stack을 만들어보고 연산 시간을 비교해보았습니다만, 별 차이가 없죠**.
- 사용한 method는 다음과 같습니다.
  - `list.append()`, `list.pop()`
  - `deque.append()`, `deque.pop()`

```python
from collections import deque
import time

N = 10000  # 초기에_넣어둘_원소_개수
TIMES = 100  # 실험 횟수
M = 1000  # M번 pop, M번 append(push)

# 일단 두 자료구조에 N개의 원소를 집어넣어둡니다.
list_stack = list([i for i in range(0, N)])
deque_stack = deque([i for i in range(0, N)])

########################################
# List as Stack
lst_time_lst = []
for _ in range(0, TIMES):
    start_time = time.time()
    # M개의 원소를 append, pop
    for i in range(0, M):
        list_stack.append(i)
        list_stack.pop()
    # 경과 시간을 계산해서 넣어줍니다.
    time_duration = time.time() - start_time
    lst_time_lst.append(time_duration)

########################################
# Deque as Stack
deque_time_lst = []
for _ in range(0, TIMES):
    start_time = time.time()
    # M개의 원소를 append, pop
    for i in range(0, M):
        deque_stack.append(i)
        deque_stack.pop()
    # 경과 시간을 계산해서 넣어줍니다.
    time_duration = time.time() - start_time
    deque_time_lst.append(time_duration)

# RESULT
# 결과를 보면, deque와 list간에 거의 차이가 없습니다.
print(f"List__time_sum: {sum(lst_time_lst)}")
print(f"Deque_time_sum: {sum(deque_time_lst)}")
# List__time_sum: 0.011439323425292969
# Deque_time_sum: 0.012769937515258789
```

## Queue - deque is much efficient than list

- 이번에는 Queue로 사용해보겠습니다. Queue는 FirstInFirstOut이라는 전략을 취하죠. 먼저 들어간 놈이 먼저 나옵니다.
- 이를 위해서 다음 메소드들을 사용합니다.
  - `list.append()`: List의 오른쪽에 원소를 넣어줄 때
  - `list.pop(0)`: List의 왼쪽에서 원소를 뺄 때
  - `deque.append()`: deque의 오른쪽에 원소를 넣어줄 때
  - `deque.popleft()`: deque의 왼쪽에서 원소를 뺄 때
- 결론부터 말하면, 이 때는 `deque`가 훨씬 빠릅니다. `list.pop(0)`를 사용하게 되면 list의 메모리를 재할당해야 하는 경우들이 생겨서, 연산시간이 훨씬 오래 걸릴 수 있죠.

```python
from collections import deque
import time

N = 1000  # 초기에_넣어둘_원소_개수
TIMES = 10  # 실험 횟수
M = 100  # M번 pop, M번 append(push)

# 일단 두 자료구조에 N개의 원소를 집어넣어둡니다.
list_queue = list([i for i in range(0, N)])
deque_queue = deque([i for i in range(0, N)])

########################################
# List as Queue
lst_time_lst = []
for _ in range(0, TIMES):
    start_time = time.time()
    # M개의 원소를 append, pop
    for i in range(0, M):
        list_queue.append(i)
        # 앞에서 빼야 하므로 `.pop()`를 실행합니다.
        list_stack.pop(0)
    # 경과 시간을 계산해서 넣어줍니다.
    time_duration = time.time() - start_time
    lst_time_lst.append(time_duration)

########################################
# Deque as Queue
deque_time_lst = []
for _ in range(0, TIMES):
    start_time = time.time()
    # M개의 원소를 append, popleft
    for i in range(0, M):
        deque_stack.append(i)
        deque_stack.popleft()
    # 경과 시간을 계산해서 넣어줍니다.
    time_duration = time.time() - start_time
    deque_time_lst.append(time_duration)

# RESULT
# 결과를 보면, deque와 list간에 거의 차이가 없습니다.
print(f"List__time_sum: {sum(lst_time_lst)}")
print(f"Deque_time_sum: {sum(deque_time_lst)}")
# List__time_sum: 0.026302099227905273
# Deque_time_sum: 0.00012063980102539062
```

## Wrap-up

- Queue로 사용해야 할 때는 `deque`를 사용하고, 그렇지 않을 때는 그냥 list를 써도 아무 문제없다 하하.
