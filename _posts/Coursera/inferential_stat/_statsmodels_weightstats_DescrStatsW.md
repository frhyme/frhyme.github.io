---
title: statsmodel - proportion confidence interval.
category: python-libs
tags: python python-libs coursera statsmodel confidence-interval 
---


class statsmodels.stats.weightstats.DescrStatsW(data, weights=None, ddof=0)[source]
descriptive statistics and tests with weights for case weights

Assumes that the data is 1d or 2d with (nobs, nvars) observations in rows, variables in columns, and that the same weight applies to each column.

If degrees of freedom correction is used, then weights should add up to the number of observations. ttest also assumes that the sum of weights corresponds to the sample size.

This is essentially the same as replicating each observations by its weight, if the weights are integers, often called case or frequency weights.

- 데이터가, 여러 차원이라고 할때, 이 데이터들에 대해서 각 칼럼별로 weight를 따로 
만약, degree of freedom이 적용된다고 하면, 이는 observation의 수에 따라서 적용되어야 하