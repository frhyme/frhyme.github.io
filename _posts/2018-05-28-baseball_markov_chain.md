---
title: 야구) 야구에 Markov Chain 적용하기
category: baseball
tags: baseball markov-chain sabermetrics

---

## 야구 equals 마코브 체인 

- [Markov chain의 영문 위키피디아](https://en.wikipedia.org/wiki/Markov_chain#Discrete-time_Markov_chain) 아래 쪽을 보면 다음과 같은 내용이 담겨 있습니다. 

> Markov chain models have been used in advanced baseball analysis since 1960, although their use is still rare. Each half-inning of a baseball game fits the Markov chain state when the number of runners and outs are considered. During any at-bat, there are 24 possible combinations of number of outs and position of the runners. Mark Pankin shows that Markov chain models can be used to evaluate runs created for both individual players as well as a team.[84] He also discusses various kinds of strategies and play conditions: how Markov chain models have been used to analyze statistics for game situations such as bunting and base stealing and differences when playing on grass vs. astroturf.[85]

- 한글로 해석하자면, 대략 다음과 같습니다(발로 번역했습니다)

> 마코브체인은 존나 잘 쓰이지도 않던 1960년대에 야구쪽에서 쓰였다. 개별 이닝은 아웃카운트와 주자 로 구분된 24가지 상황을 state로 한 마코브 체인으로 모델링될 수 있으며, 팀과 선수가 득점에 얼마나 기여하는지를 평가하기 위해 사용될 수 있음을 Mark Pankin이 증명했다. 또한, 마코브체인을 이용하여 다양한 전략과 경기 조건(번트와 도루, 조건: 잔디, 인조잔디)을 분석하였다

- 사실 다시 생각해보면, 턴제로 구분되어 있는 야구는 마코브체인으로 모델링하기에 매우 적합한, 게임입니다. 이미 데이터도 아주 많이 쌓여 있는 것이 사실일 것이고요. 
    - 정확하게는 discrete Time Markov Chain(DTMC)에 적용하기 적합합니다. Time은 매 아웃카운트 로 구분될 수 있겠죠
    - 축구처럼 턴이 명확하지 않은 경우에는 Continous Time Markov Chain을 쓰는 것이 적합할 것 같네요. 

## 야구를 DTMC로 모델링합시다. 

- 기사말고, 좀 잘 정리된 자료를 찾아봤는데 다행히 [여기에](http://www.pankin.com/markov/theory.htm) 있습니다. 일단은 이 내용을 기준으로 진행하겠습니다. 

- `T`: Transition matrix(state to state), 28 by 28 matrix
    - \#01: 0아웃 주자없음 
    - \#02: 1아웃 주자없음
    - \#03: 2아웃 주자없음
    - \#04: 0아웃 1루
    - ...
    - \#07: 0아웃 2루
    - ...
    - \#10: 0아웃 3루
    - ...
    - \#13: 0아웃 1,2루
    - ...
    - \#16: 0아웃 1,3루
    - ...
    - \#19: 0아웃 2,3루
    - ...
    - \#20: 0아웃 1,2,3루
    - ...
    - \#25: 쓰리아웃 무득점 
    - \#26: 쓰리아웃 1득점
    - \#27: 쓰리아웃 2득점
    - \#28: 쓰리아웃 3득점

- `R`: each plate appeareance 별 기대득점 matrix 28 by 1 matrix 
    - R(1)  = p1,1
        - state1(0아웃 주자없음)에서 다시 state1이 될 확률은 결국 홈런밖에 없음. 
    - R(2)  = p2,2
    - R(4)  = 2p4,1 + p4,4 + p4,7 + p4,10 + p4,2
    - R(23) = 4p23,2 + 3(p23,5 + p23,8 + p23,11 + p23,3)
        + 2(p23,14 + p23,17 + p23,20 + p23,6 + p23,9 + p23,12 + p23,27)
        + p23,23 + p23,15 + p23,18 + p23,21 + p23,26
    - R(25) = R(26) = R(27) = R(28) = 0

- `E`: R + TR + TTR + TTTR ..., 해당 state부터 이닝 종료까지의 생산 가능한 득점, 28 by 1 matrix 
    - `R`은 각 state에서 each plate appearance에서 발생가능한 득점을 말하고, 여기에 T를 연속으로 곱해간다는 것은 각 상황에서 타석이 끊어지지 않고 이어질 경우를 고려하는 것임. 따라서 이렇게 계산된 값은 해당 state부터 이닝 종료까지 생산 가능한 득점을 말하고, 이를 `Markov Run`이라고 함. 
    - = (I + T + T^2 + T^3 + … )R 
    - = (I - T)^(-1) (I - T)(I + T + T^2 + T^3 + … )R [since (I - T)^(-1) (I - T) = I] 
    - = (I - T)^(-1) (I - T + T - T^2 + T^2 - T^3 + T^3 - … )R 
    - = (I - T)^(-1) IR 
    - = (I - T)^(-1) R 

## Markov chain with identical batter

- 이제 transition matrix `T`를 실제 값으로 정의하여, 실험을 해보도록 하겠습니다. 

### 게임 중 발생 가능한 이벤트 

- 본 포스트에서 정의한 마코브체인은 discrete-time에서 정의되며, 각 time은 타자의 plate appearance로 정의됩니다. 따라서, 아래 이벤트 들의 확률에 의해 `T`가 정의됩니다. 
    - 1루타, 수비실책으로 인한 1루타:
    - 2루타:
    - 3루타:
    - 볼넷, 고의사구, 사구:
    - 홈런:
    - 삼진:
    - 병살타: 병
    - 외야 뜬공: 경우에 따라, 삼진과 같은 이벤트일 수도, 아닐 수도 있습니다. 3루에 주자가 있다고 해도, 발이 빠른 주자와 아닐 경우가 구분되는데, 마코브체인에서는 이를 구분할 수 없음(memoryless)
- 그러나, 이를 모두 표현하면 너무 복잡하기 때문에, 간단하게 테스트하기 위해서 아래 가정에 따라 실제를 단순화 합니다. 

### 단순화를 위한 몇 가지 가정들 

1. 모든 타자가 동일한 스탯을 가지고 있다고 가정합니다.
2. time을 타석의 타자에 의해서 결정된다고 봤기 때문에, 도루는 발생하지 않는 것으로 가정하였다. 
3. 일단은 안타와 삼진만 있다고 가정합니다. 
4. 심지어, 안타에도 1루타/홈런 만 있다고 가정하였다. 
5. 루상의 주자는 타자와 똑같은 양을 진루합니다(1루타: 2루에서 3루, 2루타: 2루에서 홈)

- 개별 이벤트의 확률은 다음과 같다. 
    - P(1루타): 0.3
    - P(홈런): 0.03
    - P(삼진): 1 - P(홈런) - P(1루타)

### T, Exp. Runs at PA, Exp. Runs until inning end.

- 자, 이제 Transition matrix `T`, Expected Runs at PA `R`, Expected Runs until inning close `E`를 계산한다. 파이썬으로 코딩하였다. 

```python
import pandas as pd
import numpy as np

pDict = {"1b": 0.3,
         "hr": 0.03,
         'so':0.67
        }
"""(out, base) tuple, 하지만 out이 3일 경우 (out, score)
"""
OutCount = [0, 1, 2]
Base = ["0", "1", "2", '3', '12', '13', '23', '123']
OutBase_index = [(out, b) for out in OutCount for b in Base]
OutBase_index += [(3, 0), (3, 1), (3, 2), (3, 3)]
"""multi index(hierarchical index)를 만들려면, multi index 객체를 만들어서 넘겨줘야함. 
"""
OutBase_index = pd.MultiIndex.from_tuples(OutBase_index)
# multi index

T_df = pd.DataFrame(np.zeros(28*28).reshape(28, 28) ,index = OutBase_index, columns = OutBase_index)
"""1루타로 인한 상황 변화 업데이트"""
for i in range(0, 3):
    T_df.loc()[i, '0'][i, '1'] += pDict['1b']
    T_df.loc()[i, '1'][i, '12'] += pDict['1b']
    T_df.loc()[i, '2'][i, '13'] += pDict['1b']
    T_df.loc()[i, '3'][i, '1'] += pDict['1b']
    T_df.loc()[i, '12'][i, '123'] += pDict['1b']
    T_df.loc()[i, '13'][i, '12'] += pDict['1b']
    T_df.loc()[i, '23'][i, '13'] += pDict['1b']
    T_df.loc()[i, '123'][i, '123'] += pDict['1b']
"""홈런으로 인한 상황 변화 업데이트"""
for Ind in T_df.index:
    o, b = Ind
    if o <3:
        T_df.loc()[o, b][o, '0'] += pDict['hr']
"""삼진으로 인한 상황 변화 업데이트"""
for Ind in T_df.index:
    o, b = Ind
    if o < 2:
        T_df.loc()[o, b][o+1, b] += pDict['so']
    elif o==2:
        T_df.loc()[o, b][o+1, 0] += pDict['so']
"""absorbing state"""
for Ind in T_df.index:
    if Ind[0]==3:
        T_df.loc()[Ind][Ind] = 1
T_df
T = T_df.values
```

- 이제  `R`을 정의하고 출력해준다. 
    - 아웃카운트와 상관없이, 모두 동일한 것은, 내가 (희생플라이) 등을 무시했기 때문. 

```python
# define R
R = pd.DataFrame(np.zeros(28).reshape(28,1),
                 index=T_df.index, columns=['Expected R. at PA'])
for Ind in R.index:
    o, b = Ind
    if o!=3:
        if b!='0':
            R.loc()[o, b] += pDict['hr']*(len(b)+1)
        else:
            R.loc()[o, b] += pDict['hr']*1.0
for Ind in R.index:
    o, b = Ind
    if o !=3 and '3' in b:
        R.loc()[o, b] += pDict['1b']*1.0
print(R)
```
```
       Expected R. at PA
0 0                 0.03
  1                 0.06
  2                 0.06
  3                 0.36
  12                0.09
  13                0.39
  23                0.39
  123               0.42
1 0                 0.03
  1                 0.06
  2                 0.06
  3                 0.36
  12                0.09
  13                0.39
  23                0.39
  123               0.42
2 0                 0.03
  1                 0.06
  2                 0.06
  3                 0.36
  12                0.09
  13                0.39
  23                0.39
  123               0.42
3 0                 0.00
  1                 0.00
  2                 0.00
  3                 0.00
```

- 이닝 종료까지 가능한 평균 득점을 계산하였다. 실제로는 역함수를 사용하여 계산했어야 했지만, 내가 너무 단순화하여 `T`를 정의하였기 때문에, `T`는 역함수가 없음. 

```python
"""
E = R + TR + TTR + TTTR ...,
E = (I - T) - 1R 
"""
E = R.copy()
for i in range(0, 100):
    a = T
    for j in range(0, i):
        a = a.dot(T)
    E+=a.dot(R)
#E = np.linalg.inv(np.identity(28) - T).dot(R)
E.columns = ["Expected R. until inning end"]
print(E)
```

- 실제로 [Tom tango의 Run Expectancy Matrix](http://www.tangotiger.net/re24.html)와 경향성은 비슷한 것을 알 수 있다. 마코브체인 좋앙

```
       Expected R. until inning end
0 0                        0.356147
  1                        0.622285
  2                        0.784697
  3                        1.055384
  12                       1.050836
  13                       1.321522
  23                       1.483934
  123                      1.750073
1 0                        0.192205
  1                        0.352762
  2                        0.473965
  3                        0.743305
  12                       0.634522
  13                       0.903862
  23                       1.025065
  123                      1.185622
2 0                        0.075537
  1                        0.144237
  2                        0.204537
  3                        0.405537
  12                       0.273237
  13                       0.474237
  23                       0.534537
  123                      0.603237
3 0                        0.000000
  1                        0.000000
  2                        0.000000
  3                        0.000000
```

## wrap-up

- 마코브체인에서 타순별로 T_1...T_9 를 정의하여 다르게 배치해가면서 최적의 타순배치를 찾는 작업도 할 수 있습니다. 이런 방식으로, 다양한 상황에 대해 시뮬레이션을 수행해 볼 수 있다는 것이, 마코브체인의 강점이라고 할 수 있습니다. 
- 나중에, 2루타, 3루타 와 같은 방식으로 구체화하여 적용해보면 재밌을 것 같다는 생각이 드네요. 

## reference

- <https://www.fangraphs.com/tht/introducing-markov-chains/>
- <https://www.fangraphs.com/blogs/more-fun-with-markov-custom-run-expectancies/>
- <http://www.pankin.com/markov/theory.htm>
- <https://dc.uwm.edu/cgi/viewcontent.cgi?article=1969&context=etd>