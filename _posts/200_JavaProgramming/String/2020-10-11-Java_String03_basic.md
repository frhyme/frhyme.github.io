---
title: Java - String 기본 method
category: Java
tags: Java String programming
---

## Java - String

- java에서 String은 Immutable하고(값을 한번 정하고 나면 수정할 수 없고), primitive type이 아닙니다.
- 배정할 값이 없다면, `null`을 넣어줍니다.

### Immutable

- java에서 String은 Immutabl합니다. 즉 한번 값을 지정했다면 그 값의 내부 원소를 수정할 수는 없다는 이야기죠.
- 물론, 아래처럼 변수에 들어 있는 값을 통째로 바꾸어주는 것이 가능하기는 한데, 엄밀히 따지면 이는 값을 수정했다기 보다, 원래 있던 값을 폐기하고 새로운 값을 지정했다고 보는게 맞겠죠.

```java
String s1 = "abc";
s1 = "def";
```

### Initialize 

- String을 초기화하는 방법은 다음 두 가지가 있습니다.

```java
String s1 = "abc";
String s1 = new String("abc"); 
```

### Return number of Character in String

- String의 길이는 `.length()` 메소드를 사용해서 가져올 수 있습니다.

```java
String s = "abc";
s.length() // 3
```

### Return char by its index

- `.charAt()` 메소드를 이용해서 String의 문자에 각각 접근할 수 있습니다.

```java
String s = "abc";
s.charAt(0) //'a'
s.charAt(1) //'b'
```

### Other Useful methods

- `.isEmpty()`: 해당 String이 비어있으면(`""`), true를 리턴합니다.
- `.isBlank()`: 해당 String이 비어있거나 공백(whitespace)만 있으면 true를 리턴합니다.
- `.toUpperCase()`, `.tolowerCase()`: String을 대문자, 소문자로 변환합니다.
- `.startsWith(prefix)`, `.endsWith(suffix)`: String이 prefix로 시작하는지, suffix로 끝나는지를 확인하여 true, fale를 리턴합니다.
- `.contains()`: String에 특정 string이 포함되어 있는지를 확인하여 true, false 를 리턴.
- `.substring(beginIndex, endIndex)`: String의 substring를 리턴
- `.trim()`: 앞뒤 공백(whitespace, tab, newline)을 삭제하고 리턴.
- `.replace(oldStr, newStr)`: String에 존재하는 oldStr을 모두 newStr로 변환하고 리턴.

### Concatenate

- String은 `+` 연산으로 두 String을 연결할 수도 있고, `.concat`를 이용해서 연결할 수도 있습니다.

```java
String s1 = "abc";
String s2 = "def";

System.out.println(s1 + s2);
System.out.println(s1.concat(s2));
```

- 다만, String과 다른 변수 타입, 가령 `int`, `Boolean`을 사용할 경우에도 아래처럼 알아서 String이 아닌 변수를 String으로 변환하여 String과 연결해줍니다.
  - 이 때는 각 변수에서 `.toString()`이라는 메소드를 사용하게 되죠.

```java
String s1 = "abc";
int a = 10;
Boolean tf = true;

s1 + a + tf // abc10true
```

### Equality Check

- java에서 String은 Interning을 통해서 관리됩니다. 즉, 새롭게 String을 만들었는데, 이 값이 이미 다른 변수에서 가지고 있는 값이라면, 그 값을 가르키도록 한다는 이야기죠.
- 따라서, 아래와 같은 코드에서 `s1`과 `s2`는 같은 메모리 공간을 가리킵니다. 그리고 java에서 String은 Interning을 하기 때문에, 같은 값이면 같은 메모리 공간을 가지게 되죠. 
- 여기서, String은 object type이므로 `==`나, `!=` 연산으로 비교하게 되면 값을 비교하는 것이 아니라, 메모리 주소를 비교하게 됩니다. 하지만, 앞서 말한 것처럼 String은 interning되어 관리되기 때문에, 그냥 주소를 비교해도 결과가 동일하게 나오죠.

```java
String s1 = "abc";
String s2 = "abc";

s1 == s2 // true
```

- 다만, 이는 `s1 = "abc"`과 같이 String Literal로 표현했을때이고, 아래와 같은 경우에는 false가 나오게 됩니다.
- `new String("abc")`로 새로운 String을 만든 경우에는 interning이 되지 않거든요. 
- 따라서, 이런 경우에는 `.equals()` 메소드를 사용해서 값을 비교해줍니다

```java
String s1 = "abc";
String s2 = new String("abc");

System.out.println(s1 == s2); // false
System.out.println(s1.equals(s2)); // true
```

---

## Wrap-up

- 기본전이 java string을 정리했습니다.
