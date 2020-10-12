---
title: Java - Array의 모든 원소가 같은지 확인하기
category: Java
tags: java programming array equality 
---

## Java의 두 Array의 모든 원소가 같은지 확인해봅시다

- 간단합니다. 두 Array `intArr1`, `intArr2`가 있을 때 내부의 모든 원소가 같은지를 확인해봅시다.
- 첫번째로는 아래 코드와 같이 모든 원소를 다 확인해주는 방법이 있겠죠.

```java
int[] intArr1 = {1, 2, 3, 4};
int[] intArr2 = {1, 2, 3, 4};

// Method1: 값을 하나하나 다 확인하기.
boolean isSame = true;
for (int i=0; i<intArr1.length; i++) {
    if (intArr1[i]!= intArr2[i]) {
        isSame = false;
        break;
    } else {
        continue;
    }
}
System.out.println("Method1: arr Same? " + isSame);
```

- 두번째로는 `Arrays.equals(intArr1, intArr2)`를 사용해서 한번에 확인하는 방법이 있죠.

```java
int[] intArr1 = {1, 2, 3, 4};
int[] intArr2 = {1, 2, 3, 4};

// Method2: 한번에 확인
System.out.println("Method2: arr Same? " + Arrays.equals(intArr1, intArr2));
```

## wrap-up

- 간단합니다. 다만, 요즘에는 너무 라이브러리들이 넘쳐나서, 두번째 방법을 늘 사용합니다. 
- 다만, 이게 참 간단한 코드인데도, 맨날 2번째 방법만 쓰다보니, 가끔은 첫번째 알고리즘도 잘 떠오르지가 않더라고요.
- 가능하면, 간단한 코드라도 내부가 어떻게 돌아가는지 확인해보는 습관이 필요한 것 같ㅅ브니다.
