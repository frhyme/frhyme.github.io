---
title: multiprocessing을 사용하여 계산을 조금 더 빠르게 하자. 
category: python-libs
tags: python python-libs multiprocessing computation
---

## 계산!!!계산!!!속도!!!빨리!!!

- 요즘 저는 파이썬을 이용해서, 복잡한 계산들을 하고 있습니다. 예를 들면, 
    - Word2vec을 이용하여, 단어를 벡터로 표현한 다음 단어들간의 semantic similarity를 계산하기 
        - 단어가 몇 개 없으면 문제가 없지만, 저처럼 10000개가 넘어가면 아주 힘들어집니다. 
    - 키워드 네트워크에서 betweenness centrality 계산하기 
        - 네트워크에서 한 노드의 betweenness centrality는 계산하기 위해서는 해당 노드를 빼고 나머지 모든 노드들의 pair의 최단거리를 계산해야 합니다. 으 생각만 해도 지옥이군요. 
        - 만약 네트워크에 노드가 10000개 있다면, 대충 5천만 쌍에 대해서 존재하는 모든 shortest path를 계산해야 하죠 허허허허. shortest path 구하는 것도 아주 지랄 맞은거 아시죠? 이거 진짜 미칠것 같아요. 
    - 프로세스 시뮬레이션 돌리기
        - generator를 이용해서 시뮬레이션을 돌리는 걸 만들었습니다. 뭐 다 좋은데, 이건 아시다시피 벡터라이즈로 뭘할수가 없습니다. 즉, 아주 좆같다는 것이져 허허허헛
- 아무튼 간에 이런 일들을 요즘에 진행하다 보니까 계산을 빠르게 돌리는 것들을 신경쓰고 있습니다. 대략 다음의 것들을 찾아봤어요. 
    - `numba`: 간단하게 함수 앞에 `@numba.jit` 데코레이터만 붙여줘도 속도가 매우 빨라집니다. 매우 빠르게 강점을 취득할 수 있지만, 순수 파이썬과 numpy에 대해서만 잘 지원해준다는 점이 매우 아쉬운 점이죠. 
    - `Cuda`: 텐서플로우를 쓸때 cuda만 한 줄 추가해도, 속도가 빨라진다! 라는 이야기를 들은 적이 있습니다. Cuda라는 것은 GPU를 다루는 일종의 api라고 생각하셔도 됩니다. `numba`에서도 cuda와 연결하는 부분들이 있죠. 
        - 다만, GPU를 사용하기 위해서는 해당 라이브러리에서 GPU를 효과적으로 사용하기 위해서 인터페이스 랄지 몇가지를 지원해주는 것이 필요합니다. 텐서플로우에서 cuda를 잘 쓸 수 있는 것은 텐서플로우에서 이미 Cuda를 잘 쓰기 위해서 세팅해둔 것이 많아서죠. 

- 여기서 문제는, 제가 쓰는 라이브러리들이 병렬처리에 대해서는 아직 고려하지 못해서 cuda, numba 모두 연결이 되어 있지 못하다는 것이죠 후. 
- 아무튼 그래서 저는 좀 더 찾아보다가 `multiprocessing`이라는 것을 써보기로 했습니다. 

## multiprocessing

> multiprocessing is a package that supports spawning processes using an API similar to the threading module.

- 파이썬에서는 일반적으로 GIL(Global Interpreter Lock)이 걸려 있기 때문에, 동시에 여러 프로세스가 운영되지 못합니다. 그렇게 보일 수는 있어도, 실제로는 하나만 돌아가고 있는 상황이죠.
- multiprocessing은 동시에 여러 프로세스를 운영할 수 있도록 지원해주는 것이라고 생각하시면 됩니다. 
- 또한, multiprocessing의 경우 여러 프로세스를 조율 및 관리해주는 비용이 들어갑니다. 따라서, 너무 작은 계산에 대해서는 오히려 더 느려질 수도 있어요. 

- 따라서 pure python, numba, numpy, multiprocessing을 조합하여 각각에 따른 결과를 비교해봤습니다. 

### small data

- data가 다음처럼 작을 때는 numpy가 압도적으로 제일 빠릅니다. 그리고 pure pytho도 그렇게 느리지 않아요. 

```python
num_list = [50000 for i in range(0, 4)]
```

