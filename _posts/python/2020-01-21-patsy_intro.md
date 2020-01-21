---
title: python - patsy - overview. 
category: python-libs
tags: python python-libs patsy statistics statsmodels
---

## patsy: python package for describing statistical models.

- 요즘, 아는 후배가 물어봐서 conjoint 분석이라는 것을 조금 수행하고 있었습니다. 
- 특정 사용자 군을 대상으로 discrete choice model이라고 하는, 그냥 흔한 binary classification 모델을 만드는 것이라고 생각하면 됩니다만, 중요한 것은, neural network가 아니고, logistic regression만을 사용해야 한다는 것이죠. 
- linear model을 사용할 때의 강점은 interpretation입니다(logistic regression도 generalized linear regression에 속하죠). 각 변수가 결과에 어떤 영향을 미치는지를 명확하게 이해할 수 있다는 것은, 상대적으로 그 효과를 정확하게 알 수 없는 neural network에 비해서 강력하죠. 또한, "변수별로 어떤 분포를 가진다"를 주입하거나, "클래스별로 다른 분포 혹은 분산이 다르다"는 것을 주입하여, 각 parameter를 미세하게 수정할 수 있습니다. 
- 아무튼, 뭐 이건 중요하지 않구요. 이러한 선형적인 통계 모델을 세워서 다양한 가설을 검증하기 위해서, python에서는 `statsmodels`라는 통계 패키지를 사용할 수 있습니다. 그리고, 이 패키지를 사용할 때, 가장 간단한 선형방정식 Ordinary Least Square를 만든다고 한다면, 다음과 같이 표현할 수 있씁니다. 보면, 대충 무슨 말인지는 감이 오시죠?

```python
model = sm.OLS.from_formula(
    formula="Y ~ X1 + X2", 
    data=data_df
)
```

- 즉, `"Y ~ X1 + X2"` 형태로, formula를 넘겨서 모델을 구축할 수 있다면, 상대적으로 편하게 모델을 만들 수 있겠죠. 
- 반대로, 저 값을 일일이, 하나하나의 parameter로 넘겨야 한다면, 매우 귀찮아집니다. 즉, 이를 편하게 할 수 있는 library가 바로 [patsy](https://patsy.readthedocs.io/en/latest/quickstart.html)이며, 당연하지만, `statsmodels`등에서 이미 사용하고 있습니다.


## patsy: Overview 

- `patsy`는 statistical model(특히, linear model)을 묘사하기 위한 python package입니다. 특히, 이는 R, S와 같은 언어들에 내재된 formula language죠. 가령 `Y ~ x1 + x2`처럼, 선형적인 관계를 symbolic하게 표현하는 것을 말합니다. 
- building design matrices??? 
우선, `patsy`는 통계 패키지가 아니라, 앞서 말한 것처럼 R에서의 강력한 기능인 formula를 python에서도 쉽게 쓸 수 있도록 해주는, bridge와 가까운 언어라고 생각하시면 좋을 것 같아요. 즉 "통계 모델(특히, 선형 모델을 중심으로)을 구축하기 위한 high-level interface를 제공"한다, 라고 말하는게 좋아요. 
- 즉, 필요하다면, 직접 설치해서 쓸 수도 있지만, 그보다는 보통 `statsmodels`등을 설치할 때 의존성으로 딸려오니까, 굳이 이것만 따로 설치할 필요는 없을 것 같아요. 

## wrap-up

- 처음에는 `patsy`에 대한 다양한 사용법을 따로 정리하려고 했으나, 쓰고보니, 비교적 쓸게 없는 것 같아서, 간단하게 정리하고 말았습니다. 
- 그저, statsmodels에 내재되어 있는 라이브러리가 patsy이며, 만약 formula가 헷갈리면, 여기서 가져오면 된다, 정도로만 이해하고 이후에 formula가 나오면 검색하면서 진행하면 될것 같아요.

## reference

- [patsy - documentation](https://patsy.readthedocs.io/en/latest/R-comparison.html)