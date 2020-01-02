---
title: plt.title의 위치 바꾸기. 
category: python-lib
tags: python-lib python matplotlib heatmap position title numpy seaborn pandas 
---

## title 위치 바꾸기 

- 다른 일에는 별 문제가 없는데, heatmap을 그릴때는 종종 문제가 됩니다. 특히 xtick을 위쪽으로 두면 다음 그림에서처럼 xtick과 title이 겹쳐서 보기 흉해져요. 

```python
import seaborn as sns 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

temp_df = pd.DataFrame(np.random.normal(0, 1, (10, 10)), 
                       columns= ["col{}".format(i) for i in range(0, 10)], 
                       index= ["idx{}".format(i) for i in range(0, 10)]
                      )
sns.heatmap(temp_df, cmap=plt.cm.rainbow, linewidths=10)
plt.tick_params(labelsize=13) 
plt.title(k, fontsize=15)
plt.gca().xaxis.tick_top(), plt.xticks(rotation=0), plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180813_plt_title.svg')
plt.show()
```

- 그림을 보면, title과 xtick이 겹쳐 있습니다. 

![](/assets/images/markdown_img/180813_plt_title.svg)

## set title position

- 간단하게 `plt.title()`에서 좌표를 넘겨주면 됩니다. 

```python
plt.title(k, 
          position=(0.5, 1.0+0.05), 
          fontsize=15)## title 위치 변경 
```

- 이렇게 아래 코드를 실행하면 그림에서 title이 예쁘게 잘 나오는 것을 알 수 있습니다. 

```python
temp_df = pd.DataFrame(np.random.normal(0, 1, (10, 10)), 
                       columns= ["col{}".format(i) for i in range(0, 10)], 
                       index= ["idx{}".format(i) for i in range(0, 10)]
                      )
plt.figure(figsize=(8, 6))
sns.heatmap(temp_df, cmap=plt.cm.rainbow, linewidths=10)
plt.tick_params(labelsize=13) 
plt.title(k, 
          position=(0.5, 1.0+0.05), 
          fontsize=15)## title 위치 변경 
plt.gca().xaxis.tick_top(), plt.xticks(rotation=0), plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180813_plt_better_title.svg')
plt.show()
```

![](/assets/images/markdown_img/180813_plt_better_title.svg)