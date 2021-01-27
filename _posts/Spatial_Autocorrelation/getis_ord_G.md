

## Getis Ord G

- 

## Scratch 

- Moran's Index는 "Spatial Autocorrelation"을 측정하는 수치.
- 구역별로 완전한 randomness를 가진다는 것을 null Hypothesis로 두고 그렇지 않을 가능성을 통계적 방법을 통해 검정하는 testing방법으로 보입니다.
- 이 때, 완전한 무작위성을 CSR(Complete Spatial Randomness)라고 하고, Moran's Index는 현재의 공간이 CSR에서 얼마나 벗어나 있는지를 의미하죠. 
  - Moran's Index는 1에 가까울수록 내부에 군집이 존재한다고 봅니다. 
  - 0에 가까우면 CSR이 되고(엄밀히 따지면 -1(n-1)). 이 null hypothesis가 되면, 0에 가까운 상태를 가정하고 테스팅을 하게 됨.
  - -1에 가까우면, 지나치게 퍼져 있는, 가령 체스판 같은 형태로 값이 존재한다는 의미가 되죠. 
  - 각 구역별로 Weight 값이 존재합니다. 이 Weight는 각 구역의 특성이자, 인접한 공간과 영향을 가질 것으로 생각되는 값이 됩니다. 가령, '해당 구역의 도시 인구 수'라는 값을 Weight로 둔다면, 해당 구역의 인구 수가 인접한 구역에 영향을 줄 것이다, 라고 본다는 것이죠. 
    - 인접한 두 구역 A, B가 있다고 합시다. 그리고 전체 구역의 평균을 m이라고 하죠. 
    - 전체 평균으로 A, B의 값을 표준화하게 되는데 만약 A, B가 모두 평균보다 크다면 표준화된 값은 둘다 양수, 평균보다 작다면 둘다 음수가 되죠. 그리고 인접한 값을 곱하면 양수가 됩니다. 하나는 양수, 하나는 음수가 된다면 음수가 됩니다.
    - 그리고 그 값이 평균에서 멀어질 수록 그 절대값은 커지게 되죠.
    - 이런 수치들을 이용해서 분포를 측정하고 검정 값인 Z_value를 찾습니다.


### 공간가중치

- w_ij는 두 구역간이 서로 인접하다고 판단되면 1 아니면 0을 정의합니다.
- 인접방식을 따지는 방법은 여러 방식이 있습니다.
  - 룩 방식: 상하좌우만 서로 인접하다고 평가하는 방식 
  - 퀸 방식: 상하좌우 대각선이 인접하다고 평가하는 방식
- 그 외에도 각 row의 합이 1이 되도록 표준화한다거나, 거리를 고려하여 계산한다거나 하는 다양한 방법이 있음 

### 계산법 

- 슈도 코드로 대략 이런 느낌인 듯 

```python
I = 0 # Moran's index
N # 구역들 개수 
w_ij # 구역i부터 구역j까지의 공간가중치
W # 공간가중치 W_ij 의 총합 
x_avg # x의 평균 
c_ij # (x_i - x_avg) * (x_j - x_avg)

I_upper = 0 # I의 분자 
for i in range(0, N): 
    for j in range(0, N):
        if i != j: 
            c_ij = (x_i - x_avg) * (x_j - x_avg)
            I_upper += w_ij * c_ij
        else: 
            continue
I_upper = I_upper * N

I_lower = 0 # I의 분모 
for i in range(0, N): 
    I_lower += (x_i - x_avg) * (x_i - x_avg)
W = 0
for i in range(0, N): 
    for j in range(0, N):
        if i != j: 
            W += w_ij
        else:
            continue
I_lower = I_lower * W

I = I_upper / I_lower
```

- 만약, X가 random한 집단에서 임의로 추출된 집단이라면 다음 분포를 따라야 함.
  - `E(I)`: `-1/(N - 1)`
  - `Var(I)`: ...복잡함. 
  - z-value: (I - E(I)) / (sqrt(Var(I)))

## Example

```python

```

## Issues

- Getis Ord G
- Hot zone, Cold zone