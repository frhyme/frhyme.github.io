---
title: 7전 4선승전에서 첫번째 경기는 얼마나 중요한가?
category: project 
tags: python project numpy probablity
---

## 스포츠에서 첫번째 경기를 이기는 것은 얼마나 경기에 영향을 미치는가?

- 많은 스포츠에서 "첫번째 경기를 잡는 것이 중요하다"라는 말이 있죠. 7전 4선승제 라고 봤을 때, 첫번째 경기를 이기게 되면, 남은 6경기에서 3경기만 잡으면 되므로 우승 확률 자체가 올라가게 되죠. 되게 당연한 이야기인데, 과연 이게 얼마나 우승 확률을 올려주는지 간단한게 정리해 봤습니다.

## 7전 4선승제의 경우

- 팀의 강 경기별 승리 확률이 `p`라고 할 때, 7경기에서 4번 이상 우승할 확률은 대강 다음 코드와 같습니다.
  - `combiation(n, r)`: nCr
  - `power(n, r)`: `n`의 `r`승  

```python
combination(7, 4) * power(p, 4) * power(1.0 - p, 3)
combination(7, 5) * power(p, 5) * power(1.0 - p, 2)
combination(7, 6) * power(p, 6) * power(1.0 - p, 1)
combination(7, 7) * power(p, 7) * power(1.0 - p, 0)
```

- 우선, 각 경기의 승리 확률이 `p`라면, 7전 4선승 확률도 `p`라고 생각할 수 있지만, 동일하지 않습니다. 가령, 한 경기의 승리 확률이 0.5보다 높다면, 7전 4승의 확률은 다음과 같이 조금씩 더 올라가게 됩니다. 반대로, 당연한 이야기지만. 한 경기의 승리 확률이 0.5보다 낮다면 7전 4선승의 확률은 낮아지게 되죠.
- 대략 아래에서 보는 것처럼 승률이 0.5에서 차이가 많이 날수록, 7전 4선승 확률에서는 더 큰 차이가 발생하게 됩니다.

```plaintext
win_p: 0.40 -- win 4/7: 0.290 -- diff: -0.110
win_p: 0.41 -- win 4/7: 0.309 -- diff: -0.101
win_p: 0.42 -- win 4/7: 0.329 -- diff: -0.091
win_p: 0.43 -- win 4/7: 0.350 -- diff: -0.080
win_p: 0.44 -- win 4/7: 0.371 -- diff: -0.069
win_p: 0.45 -- win 4/7: 0.392 -- diff: -0.058
win_p: 0.46 -- win 4/7: 0.413 -- diff: -0.047
win_p: 0.47 -- win 4/7: 0.435 -- diff: -0.035
win_p: 0.48 -- win 4/7: 0.456 -- diff: -0.024
win_p: 0.49 -- win 4/7: 0.478 -- diff: -0.012
win_p: 0.50 -- win 4/7: 0.500 -- diff: +0.000
win_p: 0.51 -- win 4/7: 0.522 -- diff: +0.012
win_p: 0.52 -- win 4/7: 0.544 -- diff: +0.024
win_p: 0.53 -- win 4/7: 0.565 -- diff: +0.035
win_p: 0.54 -- win 4/7: 0.587 -- diff: +0.047
win_p: 0.55 -- win 4/7: 0.608 -- diff: +0.058
win_p: 0.56 -- win 4/7: 0.629 -- diff: +0.069
win_p: 0.57 -- win 4/7: 0.650 -- diff: +0.080
win_p: 0.58 -- win 4/7: 0.671 -- diff: +0.091
win_p: 0.59 -- win 4/7: 0.691 -- diff: +0.101
win_p: 0.60 -- win 4/7: 0.710 -- diff: +0.110
```

