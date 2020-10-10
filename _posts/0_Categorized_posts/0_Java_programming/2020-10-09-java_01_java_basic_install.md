---
title: IntelliJ를 설치하고 Java를 간단하게 공부해봅니다.
category: Java
tags: java programming IntelliJ
---

## Install IntelliJ

- [IntelliJ](https://www.jetbrains.com/ko-kr/idea/)를 다운받아서 설치합니다. 참고로 말하면, 저는 맥을 사용하고 있습니다.
- 다운받고 설치하고 뭐 그런거는 보통 Next 버튼을 연타하면 되는 것이므로 넘어가겠습니다. 물론 고급 사용자의 경우 초기 설정을 변화하는 경우도 있지만 그건 이후 설정해도 되니까요.

## Jetbrains Academy

- 다만, 설치하다 보니 [JetBrains Academy](https://hyperskill.org/tracks)를 알려주네요.
- 처음 가입을 하게 되면 가입한 날부터 7일까지 무료로 사용할 수 있도록 해줍니다. 그리고, 친구를 초대하거나, 프로젝트를 완료하거나 하는 식으로 성취에 따라서 무료 사용기간을 연장할 수 있는 것으로 보입니다.
- Java, Kotlin, Python 등에 대해서 강의가 있군요. 다만, 모두 영어로 되어 있습니다. 요즘 느끼는데, 영어를 잘하면 접할 수 있는 교육 콘텐츠의 범위가 참 늘어나는 것 같아요. 사실 python이고 java고 떠나서 영어가 최고에요 그렇죠?
- 무료 사용기간이 모두 끝나면 한달에 25달러를 내거나, 1년에 50달러를 내거다 해서 사용할 수 있습니다만, 사실 Coursera나 YouTube, 그리고 수많은 블로그들에서 콘텐츠들이 많이 존재해서, 언젠가부터는 돈을 내는 게 미묘하게 아깝다는 생각이 들고는 합니다.
  - 이건 솔직한 제 생각입니다. 많은 사람들이 무엇인가를 배워야 할 때 취하는 전략은 "학원"을 다니는 것이죠. 그런데, 학원에서 가르치는 커리큘럼이 스스로에게 딱 맞기는 어려울 수 있습니다. 물론, 사람에 따라서는 어떤 커리큘럼을 다 따라간 다음에 새로운 것을 시작할 수 있는 사람도 있죠. 그런데, 장기적으로 개발을 하려고 생각한 다면, 학원보다는 스스로 질문하고 학습하는 습관을 들이는 것이 중요하다고 생각해요.
  - 개발을 공부한다는 것은 평생 사소한 질문부터 난관들 그리고 모르는 것들과 마주한다는 것을 의미합니다. 세상에 그 모든 것을 일일이 알려주는 학원 같은 것은 없어요. 개발자의 실력이 뛰어나 질수록 점점, 개발자가 필요로 하는 지식은 찾기 어려워집니다. 그렇다면 스스로 이런저런 지식들의 단편을 긁어 모아서 해결을 해야 하죠. 이 때 학원 같은 것은 필요하지 않습니다. 오히려 필요한 것은 스스로 질문을 던지고 인터넷을 통해 찾아서 지식을 재구축해나가는 과정이죠.
  - 저는, 그래서 개발 공부를 하고 싶다는 사람에게 항상 "일단 니가 궁금한 것은 인터넷에서 찾고 그 지식을 어딘가에 글로서 정리해봐라"라고 말합니다. 그리고 거기서 모르는 내용이 나온다면, 그걸 다음에 또 글로 쓰라고 말하죠. 그걸 무수히 반복하면, 가령 1년 동안 반복한다면 쌓이는 지식은 뭐 말하지 않아도 엄청나지겠죠. 뭐 그런겁니다. 저는 제 마음대로 이걸 "Curiosity-Driven Study"라고 부릅니다.
- 뭐 아무튼, 저는 일단 이 수업들을 순차적으로 따라가 보려고 합니다. 7일동안 빡세게 하려고요.

--- 

## Java

- Java는 오라클이 소유하고 있죠. 또한, JVM(Java 가상 머신) 위에서 돌아가기 때문에, 만들어진 코드는 어떤 환경 내에서도 문제없이 돌아간다, 라고 주장합니다. 이를 Write Once, Run Anyywhere, WORA 라고 말하고도 있죠. 다만, 제 경험상 JDK의 문제로 인해서 오류가 발생하는 일이 워낙 많기는 했는데, 뭐 일단은 넘어가도록 합니다.
- 그리고, 안드로이드의 등장 이후 어플리케이션의 주 개발 언어가 Java이기 때문에, Java는 더 인기를 끌었다고 할 수 있습니다. 물론, 요즘에는 Kotlin이 점차 그 점유율을 먹고 있기는 하지만, 아직까지는 한참 나중의 일이라고 봅니다.

### Garbage Collector

- Java는 C/C++과 달리 "메모리를 알아서 관리"합니다. 이를 Garbage Collector라고 말하죠.
- Garbage는 "값은 있는데 주소가 날아간 메모리"를 말합니다. 이를 간단히 코드로 보면 다음과 같습니다. 아래 코드 상에서 `a[2]`는 값이 있었지만, 값자기 사라지죠. 기술적으로 말하면 "메모리에 값이 저장되었는데, 이 메모리 주소가 없어짐"이라고 보는 것이 많습니다. 분명 `3`이라는 값이 어딘가에 저장되어 있기는 할텐데, 더 이상 부를 수 없죠. 이런 쓸데없는 메모리를 Garbage라고 부르고, 이를 잡아내고 비할당해주는 역할을 하는 아이가 바로 Garbage Collector입니다.

```python
a = [1, 2, 3]
a = [1, 2] # a[2]의 메모리 주소가 사라짐.
```

- 그리고 Java는 흔히 C/C++에는 Garbage Collector가 없어서, 메모리를 직접 관리해야 하죠. 이로 인해 발생하는 문제가 너무 많고, 그래서 Java가 더 낫다, 라는 주장을 펼칩니다.
- 그럴, 수도 있습니다만, 그냥 그렇게 결론을 내어서는 안됩니다. 여기서 우리가 가져야 하는 의문은 "왜 C는 Garbage Collector를 만들지 않았는가?"겠죠. 이는 다시 "Garbage Collector는 항상 좋은 것인가?"라는 질문으로 이어집니다.
- 2017년 8월 Instagram에는 [Dismissing Python Garbage Collection at Instagram](https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172#.koitdzt7n)이라는 글이 올라옵니다. 제목 그대로, Python의 GC를 해제했더니, Instagram의 속도가 10% 향상되었다는 이야기죠.
- 물론, 이는 python의 GC가 개구린 것 아니냐?라는 말을 의미하기도 합니다. 혹은 Instagram의 코드가 개구려서 Garbage Collector 알고리즘이 메모리를 제대로 못 해제한거 아니냐? 라는 말도 가능하겠죠.
- 제가 느리는 결론은 하나입니다. "Garbage Collector는 만능이 아니고, 비용이 발생한다"라는 것이죠. 생각해봅시다. 필요없어진 메모리를 알아서 해제해주려면, 어떤 프로세스가 외부에서 돌아가야겠죠. 비용이 발생하겠죠. 만약 메모리를 자주 많이 사용하고 해제한다면 GC가 관리해야 하는 메모리의 수가 증가하고, 당연히, 과부하가 걸리겠죠. 그럼 느려지겠죠? 쉬운 이야기입니다.
- 따라서, C의 경우는 그 부분조차 프로그래머의 역량으로 넘겨버린 것이겠죠. 누군가에게는 이 방법이 더 맞을지도 모릅니다.

--- 

## IntelliJ - NO SDK?

- IntelliJ에서 간단한 프로젝트를 만들고 코드를 실행해 보려고 합니다만, `No SDK`라는 말이 뜨네요.
- 하지만, 다행히도 해당 버튼을 누르니까, 알아서 설치할 수 있는 것 같습니다. 아유 편해.
- `Oracle OpenJDK 15`를 설치합니다. `OpenJDK`는 오라클이 상업적인 라이센스를 가지지 않는, 그냥 막 사용할 수 있는 Java라고 생각하시면 됩니다. 어떤 플러그인들은 없다고 하는데, 일단 저는 뭐 초보자니까 신경 안쓰고 진행해도 될 것 같아요.

## Basic Literal 

### Integer = 1_000_000

- 이건 처음 알았는데, 다음처럼 실행해도 알아서 잘 인식합니다. 그리고 해당 방식은 java뿐만 아니라, python에서도 동일하군요 오 처음 알았습니다.

```java
int a = 1_000_000; // 10^6
```

### Char and String 

- python에서는 `"aa"`와 `'aa'`에 차이가 없습니다. 쌍따옴표도 홑따옴표도 모두 문자열이 되거든요.
- 하지만, java에서는 홑따옴표는 `char`, 쌍따옴표는 `String`을 의미합니다.

```java

```

### Main Method 

- C에서도 `main`함수가 있는 것처럼 java도 마찬가지죠.
- 다만, C와 다른 것은 main 함수 자체도 하나의 Class 내에 정의되어 있다는 것이죠. 사실 처음에 java를 배울 때 익숙하지 않았던 것은 아마 이것 때문이었던 것 같아요. "아니 왜 main 함수 가 class 내에 있어?"라는 생각에 사로잡혀서 이해하지 못했던 것 같은데, 지금 생각해보니 왜 이해를 못했나 싶네요.

```java
public class Main {
    public static void main(String[] args) { 
        // { 앞에 Whitespace를 두는 것이 더 좋은 코드입니다.
        System.out.println("Hello World!!");
    }
}
```

### String

- c에서는 String을 지칭하는 타입이 따로 없고, `char[]`로 사용했던 같은데, 이게 array와 String의 구분이 좀 미묘해서 다른 사람들한테 설명해줄 때 헷갈리는 부분들이 있었던 것 같습니다.
- 반면 Java에서는 다음처럼 편하게 String을 정의해줄 수 있다는 것이 조금 더 좋은 것 같아요.

```java
String s1 = "abcd";
System.out.println(s1);
```

### Type Inference

- Java 10부터는 type을 정의하지 않고, `var`로 변수만 선언해주고, 이후 해당 변수에 들어오는 값에 따라서 해당 변수의 type을 정의해주는 방식도 가능합니다.

```java
public class Main {
    public static void main(String[] args) {
        var s1 = "abc";
        System.out.println(s1.getClass()); // class java.lang.String
    }
}
```

- 하지만 그렇다고 코드에서 type을 막 바꿀 수 있다는 이야기는 아닙니다. 
- 아래에서 보는 것처럼, 한번 값이 들어오면 type이 고정되고, 그 변수에 다른 값을 넣으려고 보면, 아래처럼 에러가 발생하죠.

```java
public class Main {
    public static void main(String[] args) {
        var s1 = "abc";
        System.out.println(s1.getClass()); // class java.lang.String
        s1 = 10; // ERROR > java: incompatible types: int cannot be converted to java.lang.String
        System.out.println(s1.getClass());
    }
}
```

- 자동으로 type을 추론해주는 것이 대세이기는 해서, java도 이를 수용한 것처럼 보이지만, 저는 딱히 좋은 방법이라고 생각하지는 않아요. 그건 java스러운 코딩이 아니라고 생각합니다.

### NamingConvention

- Java에서의 Naming Conventions은 대략 [geeksforgeeks - java naming conventions](https://www.geeksforgeeks.org/java-naming-conventions/)에 자세한 내용이 나와 있습니다.
  - Class, Interface: `CamelCase`, CamelCase and First Captial Letter. 
  - Method: `camelCase`, camelcase with First not Capital. 
  - Variable: `camelCase`, camelcase with First not Capital. 
  - Constant: `NOT_CAMEL_CASE`, all capital and underscore.
  - Package: `package`, all lower character.

---

## Wrap-up

- 사실 매우 기본적인 내용들을 정리했습니다.
- 뭐 워낙 초반이라서 쉽기는 하고 보통 이럴 때는 빠르게 넘어가지만, 저는 쉬운 거 다하면서 즐깁니다. 
- 쉬운 거 배우면서 "역시 나는 천재야!"라는 뽕을 맞는 걸 좋아하기 때문에 계속합니다. 호호호.
