---
title: jupyter notebook에서 warning 무시하기
category: python-lib
tags: python python-lib jupyter-notebook

---

## warning을 지웁시다. 

- jupyter notebook으로 작업하다보면(특히 `pandas`) 이런저런 warning이 뜹니다. 
- 물론 버그의 원인이 되므로 매우 중요하지만, 이걸 하나하나 다 고치다보면 진짜 복창이 터지거든요. 그래서 저는 종종 무시할때도 있습니다. 
- 아래 코드를 쓰시면 됩니다. 참 쉽죠? 

```python
import warnings
warnings.filterwarnings('ignore')
```