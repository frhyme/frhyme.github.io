---
title: Java - for each 문
category: java
tags: java programming loop
---

## java - for each 

- java에서도 for each 문을 사용할 수 있습니다.

```java
String[] numStrs = {"1", "2", "3", "4", "5"}

// 아래와 같이 type varName: array, 형태로 작성되어야 합니다.
for(String num: numStrs) {
    System.out.printf("num %d\n", num);
}
```

- 별 거 아니잖아? 라고 생각할 수 있지만, 이러한 for each 문은 다음과 같이 iterable한 경우에 좀 더 유용하게 사용할 수 있습니다.

```java
String charArr = "ABCDEF"

// .toCharArray()를 통해 iterable한 형태를 만들고, 
// 값을 저장하지 않고, 임시로 쓴 다음 날려버릴 수 있음.
for (char x : charArr.toCharArray()) {
    System.out.println(x);
}
```

- 위처럼 하지 않으려면 다음처럼 새로운 변수를 만들어서 값을 저장해준 다음 처리해야 하죠. 다음처럼요.

```java
String str1 = "ABCDEF";
// str1과 같은 값을 charArr이라는 어레이에 넣어주어야 함. 메모리 낭비!
char[] charArr = str1.toCharArray();
for (int i=0; i < charArr.length; i++) {
    System.out.println(charArr[i]);
}
```

---

## python - for each 

- python의 경우 오히려 전통적인 for 문보다는 for each 문을 훨씬 많이 사용하는 편입니다.

```python
lst = ["a", "b", "c"]

# for each 문
for x in lst:
    print(x)
# for with i 
for i in range(0, len(lst)):
    print(lst[i])
```
