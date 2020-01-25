---
title: Inferential Statistical Analysis with Python - WEEK 2
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## WEEK 3 - Statistical Inference with Confidence Intervals

- 2주차에서는 주로 Confidence interval을 배웠으며, 어떻게 계산하고 해석하는지, 그리고 Confidence라는 것이 의미하는 것은 무엇인지 등에 대해서 배우게 됩니다. 
- 이를 위해서는 우선 '모집단'과 '표본집단'에 대한 이해가 필수적입니다. 가령, '한국의 남성들의 키 평균'을 알고 싶다고 한다면, 여기서, '한국의 남성'이 모집단이 되죠. 돈이 충분하다면 우리가 전수조사를 할 수 있지만, 우리는 늘 그렇지 않습니다. 따라서, 우리는 필요한 표본들, N이라는 값을 가져와서 '평균'이라는 parameter를 예측하게 되죠. 
- 그런데, 여기서 이 '평균'이라는 값이 얼마나 정확할까요? 얼마나 정확하다고 할 수 있을까요? 너무 당연하지만, N이 1일때의 정확도가 N이 10일 때의 정확도, 그리고 N이 100일 때의 정확도는 모두 다릅니다. 
- 또 나아가서, 이 '평균'이라는 것도 결국은 변수일 뿐입니다. 수집된 남성들은 모두 모집단의 분포를 따르는 랜덤 변수들이며, 랜덤 변수들을 N개 합하여 만들어진 새로운 랜덤변수가 바로 'N명의 남성들의 키 평균'이라는 변수죠. 즉, 이 아이조차도 어떤 특정한 분포를 따르게 됩니다. 이 때의 분포는 보통 [스튜던트-T 분포](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%8A%9C%EB%8D%98%ED%8A%B8_t_%EB%B6%84%ED%8F%AC)라고 가정하죠. 
- 이 '평균'이라는 랜덤변수가 가지는 스튜던트 T 분포를 기반으로 90%의 확률로 어느 정도 구간에 위치하는가, 95%의 확률로 어느 구간에 위치하는가, 를 말하고 있는 것이 바로 신뢰 구간, confidence Interval입니다. 
- 그리고, 이 분포는 degree of freedom, 즉 N명에 대해서 샘플을 수집하였는가? 에 따라서 그 분포의 모수가 달라집니다(정확히는 N-1이 degree of freedom입니다). 이 모수는 [Table_of_selected_values](https://en.wikipedia.org/wiki/Student%27s_t-distribution#Table_of_selected_values)를 통해서 확인할 수 있습니다. 또한, 통상적으로는 그냥, N이 충분하다고 가정하고, 95%의 구간에 대해서는 1.96, 99%의 구간에 대해서는 2.58이라고 외웁니다. 이렇게 쓰고 보니, 고등학교 수학같군요.
- 다만, 이렇게 쓰고 나면, t-분포의 매개변수는 마치, degree of freedom 뿐이라고 생각하기 쉽습니다만, 그렇지 않습니다. t-분포는 정규 분포를 기본 base로 활용하며, 여기에 degree of freedom에 따라서 그 분포가 조금씩 달라지는 형태에 가깝죠. 즉, t-분포의 매개변수는, 정규분포의 평균, 분산 그리고 degree of freedom까지 필요하다는 이야기입니다. 
- degree of freedom을 참고하여, t-multiplier 즉 테이블에서 정의된 신뢰구간에 대한 값을 파악하고, 표본 집단의 평균과 표본 집단의 분산을 파악해서 신뢰구간을 정확하게 계산해줘야 합니다.

## Calculate Confidence Interval. 

- week2에서는 population proportion에 대해서 추정하고, 신뢰구간을 파악합니다. 
- 추정하려는 값의 평균은 p(population proportion)이고, 분산은 p(1-p)가 됩니다(각각, np/n, npq/n)이라고 생각하시면 단순하죠). 그러나, 이는 모집단에 대한 평균과 분산이죠. 표본집단에 대한 분산은 `p(1-p) 나누기 N`이 됩니다. 그리고, 표준 오차 standard error를 계산하려면 루트를 씌우고요.
- 간단하게 python을 사용해서 계산하면 다음과 같습니다.

### Calc by numpy. 

```python
import numpy as np

# degree of freedom이 매우 크다고 가정하고, 
# two-sided로 95%의 신뢰구간을 가질 때, t 분포의 
tstar = 1.96 
sample_proportion = .85
N = 659

se = np.sqrt((sample_proportion * (1 - sample_proportion))/N)
print(f"Standard Error for Population Proportion: {se:.6f}")
lower_confidence_boundary = p - tstar*se
upper_confidence_boundary = p + tstar*se
print(f"lower_confidence_boundary: {lower_confidence_boundary}")
print(f"upper_confidence_boundary: {upper_confidence_boundary}")
```

```
Standard Error for Population Proportion: 0.013910
lower_confidence_boundary: 0.8227373256215749
upper_confidence_boundary: 0.8772626743784251
```

### Calc by statsmodels.

