---
title: Java - Array를 출력하기.
category: Java
tags: java programming array
---

## Java - Array를 어떻게 출력할 수 있나?

- 사실 아래 코드와 같이, 배열의 원소를 하나씩 출력하는 것은 어렵지 않습니다.
- 값을 하나씩 하나씩 출력하면 되죠.

```java
int[] intArr = {1, 2, 3, 4};

for (int i=0; i<intArr.length; i++) {
    System.out.println(intArr[i]);
}
```

- 그런데, 이 아이를 한번에 출력하면 어떻게 될까요?
- `{1, 2, 3, 4}`가 나와야 할 거라고 생각했지만, 사실은 `[I@f6f4d33`라는 이상한 값이 나옵니다. 이 값은 `intArr.toString()`과 동일하죠. 
- 구조를 보면, `[I`는 "Array of int"를 의미하는 것으로 보이고, `@`를 기준점으로 뒤쪽은 memorey address에 대한 HashCod로 보이네요(왜 메모리를 그냥 보여주지 않고, hascode를 보여주지? 싶지만, 메모리 주소를 알게 되면 리스키한 부분이 생기니까 일부러 가려서 보여주는 것이 아닐까, 싶습니다 홍홍).
- java는 "객체 지향 언어(object oriented language)"입니다. 따라서, `intArr` 또한 객체이고, 얘를 출력하게 되면 알아서 내부의 `.toString()`를 출력하게 되죠. 그리고 이 메소드는 기본적으로는 위에서 보여준 것과 같이, "메모리 주소값을 출력하는 것이 default"인 것이죠. 혹은 이 객체의 parentClass의 메소드가 그렇게 정의되어 있는 것이죠.
- 그리고 이 때, `toString()`의 default는 다음과 같이 3 부분으로 정의됩니다.
  - `intArr.getClass().getName()`: 해당 객체의 클래스 이름
  - `@`: 구분점
  - `Integer.toHexString(intArr.hashCode())`: 해당 객체의 주소값에 대한 hasCode를 HexString으로 변환한 값 

```java
int[] intArr = {1, 2, 3, 4};

System.out.println(intArr); // [I@f6f4d33
System.out.println(intArr.toString()); // [I@f6f4d33
System.out.println(intArr.getClass().getName() + "@" + Integer.toHexString(intArr.hashCode())); // [I@f6f4d33
```

### .toString()을 Overriding해주면 되는 것 아냐? 

- 앞서 말한 바와 같이, 결국 `.toString()`를 재정의해주면, 즉 Over-ridding해주면 끝나는 문제이기는 합니다.
- 하지만, 음, 이걸 어떻게 적용할 수 있을지 모르겠네요.
- 혹시 아시는 분 있으면 알려주세요.

### Arrays.toString() 을 사용하자

- `java.utils.Arrays` 클래스에는 java의 Array 활용시 유용하게 사용할 수 있는 다양한 static method들이 있습니다. static method이기 때문에, 객체를 생성하지 않아도 바로 사용할 수 있죠.
- `Arrays.toString()`를 사용하면 제 의도대로 결과를 출력할 수 있죠.

```java
import java.utils.Arrays; 

int[] intArr = {1, 2, 3, 4};
System.out.println(Arrays.toString(intArr)); // [1, 2, 3, 4]
```

---

## python의 경우 

- python은 그냥 출력하면 됩니다. 알아서 잘 출력해줘요.

```python
lst = [1, 2, 3]
print(lst)
```

## reference

- [stackoverflow - What's the simplest way to print a Java array?](https://stackoverflow.com/questions/409784/whats-the-simplest-way-to-print-a-java-array)
- [stackoverflow - why wont my array print out correctly](https://stackoverflow.com/questions/16217452/why-wont-my-array-print-out-correctly)
