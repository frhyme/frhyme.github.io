---
title: matplotlib와 flask 연결하기 
category: python-lib
tags: python python-lib flask matplotlib image 
---

## matplotlib와 flask를 연결해보려고 합니다.

- 비교적 간단하게 할 수 있는거라고 생각했는데 잘 안되네요. 


## 이미지 캐시 삭제 


## macOS의 경우 발생하는 에러 

- 다음과 같은 오류가 발생하곤 합니다. 

```bash
Assertion failed: (NSViewIsCurrentlyBuildingLayerTreeForDisplay() != currentlyBuildingLayerTree), function NSViewSetCurrentlyBuildingLayerTreeForDisplay, file /BuildRoot/Library/Caches/com.apple.xbs/Sources/AppKit/AppKit-1561.40.112/AppKit.subproj/NSView.m, line 14485.
```

- 이유는 잘 모르겠지만, 비교적 간단하게 해결할 수 있습니다. 
- library를 임포트할 때 다음 순서에 맞춰서 해주시면 문제가 일단 해결됩니다. 

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
```