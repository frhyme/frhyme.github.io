---
title: Java - Collections
category: java
tags: java programming collections GenericProgramming
---

## Java - Collections

- Java에서 기본으로 제공하는 Array의 경우 사용할 수 있는 Array의 크기가 고정되어 있죠. 그런데 실제 상황에서는 필요에 따라 Array의 크기가 추가로 더 필요할 때가 있죠. 물론, 어려운 코드는 아닙니다. 더 큰 크기의 New Array를 만들고, 기존 Array의 원소들을 모두 복사하여 New Array에 넣어주면 되죠. 물론 그저 귀찮을 뿐입니다. 
- 당연하지만, 그래서 Java에는 Collections 라는 라이브러리가 있습니다. 얘는 크기가 고정되어 있지 않은 Array(Dynamic Array)이며, 얘는 Class이기 때문에, 매우 다양한 종류의 method를 지원합니다. 그리고 당연하지만, 그래서 그냥 Array에 비해서 속도가 느리겠죠. 또한 Generic type이기 때문에, 어떤 타입에 대해서도 Array를 만들 수 있죠.
- Java Standard Library에 이런 다양한 종류의 Collection들이 있지만, 만약 충분하지 못할 경우 [Guava: Google Core Libraries for Java](https://github.com/google/guava)를 사용할 수도 있습니다.

## Java - ArrayList

- `ArrayList`를 사용해서 간단한 코드를 작성해봤습니다.

```java
// import java.util.ArrayList;
// default로 import되기 떄문에 굳이 쓰지 않아도 문제는 없습니다.

class Main {
    public static void main(String[] args) throws Exception {
        // ArrayList<T> 자체가 Class이기 때문에, 생성자를 call해야 합니다.
        // ArrayList<T>(initialCapacity)를 Call하며,
        // initialCapacity에는 초기에 잡아주는 ArrayList의 크기가 잡히죠.
        ArrayList<String> strArr = new ArrayList<String>(10);
        System.out.printf("strArr Size: %d\n", strArr.size());
        // ADD something
        strArr.add("a");
        strArr.add("b");
        strArr.add("c");
        strArr.add("d");
        // ADD with ArrayList
        // Array를 바로 넣어줄 수 없기 때문에, List로 변경한 다음 넣어줍니다.
        strArr.addAll(Arrays.asList(new String[]{"e", "f"}));
        System.out.println(strArr);
        // REMOVE by INDEX
        strArr.remove(0);
        // REMOVE by VALUE
        strArr.remove("c");
        System.out.println(strArr);
        // Get by INDEX: [0] 으로 접근할 수 없습니다.
        System.out.println(strArr.get(0));

        // for-each를 사용하여 print
        for(String eachStr : strArr) {
            System.out.println(eachStr);
        }
    }
}
```
