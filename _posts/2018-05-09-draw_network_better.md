---
title: networkx와 matplotlib를 사용하여 graph를 예쁘게 그려 봅시다. 
category: python-lib
tags: python python-lib networkx matplotlib

---

## maplotlib를 사용하는 이유. 

- 이전 포스트에서는 `graphviz`를 사용하겠다고 했었습니다. 물론 이 것의 장점이 있기는 한데, 약간 범용적인 측면에서 생각해보면 결국 matplotlib로 돌아가게 됩니다(물론 process model을 표현하는데는 graphviz가 훨씬 좋습니다만). 
- python에서는 결국 그림을 그릴때 `matplotlib`를 중심으로 생각하게 되고, 특히 documnetation이 훨씬 많으니까요. 따라서, 다시 matplotlib를 활용해서 그림을 그려보려고 합니다. 
- 이후에 `networkx`의 documentation을 다시 보고 
- 지나치게 선이 구불구불해지는 면들이 있고, `layout`도 생각해보다 다양하지 않은 것 같습니다(물론 제가 모르는 것일 수도 있구요). 

## 