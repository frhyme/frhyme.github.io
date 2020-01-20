---
title: Fitting Statistical Models to Data with Python - WEEK 3 - part 3
category: python-libs
tags: python python-libs coursera statsmodels statistics
---

## Multilevel and marginal modeling, a case study with the NHANES data

- 데이터라는 것은, 사실 여러 관계를 가지고 있을 수 있습니다. 하나의 선형적인 관계만 가지는 것이 아니라, multi-level로 구성되어, `a ~ b`, `b ~ c`의 형태로 존재할 수 있다는 것이죠. 이러한 형태로 모델링하는 것이 보통 multi-level modeling입니다. 
- 그리고, 보통 이처럼 서로 내부적인 관계가 존재하게 되는 것은 그 데이터가 특정한 class 혹은 cluster에 포함되어 있기 때문이죠. 물론, 잘 설계된 실험에서는 타겟 그룹에 대해서 피실험자를 무작위로 선정하여, 선정된 데이터가 우리가 원하는 타겟 그룹을 정확히 대표할 수 있도록 조절하지만, 대부분의 데이터 수집에서는 이러한 부분이 충실하게 반영되어 있다고 하기 어렵습니다.
- 따라서 본 챕터에서는 NHANES의 데이터를 대상으로 클러스터를 반영하여 모델을 수립한다. cluster는 보통 피실험자의 개인적인 데이터(나이, 성별 등)에 기반하지만, 이러한 데이터들은 보통 개인정보이므로 숨겨진다. 대신 본 데이터에서는 `MVUs: "masked variance units"`가 존재하며, 이것이 실제로 존재하는 cluster가 된다. 

### Intraclass correlation

- 클러스터 내의 관측(observation)들간의 유사성은 보통 ICC(IntraClass Correlation)이라는 통계 값으로 측정된다. 보통 0과 1의 값을 가지며, pearson's correlation과는 구별되는 형태다.  
- ICC는 두 가지의 regression technique를 사용하여 평가하는데, 하나는 GEE를 이용한 Marginal regression, 두번째는 Mixed Linear Model을 사용한 Multi-level regression이 된다.
- 다음과 같이, 다양한 column에 대해서 class 내 값들의 관련성을 도출해본 결과는 다음과 같다. 

```python
################
# Assess ICC(Intra Class Cluster)
# GEE에 각 group에 따라 
print("== Assess ICC(IntraClass Cluster")
for col in ["BPXSY1", "RIDAGEYR", "BMXBMI", "smq", "SDMVSTRA"]:
    model = sm.GEE.from_formula(
        formula=f"{col} ~ 1", 
        groups="group",
        cov_struct=sm.cov_struct.Exchangeable(), 
        data=da
    )
    result = model.fit()
    print(f"{col} :: {result.cov_struct.summary()}")
print("=="*20)
```

- 특히, `SDMVSTRA`가 매우 높은 ICC값을 가지는 것을 알 수 있다. 나머지 값들도, 0.03이면 높은 편이며, range(-0.002 0.002)의 밖에 위치할 경우, 어느 정도 관련성이 높다, 라고 할 수 있다. 보통 pearson correlation에서는 값이 0.03 정도의 값이면 무시해도 된다고 생각하지만, ICC는 이정도 값이면 작지만, 무시하기는 어려운 값이된다. 

```
== Assess ICC(IntraClass Cluster
BPXSY1 :: The correlation between two observations in the same cluster is 0.030
RIDAGEYR :: The correlation between two observations in the same cluster is 0.035
BMXBMI :: The correlation between two observations in the same cluster is 0.039
smq :: The correlation between two observations in the same cluster is 0.026
SDMVSTRA :: The correlation between two observations in the same cluster is 0.959
```


## wrap-up

- 그 외로도 다양한 내용들이 있었다. 특히, GLM과 GEE를 사용할 때의 차이점, GLM을 명시적으로 데이터 내에 존재하는 dependence structure를 선언해야 하는 반면, GEE는 숨겨진 구조를 유추해가는 식으로 진행하므로, 그 데이터 내에 존재하는 관계들에 대해서 명확하지 않을때 사용하기 좋다는 것. marginal model이 GEE, multilevel-model이 Linear Mixed Model이라는 것.
- 그외로도 다양한 내용들이 있었으나, 이전에 배웠던 내용들과 개념적으로 크게 벗어나지 않는 것 같아서 우선 제외하였습니다.