---
title: Wide and Long data format
category: other
tags: data-format table
---

## Repeated Measures Data: Wide and Long

### wide format

- 가령, `Wide format: one row per subject`의 경우는 측정 회수와 상관없이, 같은 사람(subject)이라면, row에 고정하고, column을 늘리는 식으로 데이터를 저장하는 것을 말한다. 가령, row에 한 사람만을 두고, `나이에 따른 BMI`를 칼럼으로 둬서, `BMI_25`, `BMI_30`, `BMI_40`을 칼럼으로 만들었다면,

```
ID	Birth_state	BMI_25	BMI_30	BMI_40
1	OK	26	26	27
2	MI	23	22	28
3	FL	21	28	25
```

### long format

- 가령, `Long format: one row per measurement` 즉 측정마다 row를 만들기 때문에, `Age`라는 칼럼을 추가하여, 측정마다 row가 추가되는 식으로 정리된다.

```
ID	Birth_state	Age	BMI
1	OK	25	26
1	OK	30	26
1	OK	40	27
2	MI	25	23
2	MI	30	22
2	MI	40	28
3	FL	25	21
3	FL	30	28
3	FL	40	25
```

