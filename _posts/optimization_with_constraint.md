---
title:
category:
tags:
---

## constraint가 있을 경우에 optimization 방법

- 이전에는 constraint가 없는 상황에서, 비교적 간단하게 최적화를 했습니다. constraint가 없는 경우에는 그냥 그려진 objective function만을 미분하여 gradient descent로 진행해도 되는 거니까요. 
- 그러나 만약에 weight에 대해서 어떤 조건이 반드시 성립되어야 할 경우(뭐 w_1이 반드시 1보다 커야 하고, 합이 10이어야 하고 뭐 그런 것들)에는 같은 방식으로 접근할 수 없습니다. 이럴 때는 어떻게 진행하는 것이 좋을까요? 