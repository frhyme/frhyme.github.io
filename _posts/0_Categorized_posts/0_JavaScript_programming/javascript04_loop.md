---
title: 
category: 
tags: 
---

```javascript
lst = ['A', 'B', 'C']
for(i=0; i < lst.length; i++) {
  console.log(lst[i])
}

// python에서는 for loop에서 x in lst로 처리하면 원소를 직접 가져오지만, 
// javascript에서는 index를 가져옵니다.
for(i in lst) {
  console.log(i)
}
```