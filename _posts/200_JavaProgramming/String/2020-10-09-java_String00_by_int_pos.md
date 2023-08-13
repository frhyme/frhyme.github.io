---
title: Java - 문자열 정수 index를 사용해서 접근
category: Java
tags: java programming IntelliJ String
---

## String access by index

- 가령, python에서는 문자열(String)의 정수 위치에 따라서 값을 접근할 때, 다음과 같이 합니다.

```python
s1 = "abc"
s1[0] // 'a'
```

- 그런데, java에서는 String의 각 캐릭터에 접근하려면 이렇게 하면 안되고, `.charAt(int index)`를 사용해야 합니다. 

```java 
int digitStr = "456";

// 0번째에 있는 char 값을 리턴
digitStr.charAt(0) // 4
```

- 혹은 String을 CharArray로 변환한 다음 접근해도 되기는 합니다.

```java 
int digitStr = "456";

// digitStr을 CharArray로 변환한 다음, 0번째에 있는 값에 접근
digitStr.toCharArray()[0]; // 4
```

- python이나, C에서는 그냥 `[integer_pos]`와 같은 방식으로 그냥 접근하면 되었던데에 반해서, java는 조금은 귀찮기는 하죠.
- 이유가 있을텐데, 아직 못 찾았습니다. 다음에 알아보겠습니다 호호.
