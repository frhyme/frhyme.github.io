---
title: java - Array를 Reverse해보자
category: Java
tags: java programming array list reverse
---


## java - Array를 Reverse

- 코딩을 하다 보면, list 혹은 array에 들어 있는 값들의 순서를 역순으로 변경하고 싶을 때가 있습니다.
- 가령 python에서는 다음과 같죠. 참 쉽죠?

```python
lst1 = [1, 2, 3]
reversed(lst1) # [3, 2, 1]
```

- 물론, 그냥 코드 자체가 복잡하지 않아서, 그냥 다음처럼 짜버리면 되는 것이기는 합니다.

```java
int[] arr1 = {1, 2, 3, 4, 5, 6};
// array 내의 값들을 바꿔줌.
for( int i=0; i < (arr1.length/2); i++) {
    int temp = arr1[i];
    arr1[i] = arr1[arr1.length-i-1];
    arr1[arr1.length-i-1] = temp;
}
```

## Collections.reverse

- 물론, java에서도 `Collections.reverse`를 이용하면, 다음처럼 쉽게 reverse할 수 있기는 합니다.
- 하지만, 코드를 자세히 보면 조금씩 다른 부분이 있죠.   
  - array의 원소가 Int가 아닌 Integer로 되어 있다는 것.
  - array를 reverse해주는 것이 아니라, array를 `List<Integer>`로 변환한 다음 reverse를 해준다는 것.

```java
package com.company;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // array 원소의 type이 int가 아닌 Integer임
        // int는 primitive type이고 Integer는 Object
        Integer[] arr1 = {1, 2, 3, 4, 5, 6};
        // List와 같은 Container는 int와 같은 primitive type을 원소로 받아들이지 못함.
        List<Integer> lst1 = Arrays.asList(arr1);
        System.out.println(lst1); // [1, 2, 3, 4, 5, 6]
        // lst1의 원소를 역순으로 배치
        Collections.reverse(lst1);
        System.out.println(lst1); // [6, 5, 4, 3, 2, 1]
    }
}
// End of Code
```

- 그냥 `List<Integer>`를 `List<int>`로 바꾸면 되는 것 아닌가? 하는 생각이 들지만 그렇게 간단하지 않습니다. 그렇게 억지로 바꾸게 되면 다음과 같은 오류가 뜨거든요.

```plaintext
Type Argument cannot be of primitive type
```

## 왜 Container는 primitive type을 원소로 받지 않는가?

- 그렇다면 왜 java의 Container에서는 primitive type을 원소로 받지 않도록 설계된 것일까요?
- 간단하게 말하면, 우선 java의 Container는 원소의 주소를 관리하지, 값을 관리하지 않습니다. 하지만 primitive type은 보통 value type이고 value type으로 값을 받아들이게 되면, `Collections.reverse()`를 사용하게 되면 메모리에 들어 있는 값들을 다 바꾸어 줘야 합니다.
- 반대로, 주소만 가지고 있다면 그냥 현재 관리하고 있는 주소 테이블의 순서만 변경하면 되는 것이죠.
- 다만, 경우에 따라서 Auto-boxing을 해주는 경우도 있습니다. 프로그래밍에서 `boxing`은 primitive type을 object로 바꾸어주는 것, 반대로 `unboxing`은 object를 primitive class로 바꾸어주는 것을 말합니다. 아래 그림을 보면 더 명확할 것 같네요. 즉, 만약 `int`를 Container의 원소로 저장한다면 알아서 `Integer`로 변경해준다는 이야기인 것이죠.

![Java_boxing_unboxing](https://cdn.educba.com/academy/wp-content/uploads/2019/07/Autoboxing-and-Unboxing-in-Java.png)

- 다만, auto-boxing은 당연히 퍼포먼스 측면에서 문제가 발생하게 되고, 또 프로그래머 몰래 알아서 처리하는 것이 아니라, 컴파일러가 알아서 처리해주는 것이기 때문에, 별로 좋은 코드라고 생각되지 않습니다. 오히려 이런 경우에는 그냥 "에러"를 발생하게 해서 수정하도록 하는 것이 훨씬 이득이라고 생각되어요.

---

## Wrap-up

- python에서는 간단하게 변경할 수 있었던 것이, java로 오면 꽤 복잡해집니다.
- 뭐, 그래도 새롭게 배운 것들이 있긴 하네요.
