---
title: python - statsmodels - GEE
category: python-libs
tags: GLM statistics GEE
---

## Generalized Estimating Equation.

- Generalized Estimating Equation, GEE는 Data 내에서 서로 보다 밀접한 그룹이 형성되어 있거나(가령, 남성/여성 과 같은 그룹이 존재하여, 서로 다른 분포를 가진다거나) 시간에 따라서 분산의 정도가 커진다거나, 관측치 간에 서로 관련성이 있거나(시간과 연결되어 있어, "이전 데이터"와 밀접하게 관련되는 자기 상관성 등을 가진다거나) 할때, 이러한 차이를 반영한 모델을 구축하기 위해서 사용됩니다. 
- 

## how to use it.

- `statsmodels`의 
- statsmodels.genmod.generalized_estimating_equations.GEE
class statsmodels.genmod.generalized_estimating_equations.GEE(endog, exog, groups, time=None, family=None, cov_struct=None, missing='none', offset=None, exposure=None, dep_data=None, constraint=None, update_dep=True, **kwargs)[source]
Estimation of marginal regression models using Generalized Estimating Equations (GEE).

GEE can be used to fit Generalized Linear Models (GLMs) when the data have a grouped structure, and the observations are possibly correlated within groups but not between groups.

Parameters:	
endog : array-like

1d array of endogenous values (i.e. responses, outcomes, dependent variables, or ‘Y’ values).

exog : array-like

2d array of exogeneous values (i.e. covariates, predictors, independent variables, regressors, or ‘X’ values). A nobs x k array where nobs is the number of observations and k is the number of regressors. An intercept is not included by default and should be added by the user. See statsmodels.tools.add_constant.

groups : array-like

A 1d array of length nobs containing the group labels.

time : array-like

A 2d array of time (or other index) values, used by some dependence structures to define similarity relationships among observations within a cluster.

family : family class instance

The default is Gaussian. To specify the binomial distribution use family=sm.family.Binomial(). Each family can take a link instance as an argument. See statsmodels.family.family for more information.

cov_struct : CovStruct class instance

The default is Independence. To specify an exchangeable structure use cov_struct = Exchangeable(). See statsmodels.genmod.cov_struct.CovStruct for more information.

offset : array-like

An offset to be included in the fit. If provided, must be an array whose length is the number of rows in exog.

dep_data : array-like

Additional data passed to the dependence structure.

constraint : (ndarray, ndarray)

If provided, the constraint is a tuple (L, R) such that the model parameters are estimated under the constraint L * param = R, where L is a q x p matrix and R is a q-dimensional vector. If constraint is provided, a score test is performed to compare the constrained model to the unconstrained model.

update_dep : bool

If true, the dependence parameters are optimized, otherwise they are held fixed at their starting values.

missing : str

Available options are ‘none’, ‘drop’, and ‘raise’. If ‘none’, no nan checking is done. If ‘drop’, any observations with nans are dropped. If ‘raise’, an error is raised. Default is ‘none.’