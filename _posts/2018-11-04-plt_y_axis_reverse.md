---
title: plt에서 y 축 reverse하기 
category: python-libs
tags: python python-libs plt reverse axis
---

## y 축을 왜 반대로 해야 하나 

- 어떤 값에 의한 순위 변화를 그려야 한다고 하면, y축의 값이 작을수록 위로 위치하도록 만들어야 합니다. 
- 이러려면 y축을 반대로 변경해야 하죠. 
- 늘 그렇지만, [이미 스택오버플로우에 비슷한 내용이 있습니다](https://stackoverflow.com/questions/2051744/reverse-y-axis-in-pyplot). 

```python
plt.gca().invert_yaxis()
```