- 이제, 첫번째 경기를 이겼을 때의 우승 확률이 어떻게 변화하는지를 확인해 봅니다. 즉, 7경기에서 4경기를 이겨야 하는 경우에서, 6경기에서 3경기를 이겨야하는 경우로 변하는 경우, 우승 확률이 어떻게 달라지는지를 정리합니다.
- 경기1을 이기면, 승률이 낮아도 0.1(10%) 이상의 승률을 올려주는데, 특히 승률이 비슷비슷할 경우, 0.5에 가까운 경우에는 승률을 약 0.17(17%) 까지도 올려줍니다. 
- 반대로, 이미 승률이 높은 경우, 매 경기 승률이 0.7인 경우에는 경기1을 이긴 상황이라도 0.05 정도 밖에 올라가지 않습니다.
- 물론 7전 4선승이 아니라, 5전 3선승일 경우에는 첫 경기의 중요성이 더 커지겠죠.

```plaintext
win_p: 0.30 -- win 4/7: 0.126 -- win 3/6: 0.256 -- diff: +0.130
win_p: 0.32 -- win 4/7: 0.153 -- win 3/6: 0.294 -- diff: +0.140
win_p: 0.34 -- win 4/7: 0.184 -- win 3/6: 0.333 -- diff: +0.149
win_p: 0.36 -- win 4/7: 0.217 -- win 3/6: 0.373 -- diff: +0.157
win_p: 0.38 -- win 4/7: 0.252 -- win 3/6: 0.414 -- diff: +0.162
win_p: 0.40 -- win 4/7: 0.290 -- win 3/6: 0.456 -- diff: +0.166
win_p: 0.42 -- win 4/7: 0.329 -- win 3/6: 0.497 -- diff: +0.168
win_p: 0.44 -- win 4/7: 0.371 -- win 3/6: 0.538 -- diff: +0.168
win_p: 0.46 -- win 4/7: 0.413 -- win 3/6: 0.579 -- diff: +0.166
win_p: 0.48 -- win 4/7: 0.456 -- win 3/6: 0.618 -- diff: +0.162
win_p: 0.50 -- win 4/7: 0.500 -- win 3/6: 0.656 -- diff: +0.156
win_p: 0.52 -- win 4/7: 0.544 -- win 3/6: 0.693 -- diff: +0.149
win_p: 0.54 -- win 4/7: 0.587 -- win 3/6: 0.728 -- diff: +0.141
win_p: 0.56 -- win 4/7: 0.629 -- win 3/6: 0.761 -- diff: +0.132
win_p: 0.58 -- win 4/7: 0.671 -- win 3/6: 0.792 -- diff: +0.121
win_p: 0.60 -- win 4/7: 0.710 -- win 3/6: 0.821 -- diff: +0.111
win_p: 0.62 -- win 4/7: 0.748 -- win 3/6: 0.847 -- diff: +0.099
win_p: 0.64 -- win 4/7: 0.783 -- win 3/6: 0.871 -- diff: +0.088
win_p: 0.66 -- win 4/7: 0.816 -- win 3/6: 0.893 -- diff: +0.077
win_p: 0.68 -- win 4/7: 0.847 -- win 3/6: 0.913 -- diff: +0.066
win_p: 0.70 -- win 4/7: 0.874 -- win 3/6: 0.930 -- diff: +0.056
```

## 5전 3선승제의 경우

- 5전 3선승제의 경우는 약 0.21까지 확률을 올려줍니다. 7전 4선승제보다 더 높죠. 

