---
title: float list로부터 mode 찾기 
category: python-lib
tags: python mode counter math statistics
---

## mode를 찾읍시다. 

- 대상 데이터의 분포가 normal, exp, poisson 등 의 분포인 것을 확실하게 알 수 있으면 좋겠지만, business 환경에서는 이것을 아는게 좀 어려워요. 일단 데이터의 수도 적으니까요. 
- 그래서 보통 triangular dist라는 min, mode, max라는 세 가지 값을 가지고 분포를 만들고 시뮬레이션을 돌립니다. 단, min, max는 알기 쉬운데 mode는 어떻게 알 수 있을까요? 가지고 있는 data는 보통 integer가 아니라 float인데요. 

- 그래서 float list에서 mode를 찾는 방법을 알아봅시다. 

## 적절한 bin 개수 찾기 

- 만약 해당 data로 histogram을 그린다고 생각해봅시다. bin size는 몇 개 정도여야 적당할까요? 1부터 sample의 수인 n까지 매우 다양합니다. 
- 다행히 이미 잘 만들어진 계산법이 있습니다 하하핫. 아래 계산법에 따라서 각 값을 해당 bin에 집어넣습니다. 

```python
bin_size = np.round(1+3.322*np.log10(len(input_lst)))## 최적의 binsize를 찾는 계산법 
```

- 전체 코드는 대략 다음과 같습니다. 

```python
def find_mode(input_lst):
    ma, mi = max(input_lst), min(input_lst)
    bin_size = np.round(1+3.322*np.log10(len(input_lst)))## 최적의 binsize를 찾는 계산법 
    r_lst = ((x-mi)/(ma-mi) for x in input_lst)
    r_lst = (x//(1/(bin_size))/(bin_size) for x in r_lst)
    r_dict = {}
    for k in (x*(ma-mi)+mi for x in r_lst):
        if k in r_dict.keys():
            r_dict[k]+=1
        else: 
            r_dict[k]=1
    return sorted(r_dict.items(), key=lambda x: x[1], reverse=True)[0][0]

test_tri = np.random.triangular(1, 3, 5, 10000)
find_mode(test_tri)
```

- 대충 엇비슷하게 나오는군요 하하핫

```
2.9774677741080167
```