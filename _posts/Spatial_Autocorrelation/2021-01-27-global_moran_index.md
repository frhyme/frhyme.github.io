---
title: Moran's Index python으로 계산하기
category: others
tags: python HypothesisTesting scipy autocorrelation
---

## Global Moran' I

- [Moran's Index](https://en.wikipedia.org/wiki/Moran%27s_I)는 특정 구역 혹은 관계들 속에 군집이 존재하는지를 통계적으로 검정하는 방법입니다.
- **Null Hypothesis**: "군집이 존재하지 않는다", 즉, 모든 구역이 Randomness를 가진다는 것을 null Hypothesis로 둡니다. 즉 "AutoCorrelation이 없다"를 가정한다는 것이죠.
- 좀 더 구분한다면, Moran's Index의 값에 따라 1, 0, -1로 나뉩니다.
  - **Moran's Index가 1인 경우**: "군집이 존재한다"는 것을 의미합니다.
  - **Moran's Index가 0인 경우**: 군집이 존재하지 않는다를 의미하죠. 
  - **Moran's Index가 -1인 경우**: 얘는 마치 체크무늬와 같이, 완전히 군집이 아닌 경우를 말합니다.
- 계산이 더러워서, 수식 말고 예시를 들어 말로 설명하면 다음과 같습니다.
  - 우리는 인구가 높은 구역끼리, 낮은 구역끼리 서로 모여 있는지 확인해보려고 합니다.
  - 가령 구역 A, B가 있고 각 인구 수를 각각 `a`, `b`라고 하겠습니다. 전체 구역의 평균을 `m`이라고 하죠.
  - 모든 구역의 인구 수에서 평균을 빼서 표준화시키면, 평균보다 큰 구역은 양수의 값을 가지고, 평균보다 작은 구역은 음수의 값을 가집니다.
  - 그리고, 지역적으로 인접해 있다고 생각되는 구역들에 대해서 서로 인구 수를 곱하여 줍니다. 즉, 인구수가 평균보다 높은 애들끼리 인접해 있다면 그 곱이 양수가 나올 것이고, 또 평균보다 낮은 애들끼리 인접해 있다면 그 곱 또한 양수가 나오겠죠. 반대로, 높은 애와 낮은 애가 인접해 있다면 그 곱은 음수가 나올 겁니다.
  - 만약, 정말 random이라면(null hypothesis를 따른다면), 그 분포는 양수와 음수가 뒤섞여서 존재하겠죠.
  - 그러나, 군집이 존재한다면, 즉 양수끼리 음수끼리 서로 인접하다면 아마도 이웃간의 곱을 계산했을 때, 양수가 많이 나오게 되겠죠.
  - 또한, 체크무늬처럼 존재한다면, 이웃간의 곱은 모두 음수로 구성되어 있겠죠.
  - 이 분포를 사용해서 대략 현재 분포가 어떤 지를 대략 측정할 수 있겠죠. 이런 방식을 바로 Moran's I라고 합니다. 물론, 그 계산방법은 좀 복잡합니다만.

### python Implementation

- 수식은 좀 이해가 안되어서, 대략 다음과 같이 코드로 작성하였습니다. 긴 코드는 뒤 쪽에 작성하였고, 여기서는 결과만 보여주는 식으로 작성하였습니다.
- 이웃간의 인접성을 평가하는 방법은 여러 가지인데(클수록 인접하다고 평가). 저는 그냥 인접하면 1 아니면 0으로 평가하였습니다. 보통 Moran's I는 실제 지역을 기반으로 계산되는 일이 많아서 지역 간 거리에 따라서 계산되기도 합니다.
- 수식이 좀 복잡해 보이지만, Moran's I ~ `norm(mu, sigma)`이므로 Moran's I를 계산해주고, 얘가 기존 분포를 따른다고 봐야하는지, 따르지 않는지 결과를 내는게 다죠.

#### Case 1 - 서로 다른 인구 수끼리 연결

- 여기서는 (평균보다 높은 지역, 평균보다 낮은 지역)끼리 연결되어 있다고 가정합니다.
- 따라서, 얘는 군집이 있는게 아니고, 체스판처럼 형태를 갖추고 있다고 봐야죠.
- 따라서, `I`는 -1.0이 나오기는 하는데, sample 수가 적어서 크게 유의미하지는 않습니다.

```python
"""
- Case 1:
- A, B, C, D는 각각 [10, 0, 0, 10]의 인구를 가진다.
- 서로 인접한 이웃은  ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')
즉, 서로 인구 평균 이상 과 평균 이하가 인접한 것이죠.
"""
x_dict = {'A': 10, 'B': 0, 'C': 0, 'D': 10}
x_neighbor_lst = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')
]
evaluate_I(x_dict, x_neighbor_lst)
# I: -1.0
# z_score: -0.2294157338705618
# P(-0.229 < Z): 0.41
```

#### Case 2 - 비슷한 인구수끼리 연결

- 여기서는 높은 애들끼리, 낮은 애들끼리 연결합니다.
- 이렇게 할 경우, `I`는 1.0에 가깝게 나오죠. 물론 이때도 수가 적어서 유의미하지는 않습니다.

```python
x_dict = {'A': 10, 'B': 0, 'C': 0, 'D': 10}
x_neighbor_lst = [
    ('A', 'D'), ('B', 'C')
]
evaluate_I(x_dict, x_neighbor_lst)
# I: 1.0
# z_score: 0.5443310539518174
# P(0.544 < Z): 0.71
```

--- 

## Wrap-up

- 지금은 global Moran_index만 측정했습니다. 얘는 Hot Zone(높은 애들기리 모여 있는 군집), Cold Zone(낮은 애들끼리 모여 있는 군집)과 상관없이, 군집이 있는지 없는지만 파악할 수 있습니다.
- 그러나, 상황에 따라서는 Hot Zone이 존재하는지, Cold Zone이 존재하는지, 그리고 존재한다면 어떤 point에서 발생하는지에 대해서도 궁금할 수 있죠. 이 부분은 나중에 Getis Ord G를 공부해서 정리해보도록 하겠습니다.
- 그리고, 수식을 좀 더 까보면 더 보기 편하게 만들 수 있을 것 같긴 해요. 가령 지금은 굳이 adjacency matrix를 만들어서 계산량을 키웠는데, 그냥 이웃한 애들만 기억해두고 처리해도 되는 거니까요. 그렇게 하면, input을 dictionary로 고정해둔 상태에서 진행할 수 있을 것 같아서, 코드의 가독성이 더 좋아질 것 같아요.

## Reference

- [Moran의 I 통계량(Moran's I statistics)](https://schbeom.tistory.com/436)
- [공간자기상관 Spatial Autocorrelation - ppt download](https://slidesplayer.org/slide/14145433/)
- [How Spatial Autocorrelation (Global Moran's I) works](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm)

---

## Raw Code

```python
from scipy.stats import norm

def make_w_matrix(X_dict, X_neighbor_lst):
    # Look방식으로 상하좌우만 인접하다고 판정
    N = len(X_dict)
    Xs = list(X_dict.keys())
    w = [[0 for j in range(0, N)] for i in range(0, N)]
    for x_i, x_j in X_neighbor_lst:
        i = Xs.index(x_i)
        j = Xs.index(x_j)
        w[i][j] = 1
        w[j][i] = 1
    return w

def make_c_matrix(X_dict, w):
    x = [v for k, v in X_dict.items()]
    x_avg = sum(x) / len(x)
    c = [[0 for j in range(0, len(x))]for i in range(0, len(x))]
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if i != j:
                c[i][j] = (x_avg - x[i]) * (x_avg - x[j])
    return c

def make_I(x_dict, w, c):
    def make_W(w):
        W = 0.0
        for i in range(0, len(w)):
            for j in range(0, len(w)):
                W += w[i][j]
        return W
    # ==============================
    x = [v for k, v in x_dict.items()]
    n = len(x)
    I_upper = 0.0
    for i in range(0, n):
        for j in range(0, n):
            I_upper += w[i][j] * c[i][j]
    I_upper = n * I_upper

    I_lower = 0.0
    x_avg = sum(x) / len(x)
    for i in range(0, n):
        I_lower += (x[i] - x_avg) * (x[i] - x_avg)
    W = make_W(w)
    I_lower = I_lower * W
    return I_upper / I_lower

def make_E_I(x_dict):
    return -1.0/(len(x_dict)-1)

def make_Var_I(x_dict, w):
    def make_S1(w):
        r = 0.0
        n = len(w)
        for i in range(0, n):
            for j in range(0, n):
                r += (w[i][j] + w[j][i]) * (w[i][j] + w[j][i])
        r = r * 0.5
        return r
    def make_S2(w):
        r = 0.0
        n = len(w)
        for i in range(0, n):
            sum1 = 0.0
            for j in range(0, n):
                sum1 += w[i][j]
            sum2 = 0.0
            for j in range(0, n):
                sum2 += w[j][i]
            r += (sum1 + sum2) * (sum1 + sum2)
        return r
    def make_S3(x_dict, w):
        n = len(x_dict)
        x = [v for k, v in x_dict.items()]
        x_avg = sum(x) / len(x)
        r_upper = 0.0
        for i in range(0, n):
            r_upper += (x[i] - x_avg) ** 4
        r_upper = r_upper / n

        r_lower = 0.0
        for i in range(0, n):
            r_lower += (x[i] - x_avg) ** 2
        r_lower = r_lower / n
        r_lower = r_lower * r_lower
        return r_upper / r_lower
    def make_S4(w):
        r = 0.0
        n = len(w)
        S1 = make_S1(w)
        S2 = make_S2(w)
        r += (n**2 -3 * n + 3) * S1
        r -= n * S2
        sum1 = 0.0
        for i in range(0, n):
            for j in range(0, n):
                sum1 += w[i][j]
        sum1 = sum1 * sum1
        r += 3 * sum1
        return r
    def make_S5(w):
        S1 = make_S1(w)
        n = len(w)
        return (1 - 2 * n) * S1
    # ====================================
    S1 = make_S1(w)
    S2 = make_S2(w)
    S3 = make_S3(x_dict, w)
    S4 = make_S4(w)
    S5 = make_S5(w)
    n = len(x_dict)

    r_upper = 0.0
    r_upper = (n * S4) - S3 * S5

    r_lower = 0.0
    r_lower = (n - 1) * (n - 2) * (n - 3)
    w_sum = 0.0
    for i in range(0, n):
        for j in range(0, n):
            w_sum += w[i][j]
    r_lower = r_lower * r_lower
    return r_upper / r_lower

def evaluate_I(x_dict, x_neighbor_lst):
    w_matrix = make_w_matrix(x_dict, x_neighbor_lst)
    c_matrix = make_c_matrix(x_dict, w_matrix)
    I = make_I(x_dict, w_matrix, c_matrix)
    E_I = make_E_I(x_dict)
    Var_I = make_Var_I(x_dict, w_matrix)
    Std_I = Var_I ** 0.5
    # Z_score
    # Z_score 는 norm(0, 1)을 따르죠.
    # P(Z_score_I < Z):
    Z_score_I = (I - E_I) / Std_I
    print(f"I: {I}")
    print(f"z_score: {Z_score_I}")
    print(f"P({Z_score_I:.3f} < Z): {norm.cdf(Z_score_I, 0, 1):.2f}")
## Function Definition Done


x_dict = {'A': 10, 'B': 0, 'C': 0, 'D': 10}
x_neighbor_lst = [
    ('A', 'D'), ('B', 'C')
]
evaluate_I(x_dict, x_neighbor_lst)
# I: 1.0
# z_score: 0.5443310539518174
# P(0.544 < Z): 0.71
```