```plaintext
win_p: 0.30 -- win 3/5: 0.163 -- win 2/4: 0.348 -- diff: +0.185
win_p: 0.32 -- win 3/5: 0.191 -- win 2/4: 0.384 -- diff: +0.193
win_p: 0.34 -- win 3/5: 0.220 -- win 2/4: 0.419 -- diff: +0.199
win_p: 0.36 -- win 3/5: 0.251 -- win 2/4: 0.455 -- diff: +0.204
win_p: 0.38 -- win 3/5: 0.283 -- win 2/4: 0.490 -- diff: +0.206
win_p: 0.40 -- win 3/5: 0.317 -- win 2/4: 0.525 -- diff: +0.207
win_p: 0.42 -- win 3/5: 0.353 -- win 2/4: 0.559 -- diff: +0.207
win_p: 0.44 -- win 3/5: 0.389 -- win 2/4: 0.593 -- diff: +0.204
win_p: 0.46 -- win 3/5: 0.425 -- win 2/4: 0.625 -- diff: +0.200
win_p: 0.48 -- win 3/5: 0.463 -- win 2/4: 0.657 -- diff: +0.194
win_p: 0.50 -- win 3/5: 0.500 -- win 2/4: 0.688 -- diff: +0.187
win_p: 0.52 -- win 3/5: 0.537 -- win 2/4: 0.717 -- diff: +0.179
win_p: 0.54 -- win 3/5: 0.575 -- win 2/4: 0.745 -- diff: +0.170
win_p: 0.56 -- win 3/5: 0.611 -- win 2/4: 0.772 -- diff: +0.160
win_p: 0.58 -- win 3/5: 0.647 -- win 2/4: 0.797 -- diff: +0.150
win_p: 0.60 -- win 3/5: 0.683 -- win 2/4: 0.821 -- diff: +0.138
win_p: 0.62 -- win 3/5: 0.717 -- win 2/4: 0.843 -- diff: +0.127
win_p: 0.64 -- win 3/5: 0.749 -- win 2/4: 0.864 -- diff: +0.115
win_p: 0.66 -- win 3/5: 0.780 -- win 2/4: 0.883 -- diff: +0.103
win_p: 0.68 -- win 3/5: 0.809 -- win 2/4: 0.900 -- diff: +0.091
win_p: 0.70 -- win 3/5: 0.837 -- win 2/4: 0.916 -- diff: +0.079
```

## 3전 2선승제의 경우 

- 3전 2선승제에서 첫 경기의 중요성...은 너무 자명하지만, 그래도 해보면 얘는 0.3까지도 올려주네요 호호.

```plaintext
win_p: 0.30 -- win 2/3: 0.216 -- win 1/2: 0.510 -- diff: +0.294
win_p: 0.32 -- win 2/3: 0.242 -- win 1/2: 0.538 -- diff: +0.296
win_p: 0.34 -- win 2/3: 0.268 -- win 1/2: 0.564 -- diff: +0.296
win_p: 0.36 -- win 2/3: 0.295 -- win 1/2: 0.590 -- diff: +0.295
win_p: 0.38 -- win 2/3: 0.323 -- win 1/2: 0.616 -- diff: +0.292
win_p: 0.40 -- win 2/3: 0.352 -- win 1/2: 0.640 -- diff: +0.288
win_p: 0.42 -- win 2/3: 0.381 -- win 1/2: 0.664 -- diff: +0.283
win_p: 0.44 -- win 2/3: 0.410 -- win 1/2: 0.686 -- diff: +0.276
win_p: 0.46 -- win 2/3: 0.440 -- win 1/2: 0.708 -- diff: +0.268
win_p: 0.48 -- win 2/3: 0.470 -- win 1/2: 0.730 -- diff: +0.260
win_p: 0.50 -- win 2/3: 0.500 -- win 1/2: 0.750 -- diff: +0.250
win_p: 0.52 -- win 2/3: 0.530 -- win 1/2: 0.770 -- diff: +0.240
win_p: 0.54 -- win 2/3: 0.560 -- win 1/2: 0.788 -- diff: +0.229
win_p: 0.56 -- win 2/3: 0.590 -- win 1/2: 0.806 -- diff: +0.217
win_p: 0.58 -- win 2/3: 0.619 -- win 1/2: 0.824 -- diff: +0.205
win_p: 0.60 -- win 2/3: 0.648 -- win 1/2: 0.840 -- diff: +0.192
win_p: 0.62 -- win 2/3: 0.677 -- win 1/2: 0.856 -- diff: +0.179
win_p: 0.64 -- win 2/3: 0.705 -- win 1/2: 0.870 -- diff: +0.166
win_p: 0.66 -- win 2/3: 0.732 -- win 1/2: 0.884 -- diff: +0.153
win_p: 0.68 -- win 2/3: 0.758 -- win 1/2: 0.898 -- diff: +0.139
win_p: 0.70 -- win 2/3: 0.784 -- win 1/2: 0.910 -- diff: +0.126
```

## wrap-up

- 궁금해서 간단하게 계산해보는 중에, NBA 파이널에서 첫번째, 두번째 경기를 이긴 피닉스는 3, 4, 5경기를 모두 져 버렸습니다. 이제 피닉스가 우승할 수 있는 확률은 0.5이하로 감소해버렸네요. 뭐, 물론 크리스폴 팬은 아니지만, 크리스폴의 인생역정에서 이번에는 우승하길 바랐는데 쉽지 않겠네요. 

