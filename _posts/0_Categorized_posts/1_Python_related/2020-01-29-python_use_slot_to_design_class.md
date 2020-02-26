---
title: python에서 class를 설계할 때, slot을 통해 known attribute로 설정하자.
category: python
tags: python python-basic class OOP 
---

## Define instance attribute by using SLOT.

- python의 모든 class들은 instance attribute를 가지고 있습니다. 즉, 기본적으로 python은 오브젝트의 instance들이 가지는 attribute를 dictionary로 저장하게 됩니다. 따라서, 코드를 동작하면서, 각 instance들에 대해 다음과 같은 코드라도, 새로운 attribute를 넣어줄 수 있죠. 

```python
A.new_attr = 10 
```

- 다만, 이렇게 할 경우, 모든 instance가 각각 값을 업데이트할 수 있는 dictionary를 가지고 있게 됩니다. 그리고, dictionary는 RAM을 낭비하므로, 인스턴스의 수가 증가하게 되면, 메모리 로스는 더 증가하게 되죠. 
- 따라서, runtime시에 새로운 attribute를 추가할 필요가 없는 경우(이러한 경우를 'known attribute' 라고 합니다), 처음부터 "이 클래스의 인스턴스에는 이 attribute만 있다"라는 것을 강제할 수 있습니다. 이렇게 할 경우, instance별로 존재하는 dictionary를 만들지 않음으로써, 상당한 양의 메모리를 줄일 수 있습니다.
이렇게 처리했을 때의 강점 또한 있을 수 있으나, 이렇게 할 경우, class가 아주 많아질 경우 dictionary로 인한 메모리 로스가 발생하게 됩니다. dictionary는 RAM을 낭비하니까요. 

## Do it. 

- 아주 간단합니다. 아래 코드에서 보시는 것처럼 클래스 내에 다음 코드를 작성해주면 됩니다. 즉, 아래 코드는 `name`와 `identifier`만이 사용된다는 이야기겠죠. 

```python
class AAA_with_SLOT():
    __slots__ = ['name', 'identifier']
    def __init__(self):
        pass
``` 

- 그리고 다음과 같이 slot을 사용한 경우와 사용하지 않은 경우를 나누어, 코딩하여 메모리 사용량의 변화를 비교하였습니다. 

```python
import os
import sys
import psutil

class CLASS_WITH_SLOTS():
    __slots__ = ['i', 'name']
    def __init__(self, i, name):
        self.i = i
        self.name = name

class CLASS_WITHOUT_SLOTS():
    def __init__(self, i, name):
        self.i = i
        self.name = name
####################################

N = 900000
GB = 2.**30

for _ in range(0, 3):
    # X 변수에 SLOTS이 있는 클래스 인스턴스를 만든다.
    ## WITHOUT SLOTS
    print("== WITHOUT SLOTS")
    X = [CLASS_WITHOUT_SLOTS(f"id{i}", f"name{i}") for i in range(0, N)]
    print(f"memory Use: {CurrentProcess.memory_info()[0] / GB:9.4f} GB")
    print(f"RAM usage Percent: {psutil.virtual_memory()[2]} %")
    print("==" * 30)
    ####################################
    # X 변수에 SLOTS이 **없는** 클래스 인스턴스를 만든다.
    ## WITH SLOTS
    print("== WITH SLOTS")
    X = [CLASS_WITH_SLOTS(f"id{i}", f"name{i}") for i in range(0, N)]
    print(f"memory Use: {CurrentProcess.memory_info()[0] / GB :9.4f} GB")
    print(f"RAM usage Percent: {psutil.virtual_memory()[2]} %")
    print("==" * 30)
```

- 그 결과를 보면, SLOT을 사용하는 경우에, RAM Usage가 감소하는 것을 알 수 있습니다. 

```
== WITHOUT SLOTS
memory Use:    0.2758 GB
RAM usage Percent: 79.1 %
============================================================
== WITH SLOTS
memory Use:    0.1696 GB
RAM usage Percent: 75.5 %
============================================================
== WITHOUT SLOTS
memory Use:    0.2658 GB
RAM usage Percent: 72.8 %
============================================================
== WITH SLOTS
memory Use:    0.1702 GB
RAM usage Percent: 71.3 %
============================================================
== WITHOUT SLOTS
memory Use:    0.2661 GB
RAM usage Percent: 72.9 %
============================================================
== WITH SLOTS
memory Use:    0.1704 GB
RAM usage Percent: 71.1 %
============================================================
```

## wrap-up

- 사실, runtime에서 클래스의 인스턴스에 새로운 attribute를 집어넣는다면, 그 시점에서 이미 그 소프트웨어 설계는 실패했다고 봐야 할 것 같아요. 따라서, 가능하다면 `__slot__`을 기본적으로 사용하는 것이 보다 효과적인 python 프로그래밍 방법이 아닐까 싶습니다. 
- 그리고, 코드별 memory 사용량의 비교를 정확하게 하는 것은 어려운데(컴퓨터는 이미 다른 것들이 많이 돌아가고 있을 테니까요), 여기서는 너무 당연하게, '같은 변수에 값을 할당하여 비교'하였습니다. 같은 변수에 할당하는 것이 너무 당연한 통제변수임에도, 저는 각각을 다른 변수에 넣어주고, 비교하면서 "왜 별 차이가 없지?"해서 좀 부끄럽네요.


## reference

- <http://book.pythontips.com/en/latest/__slots__magic.html>