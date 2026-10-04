---
title: "javascript - for loop"
date: 2021-01-28
category: "javascript"
tags: ["javascript", "for", "loop"]
permalink: "/javascript/javascript04_for_loop/"
---

- javascript의 for loop를 사용하는 방법을 정리하였습니다

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