```plaintext
win_p: 0.300, win_5_2: 0.472, win_2_2: 0.090
win_p: 0.320, win_5_2: 0.513, win_2_2: 0.102
win_p: 0.340, win_5_2: 0.552, win_2_2: 0.116
win_p: 0.360, win_5_2: 0.591, win_2_2: 0.130
win_p: 0.380, win_5_2: 0.628, win_2_2: 0.144
win_p: 0.400, win_5_2: 0.663, win_2_2: 0.160
win_p: 0.420, win_5_2: 0.697, win_2_2: 0.176
win_p: 0.440, win_5_2: 0.729, win_2_2: 0.194
win_p: 0.460, win_5_2: 0.759, win_2_2: 0.212
win_p: 0.480, win_5_2: 0.787, win_2_2: 0.230
win_p: 0.500, win_5_2: 0.812, win_2_2: 0.250
win_p: 0.520, win_5_2: 0.837, win_2_2: 0.270
win_p: 0.540, win_5_2: 0.859, win_2_2: 0.292
win_p: 0.560, win_5_2: 0.879, win_2_2: 0.314
win_p: 0.580, win_5_2: 0.897, win_2_2: 0.336
win_p: 0.600, win_5_2: 0.913, win_2_2: 0.360
win_p: 0.620, win_5_2: 0.927, win_2_2: 0.384
win_p: 0.640, win_5_2: 0.940, win_2_2: 0.410
win_p: 0.660, win_5_2: 0.951, win_2_2: 0.436
win_p: 0.680, win_5_2: 0.961, win_2_2: 0.462
win_p: 0.700, win_5_2: 0.969, win_2_2: 0.490
```

## raw code

```python
import numpy as np 


def factorial(n):
    if n == 1:
        return 1
    else: 
        r = 1
        for i in range(1, n + 1):
            r = r * i
        return r


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return permutation(n, r) / factorial(r)


def combination_p(n, r, p):
    return combination(n, r) * power(p, r) * power((1 - p), n - r)


def cumululative_combination_p(n, r, p):
    # 1부터 r(exclusive) combiation sum
    return_v = 0
    for i in range(0, r):
        return_v += combination_p(n, i, p)
    return return_v


def power(a, b):
    return a ** b


print("------------------------")
for win_p in np.linspace(0.4, 0.6, 21):
    win_7_4 = 1.0 - cumululative_combination_p(7, 4, win_p)
    diff = win_7_4 - win_p
    print(f"win_p: {win_p:.2f} -- win 4/7: {win_7_4:.3f} -- diff: {diff:+.3f}")

print("------------------------")
for win_p in np.linspace(0.3, 0.7, 21):
    win_7_4 = 1.0 - cumululative_combination_p(7, 4, win_p)
    win_6_3 = 1.0 - cumululative_combination_p(6, 3, win_p)

    diff = win_6_3 - win_7_4
    print(f"win_p: {win_p:.2f} -- win 4/7: {win_7_4:.3f} -- win 3/6: {win_6_3:.3f} -- diff: {diff:+.3f}")

print("------------------------")
for win_p in np.linspace(0.3, 0.7, 21):
    win_5_3 = 1.0 - cumululative_combination_p(5, 3, win_p)
    win_4_2 = 1.0 - cumululative_combination_p(4, 2, win_p)

    diff = win_4_2 - win_5_3
    print(f"win_p: {win_p:.2f} -- win 3/5: {win_5_3:.3f} -- win 2/4: {win_4_2:.3f} -- diff: {diff:+.3f}")
print("------------------------")
for win_p in np.linspace(0.3, 0.7, 21):
    win_3_2 = 1.0 - cumululative_combination_p(3, 2, win_p)
    win_2_1 = 1.0 - cumululative_combination_p(2, 1, win_p)

    diff = win_2_1 - win_3_2 
    print(f"win_p: {win_p:.2f} -- win 2/3: {win_3_2:.3f} -- win 1/2: {win_2_1:.3f} -- diff: {diff:+.3f}")
print("------------------------")
print("------------------------")
```