- 그리고, `statsmodels`를 사용하면, 다음과 같은 결과가 나오며, 위의 계산 값과 동일하죠.

```python
import statsmodels.api as sm

ci_low, ci_upp = sm.stats.proportion_confint(
    count = n*p, # number of success
    nobs = n, # number observations
    alpha = 0.05, # significance level
    method='normal' # default
)
print(f"n: {n}")
print(f"p: {p}")
print(f"Confidence interval low: {ci_low}")
print(f"Confidence interval upp: {ci_upp}")
```

- 결과는 다음과 같습니다. 

```
n: 1000
p: 0.85
Confidence interval low: 0.8278688906821529
Confidence interval upp: 0.8721311093178471
```

## Confidence Intervals for Differences between Population Parameters

### 복습. 

- 이전에는 하나의 population에 대해서 추정한 proportion의 신뢰구간을 추정했습니다. 
- 모집단의 분포를 가진 N개의 표본 집단을 뽑아서, 표본집단의 평균이라는 랜덤 변수를 만들었죠. 그리고 이 랜덤 변수는 normali dist에 기반한 스튜어트 t 분포를 가집니다(이 아이는 노멀 분포의 평균/분산과 degree of freedom을 통해 정의되죠). 
- 그리고, 이 분포에 대해서, 평균이 일정 신뢰 구간(confidence interval)에 속하는지를 그 구간을 도출합니다. 

### 돌아와서.

- 이제, 서로 다른 표본 집단 둘에서 가져온 `p1`과 `p2`간의 차이가, 어떤 구간에 존재하는지를 파악해봅시다. 즉, `p1 - p2`라는 랜덤 변수가 어떤 구간에 위치하는지를 본다는 이야기죠. 
- 우선, 두 비율 모두 `N1`, `N2`가 매우 크다고 가정합니다(즉 degree of freedom이 매우 크다는 말죠). 따라서 거의 normal distribution과 유사한 형태를 가지게 되죠. 따라서, 95%의 confidence interval을 파악한다면, 양쪽에 1.96을 곱해주면 되는 것이죠. 그리고, 각각의 랜덤변수는  `norm(p, sqrt(p1 * (1-p1) / N1))`을 따릅니다. 
- 그리고, 새로운 랜덤변수인 `p1-p2`는 평균은 `mean(p1) - mean(p2)`이며, 표준편차는 `sqrt(std(p1)**2 + std(p2)**2)`가 됩니다. 이건, 아주 기본적인 수식이므로 더 설명하지 않아도 될것 같습니다.
- 따라서, 이를 계산해보면 다음과 같죠. 


```python
import numpy as np 
print("=="*20)
# 집단1의 랜덤변수, p1, N1, 
p1 = .304845
N1 = 2972
std_error1 = np.sqrt(p1 * (1 - p1)/N1)
print(f"std_error1: {std_error1}")

# 집단2의 랜덤변수, p2, N2, std_error2
p2 = .513258
N2 = 2753
std_error2 = np.sqrt(p2 * (1 - p2)/ N2)
print(f"std_error2: {std_error2}")
print("=="*20)

# p_diff 라는 새로운 랜덤변수는 다음과 같은 평균과 분산을 가지며 
# N이 충분히 많으므로 normal distribution을 따른다고 할 수 있다.
p_diff_average = p1 - p2
diff_std_error = np.sqrt(std_error1**2 + std_error2**2)
print(f"p_diff_average: {p_diff_average}")
print(f"diff_std_error: {diff_std_error}")
lcb = p_diff_average - 1.96 * diff_std_error
ucb = p_diff_average + 1.96 * diff_std_error
print(f"lcb: {lcb}")
print(f"ucb: {ucb}")
print("=="*20)
```

```
========================================
std_error1: 0.00844415041930423
std_error2: 0.009526078787008965
========================================
p_diff_average: -0.20841300000000001
diff_std_error: 0.012729880335656654
lcb: -0.23336356545788706
ucb: -0.18346243454211297
========================================
```

## wrap-up

- 내용은 좀 더 많았지만, python을 활용해서 confidence interval을 계산하는 방법을 중심으로 정리하였습니다. 분명히 모두 학부때 배운 내용들이고(심지어 몇몇은 고등학교 때 배운 내용임에도 헷갈리는 부분들이 있더군요).
- 결국 중요한 것은 샘플링한 값들도 결국 특정한 분포를 따르는 랜덤 변수인 것이고, 이 랜덤 변수들을 더한 '평균'과 같은 값도 결국은 랜덤 변수인 것이죠. 따라서, 모집단이 정규 분포를 따르고, 이로부터 N개의 샘플링을 통해 꺼낸 평균도 특정한 분포(스튜어트 t 분포)를 따르게 되죠. 이 분포에 따라서, 만약 99%의 가능성으로 본다면 어느 정도 구간에 존재한다고 할 수 있는지, 이를 말하는 것이 신뢰구간이라는 것입니다. 즉, 최소한 이 구간에는 99%의 가능성으로, 같은 작업을 반복하더라도 여기에 존재할 것이다, 라는 것이죠.