---
title: Java - Explicit type arguments can be replaced by Diamond Operator?
category: java
tags: java programming 
---

## Java - Explicit type arguments can be replaced by Diamond Operator?

- Java에서 Collection을 사용하다 보변 다음과 같은 Warning 메세지가 뜰 때가 있습니다. 

```java
// Explicit type arguments can be replaced by Diamond Operator
Collection<Integer> rCollection = new ArrayList<Integer>();
```

- 뒤쪽의 `Integer`를 지워버리면 Warning이 발생하지 않죠. 물론 그대로 사용해도 문제는 없습니다만.
- 이 `<>`을 Diamond Operator라고 부르죠. 별 차이 없는것 같은데, 왜 이렇게 해야 하는걸까요?

```java
Collection<Integer> rCollection = new ArrayList<>();
```

## Make the code Simpler

- 우선 코드를 간단하게 만들기 위한 것이 목적입니다.
- 아래와 같은 코드를 보면, 매우 복잡합니다. 이러다보면 실수하기가 쉬워요. 사실 왼쪽에 이미 충분한 정보가 있는데 오른쪽에 정보가 중복으로 있는 셈이죠.

```java
List<Map<String, List<String>>> complexMap = new ArrayList<Map<String, List<String>>>();
```

- 복잡한 구조를 다 없애 버리고 오른 쪽에는 Diamon Operator인 `<>`만 툭 두면 됩니다. 그럼 위의 코드와 동일한 결과가 나옵니다.

```java
List<Map<String, List<String>>> complexMap = new ArrayList<>();
```

## Reference

- [Stackoverflow - What is the point of the diamon operator in java](https://stackoverflow.com/questions/4166966/what-is-the-point-of-the-diamond-operator-in-java-7)
- [Stackoverflow - Why explicit type argument should be replaced by diamond](https://stackoverflow.com/questions/33137417/why-explicit-type-argument-should-be-replaced-by-diamond)
