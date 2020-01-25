---
title: python으로 association rule mining하기 
category: 
tags: python association-rule pandas itertools python-lib data-mining 

---

## association rule? 

- 학부때 통계 수업때 association rule mining을 배웠던 기억이 (어렴풋하게) 있습니다. 어떻게 풀었는지는 기억이 잘 안나지만, 어떤 상황에 적용하는 것이었는지는 대략 기억나요. 

> "사람들이 쇼핑해 간 데이터들이 쌓여 있다고 하자. 그때 물건 A를 샀을때, 함께 살 확률이 높은 물건 B를 찾을 수 있는가?"

- 이걸 해결했던 것이 association rule이었던 것 같아요. 단지, 쇼핑바구니 뿐만 아니라, 다양한 콘텐츠에 대해서 추천 시스템으로 만들 수 있기 때문에, 해당 알고리즘은 범용성이 매우 크다가라고 할 수 있을 것 같네요. 
- 사실 rule candidate는 아주 많습니다. (조건 set)와 (결과 set)가 exclusive할 때, 총 n 종류가 있을때, 2가지로 나누는 경우를 말하니까요. 계산을 어떻게 할 수 있을까....이거 고등학교 수학인데 이제 못합니다...ㅠㅠ

- 아무튼, `association rule mining`이라는 것은 결국 가능한 모든 rule 중에서 좋은 것들을 찾는 것을 말합니다. 개별 rule을 평가하는 지표들은 다음과 같구요.
    - `support`
    - `confidence`
    - `lift`

### support

- rule의 조건이 일어날 확률

$$
For\ the\ rule\ A \rightarrow  B \\

support(A) = P(A)
$$

### confidence

- rule의 조건이 일어났을때, 결과가 일어날 확률 

$$
confidence(A \rightarrow B) = { { P(A, B) } \over { P(A) } }
$$

### lift 

- 조건과 결과가 각각 독립적이라고 가정했을때 보다 얼마나 더 좋은가? 독립으로 곱한 것보다 높은지, 적은지를 평가한다. 

$$
lift(A \rightarrow B) = { { P(A, B) } \over {P(A) * P(B)} }
$$


## finding golden rule

- 적용해볼 데이터를 찾아보다가 [여기](http://csci.viu.ca/~barskym/teaching/DM2012/labs/LAB7/marketbasket.csv)에  marketbaset 데이터가 있어서, 이를 활용해서 실제로 association rule을 만들어 봤습니다. 

- 일단 일정 support를 넘는 모든 set를 찾고, 그 다음 그 set의 조합으로 만들 수 있는 모든 rule에서 일정 confidence, 일정 lift를 넘는 모든 rule을 뽑아줍니다. 

```python
import pandas as pd 
import itertools 

def support(df, item_lst):
    return (df[list(item_lst)].sum(axis=1)==len(item_lst)).mean()

def make_all_set_over_support(df, support_threshold):
    items = []
    single_items = [col for col in df.columns if support(df, [col]) > support_threshold] # size 1 items
    
    size = 2
    while True:
        new_items = []
        for item_cand in itertools.combinations(single_items, size):
            #print(item_cand, (df[list(item_cand)].sum(axis=1)==size).mean())
            if support(df, list(item_cand)) > support_threshold:
                new_items.append(list(item_cand))
        if len(new_items)==0:
            break
        else:
            items+=new_items
            size+=1
    items += [ [s] for s in single_items]# 이렇게 해줘야 모든 type이 list가 됨
    return items

def make_confidence_lst(df, item_set_over_support, confidence_threshold):
    r_lst = []
    for item1 in item_set_over_support:
        for item2 in item_set_over_support:
            if len(set(item1).intersection(set(item2)))==0:
                conf = support(df, list(set(item1).union(set(item2))))/ support(df, item1)
                if conf > confidence_threshold:
                    r_lst.append((item1, item2, conf))
            else:
                continue
    return sorted(r_lst, key=lambda x: x[2], reverse=True)

def make_lift_lst(df, item_set_over_support, lift_threhsold):
    r_lst = []
    for item1 in item_set_over_support:
        for item2 in item_set_over_support:
            if len(set(item1).intersection(set(item2)))==0:
                lift = support(df, list(set(item1).union(set(item2))))
                lift /= support(df, item1)
                lift /= support(df, item2)
                if lift > lift_threhsold:
                    r_lst.append((item1, item2, lift))
            else:
                continue
    return sorted(r_lst, key=lambda x: x[2], reverse=True)

over_support_lst = make_all_set_over_support(df, 0.07)# 0.05로 하면 두 개짜리도 나옴. 로 하면 3개 짜리도 나옴
print("over support list")
print(over_support_lst)
print("-----------------")
print("over confidence list")
for a, b, conf in  make_confidence_lst(df, over_support_lst, 0.53):
    print("{} => {}: {}".format(a, b, conf))
print("-----------------")
print("over lift list")
for a, b, lift in  make_lift_lst(df, over_support_lst, 5.6):
    print("{} => {}: {}".format(a, b, lift))
print("-----------------")
```

- 결과는 다음과 같습니다. 
- 햄버거 번을 사면, 패티를 산다거나, 핫도그를 사면, sweet relish를 산다거나, 의미있는 rule이 많이 뽑혔는데, "치약=> 우유"는 조금 신기하군요. 

```
over support list
[[' 98pct. Fat Free Hamburger'], [' Onions'], [' Potato Chips'], [' Hot Dogs'], [' 2pct. Milk'], [' Eggs'], [' White Bread'], [' Cola'], [' Toothpaste'], [' Hamburger Buns'], [' Wheat Bread'], [' Sweet Relish'], [' Toilet Paper']]
-----------------
over confidence list
[' Hamburger Buns'] => [' 98pct. Fat Free Hamburger']: 0.6804123711340206
[' Toothpaste'] => [' White Bread']: 0.6018518518518519
[' Toothpaste'] => [' Eggs']: 0.5648148148148148
[' Wheat Bread'] => [' White Bread']: 0.5619047619047619
[' Wheat Bread'] => [' 2pct. Milk']: 0.5523809523809524
[' Sweet Relish'] => [' Hot Dogs']: 0.5517241379310344
[' Toothpaste'] => [' 2pct. Milk']: 0.5462962962962963
[' Onions'] => [' White Bread']: 0.5321100917431193
-----------------
over lift list
[' Hamburger Buns'] => [' 98pct. Fat Free Hamburger']: 7.291663284357497
[' 98pct. Fat Free Hamburger'] => [' Hamburger Buns']: 7.291663284357496
[' Hot Dogs'] => [' Sweet Relish']: 5.9594964422550625
[' Sweet Relish'] => [' Hot Dogs']: 5.959496442255062
[' Toothpaste'] => [' Wheat Bread']: 5.640828924162257
[' Wheat Bread'] => [' Toothpaste']: 5.640828924162257
-----------------
```

## wrap-up

- 지금은 연산 시간을 크게 고려하지 않고, 코딩했습니다. 더 잘 코딩할 수 있을텐데, 귀찮아요 헤헷 

## reference 

- <https://www.kaggle.com/datatheque/association-rules-mining-market-basket-analysis>
- <https://ratsgo.github.io/machine%20learning/2017/04/08/apriori/>