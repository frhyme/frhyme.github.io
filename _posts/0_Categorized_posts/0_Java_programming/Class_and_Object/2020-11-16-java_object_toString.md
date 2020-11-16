---
title: Java - Overriding toString method
category: java
tags: java programming overriding String
---

## Java - Object - toString()

- Java에는 `Object`라고 하는 모든 Class의 BaseClass가 되는 Class가 존재합니다. 그리고 `.toString()`이라고 하는 method가 존재하죠. 
- class를 다음과 같이 정의합니다. 아무것도 정의되어 있지 않죠.

```java
package com.company;

class BaseClass {
    int id = 0;
    BaseClass (int id) {
        this.id = id;
    }
}
```

- 그리고 BaseClass Object에서 `toString()`을 실행하면 `com.company.BaseClass@23fc625e`라는 이상한 값이 나옵니다. 그냥 className과 className의 hashCode가 섞여 있는 값이죠.
- 그런데 사실 우리는, `toString()`을 실행했을 때, 이런 결과를 바란게 아니죠.

```java
class Main {
    public static void main(String[] args) throws Exception {
        BaseClass b1 = new BaseClass(1);
        System.out.println(b1.toString()); // com.company.BaseClass@23fc625e
    }
```

## Overriding toString method

- 따라서, class를 설계할 때, `toString()`을 Overriding해줍니다.

```java
package com.company;

class BaseClass {
    int id = 0;
    BaseClass (int id) {
        this.id = id;
    }
    @Override
    public String toString() {
        return "BaseClass_" + this.id;
    }
}
```