```python
from multiprocessing import Pool
import time
import numpy as np 

!pip install numba
import numba
from numba import jit 

num_list = [50000 for i in range(0, 4)]
print("==="*20)
####################################
## pure python
start_time = time.time()
def count_sum(n):
    s = 0
    for i in range(0, n):
        s+=i
    return s

result_list= []

for num in num_list:
    result_list+=[count_sum(num)]

print("pure python")
print(result_list)
print(time.time() - start_time)
print("==="*20)
####################################
####################################
## pure python with multiprocessing
start_time = time.time()
def count_sum(n):
    s = 0
    for i in range(0, n):
        s+=i
    return s

result_list= []

pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
result_list += pool.map(count_sum, num_list)

print("multiprocesing을 사용했을 때 ")
print(result_list)
print(time.time() - start_time)
print("==="*20)
####################################

####################################
## pure python with numba 
start_time = time.time()

@numba.jit
def count_sum(n):
    s = 0
    for i in range(0, n):
        s+=i
    return s

result_list= []

for num in num_list:
    result_list+=[count_sum(num)]

print("pure python + numba")
print(result_list)
print(time.time() - start_time)
print("==="*20)
####################################

####################################
## pure python with numba, multiprocessing
start_time = time.time()

@numba.jit
def count_sum(n):
    s = 0
    for i in range(0, n):
        s+=i
    return s

result_list= []
pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
result_list += pool.map(count_sum, num_list)

print("pure python + numba + multiprocessing ")
print(result_list)
print(time.time() - start_time)
print("==="*20)
####################################

####################################
## numpy 
start_time = time.time()
def count_sum(n):
    return np.arange(0, n).sum()

result_list= []

for num in num_list:
    result_list+=[count_sum(num)]

print("numpy")
print(result_list)
print(time.time() - start_time)
print("==="*20)

####################################
## numpy + numba
start_time = time.time()
@numba.jit
def count_sum(n):
    return np.arange(0, n).sum()

result_list= []

for num in num_list:
    result_list+=[count_sum(num)]

print("numpy + numba")
print(result_list)
print(time.time() - start_time)
print("==="*20)

####################################
## numpy + numba
start_time = time.time()
@numba.jit
def count_sum(n):
    return np.arange(0, n).sum()

result_list= []

pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
result_list += pool.map(count_sum, num_list)

print("numpy + numba + multiprocessing")
print(result_list)
print(time.time() - start_time)
print("==="*20)
####################################
```

- 데이터의 크기가 작을 때는 pure python도 충분히 빠르며, 오히려, 멀티프로세싱을 하거나 딴걸ㄹ 하는 것이 계산을 더 느리게 함. 

```
============================================================
pure python
[1249975000, 1249975000, 1249975000, 1249975000]
0.015837907791137695
============================================================
multiprocesing을 사용했을 때 
[1249975000, 1249975000, 1249975000, 1249975000]
0.07620906829833984
============================================================
pure python + numba
[1249975000, 1249975000, 1249975000, 1249975000]
0.06466841697692871
============================================================
pure python + numba + multiprocessing 
[1249975000, 1249975000, 1249975000, 1249975000]
0.24311566352844238
============================================================
numpy
[1249975000, 1249975000, 1249975000, 1249975000]
0.0017664432525634766
============================================================
numpy + numba
[1249975000, 1249975000, 1249975000, 1249975000]
0.3807497024536133
============================================================
numpy + numba + multiprocessing
[1249975000, 1249975000, 1249975000, 1249975000]
0.3239753246307373
============================================================
```

### big data 

- 물론 빅데이터는 사실 다른 말이지만, 아무튼 사이즈를 크게 해서 보면, numba+ pure python이 numpy보다 빠릅니다. 
- 값이 더 커지면, numpy + numbar가 더 빨라질 수도 있겠다 싶지만, 아직 안해서 봐서 모르겠어요. 

```
============================================================
pure python
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
1.580622673034668
============================================================
multiprocesing을 사용했을 때 
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
1.480203628540039
============================================================
pure python + numba
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
0.06446051597595215
============================================================
pure python + numba + multiprocessing 
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
0.236006498336792
============================================================
numpy
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
0.07915449142456055
============================================================
numpy + numba
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
0.1532001495361328
============================================================
numpy + numba + multiprocessing
[12499997500000, 12499997500000, 12499997500000, 12499997500000]
0.48383617401123047
============================================================
```

### bigger data

- pure python + numba가 제일 좋은걸로...

```
============================================================
pure python
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
14.770026922225952
============================================================
multiprocesing을 사용했을 때 
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
15.772434711456299
============================================================
pure python + numba
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
0.06241726875305176
============================================================
pure python + numba + multiprocessing 
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
0.2525184154510498
============================================================
numpy
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
0.766232967376709
============================================================
numpy + numba
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
0.6098897457122803
============================================================
numpy + numba + multiprocessing
[1249999975000000, 1249999975000000, 1249999975000000, 1249999975000000]
1.4617538452148438
============================================================
```

## wrap-up

- 일단은 지금 내가 분석해야 하는 데이터의 크기가 충분히 큰지(램에서 올리기 버거워하는 것인지 등)을 명확하게 본 다음에 진행하는 것이 좋을 것 같아요. 
- 그냥 퓨어하게 만든 python이라고 앞에 `@numba.jit`만 붙여도 충분히 큰 규모의 데이터에서는 numpy만큼 빠르게 작동하기도 합니다. 
- 뭐 아무튼, 데이터의 크기에 따라서 계산을 최적화하는 방법이 다르니까, 잘 판단해서 하는게 좋을 것 같아요(무책임) 하하하하핫


## reference 

- <https://docs.python.org/3.6/library/multiprocessing.html>