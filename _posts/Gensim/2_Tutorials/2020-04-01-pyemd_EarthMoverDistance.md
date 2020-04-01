---
title: Earth Mover Distance(EMD) and pyemd
category: python-libs
tags: python python-libs gensim pyemd 
---

## Earth Mover Distance(EMD)

- Earth Mover Distance(EMD)는 "확률 분포 A를 확률 분포 B로 변환할때 필요한 일의 양"을 의미합니다. 여기서는 확률 분포라고 general하게 말하였지만, 간단하게는 그냥 "하나의 histrogram에서 다른 histogram으로 변환할때 필요한 일의 양"이라고 생각하셔도 무방합니다. 
- 아래 그림을 보면 더 명확할 수 있는데, 원래의 분포에서 새로운 분포로 변경하기 위해서는 어느 정도의 움직임이 필요한가? 를 나타내는 것이죠. 그리고, 여기서 "어디에서 어디로 움직이느냐"에 따라서 그 변환의 비용이 달라질 수 있습니다. 이는 보통 `distance_matrix`를 사용하여, 표현하죠. 

![Earth Mover Distance img](https://d3i71xaburhd42.cloudfront.net/39fabfa2da1f78a3be5f45dc3e54233910a7ea01/2-Figure1-1.png)

- 따라서, 결국 이는 일종의 "최적화"문제로 변환됩니다. `distance_matrix`에 표현된대로, "변환할때 필요한 비용"이 다르다면, 어떻게 변환하는 것이 가장 최소의 비용을 찾는것인가? 라는 최적화 문제로 변환되는 것이죠. 
- 즉, "그게 최소화되었을때, 변환비용"을 **Earth Mover Distance(EMD)**이라고 합니다.

## `pyemd` and practice.

- 최적화 문제로 변환하는 것은 크게 어렵지 않기는 하지만, 귀찮죠. 그래서 [pypi - pyemd](https://pypi.org/project/pyemd/)에 이미 구현되어 있습니다. 
- 일단 설치를 하구요. 

```
pip install pyemd
```

### emd()

- `pyemd.emd`는 그냥 EMD값만을 구하는 것을 말합니다. 
- 그리고 이때, Argument들은 다음과 같죠. 
    - `first_histogram`: 기본 자료형이 np.float64인 길이 `N`의 `np.array`
    - `second_histogram`: 기본 자료형이 np.float64인 길이 `N`의 `np.array`
    - `distance_matrix`: 2-dimensional np.array이며, 크기는 `N` by `N`. 
        - `d_ij`는 `first_histogram`의 i_th bin이 `second_histogram`의 j_th bin으로 변활 될때 필요한 비용, 이라고 생각하면 됩니다. 크면 클수록 그 변환이 어려워지겠죠. 
    - `extra_mass_penalty`: 각 histogram의 sample의 수가 동일하지 않을 경우, 임의로 그 값을 하나더 추가해줘야 하죠. 즉 이럴 때, 그 penalty를 어떻게 할 것인가?를 말합니다. default value는 -1.0입니다.
- 계산은 다음처럼 하면 되죠. 단 이 때, `hist1`과 `hist2`의 길이는 항상 같아야 합니다. 같지 않으면, 같게 만들어준 다음 처리하면 되겠죠.

```python
import pyemd
import numpy as np 

hist1 = np.array([2.0, 1.0])
hist2 = np.array([1.0, 2.0])

# distance_matrix: d_ij 는 elemement_i => element_j로 바꿀때 필요한 work의 양
distance_matrix = np.array([
    [0.0, 1.0], [1.0, 0.0]
])

EMD_value = pyemd.emd(
    first_histogram = hist1, 
    second_histogram = hist2, 
    distance_matrix=distance_matrix, 
    extra_mass_penalty=10.0)

print(f"EMD value: {EMD_value}")
```

- EMD는 `hist1`의 첫번째 bin의 값 1.0을 `hist2`의 두번째 bind으로 옮겨줄 때 필요한 비용을 말합니다. 이 때 필요한 비용은 `distance_amtrix[0][1]`에서 확인할 수 있고, 결론적으로 그 값은 1.0이 나오네요(사실은 0.9지만 대충 넘어갑니다). 

```
EMD value: 0.999999
```


### emd_with_flow()

- `pyemd.emd_with_flow`는 단지 emd 값 뿐만 아니라, 어떤 bin의 어느 정도가 어떤 bin으로 옮겨갔는지도 함께 보여줍니다.
- 즉, 변환 과정에서의 minimum-cost-flow를 함께 반환해주는 것이죠.

```python
print("=="*20)
# EMD_value 와 flow_matrix를 같이 뽑습니다.
EMD_value, flow_matrix = pyemd.emd_with_flow(hist1, hist2, distance_matrix)
print(f"EMD value: {EMD_value}")
print("--"*20)
for i, row in enumerate(flow_matrix):
    for j, flow_or_not in enumerate(row):
        if flow_or_not > 0.0:
            print(f"== {i} in first_hist ==> {j} in second_hist, :: its distance - {distance_matrix[i][j]}")
print("=="*20)
```

```
========================================
EMD value: 0.999999
----------------------------------------
== 0 in first_hist ==> 0 in second_hist, :: its distance - 0.0
== 0 in first_hist ==> 1 in second_hist, :: its distance - 1.0
== 1 in first_hist ==> 1 in second_hist, :: its distance - 0.0
========================================
```


### emd_samples()

- `pyemd.emd_samples()`의 경우는 histogram을 argument로 받아들이는 것이 아니라, "아직 histogram화 되어 있지 않은, iterable한 아이"를 그냥 가져옵니다. 내부에서, 알아서 적합한 크기로 bin을 만들어주고, distance_matrix를 만들고, 해서 처리해주죠.

```python
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5, 5]

EMD_values = pyemd.emd_samples(
    first_array = lst1, 
    second_array = lst2, 
    extra_mass_penalty=-1.0,
    distance='euclidean', 
    normalized=True,
    bins='auto',
    range=None

)
print(f"== EMD_values: {EMD_values}")
```

## wrap-up

- 머신러닝을 공부하다보면, 결국은 최적화 문제와 연결되어 있는 것을 발견하게 됩니다. 사실, 처음부터 그렇죠. 뉴럴 넷 문제들도 결국은 주어진 환경 속에서 constraint를 만족하는 최적의 weight를 찾는 문제이니까요. 
- 아무튼, 원래는 Word_Mover_Distance를 공부하다가 거기서 사용된 개념을 정리하다보니 여기까지 넘어왔습니다. 
- 다만, Word_Mover_Distance에서는 bin을 만들 수 없으므로, 그냥 minimum-cost-flow 문제로 풀어버린다고, 생각하면 되는 것이겠죠.


## reference

- [towards data science - earth movers distance](https://towardsdatascience.com/earth-movers-distance-68fff0363ef2)
- [jeremykun.com - earthmover distance](https://jeremykun.com/2018/03/05/earthmover-distance/)
- [wikipedia - Earth Mover Distance](https://en.wikipedia.org/wiki/Earth_mover%27s_distance)
- [pypi - pyemd](https://pypi.org/project/pyemd/)