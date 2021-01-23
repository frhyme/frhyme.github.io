---
title: scala - Function 
category: scala
tags: scala programming function
---

## scala - Function 

- 간단히 다음처럼 `plus3`라는 function을 만들었습니다. 특이한 것이 java에는 `return`이 따로 없습니다.
- `functionName(inParamName: inParamType): outParamType`의 형태로 input type, output type을 뒤쪽에 `:`과 함께 작성해줍니다.

```scala
// S
object HelloWorld {
  // functionName(inParamName: inParamType): outParamType
  def plus3(x: Int): Int = {
    x + 3;
    // return x + 3; 으로 해줘도 상관없습니다.
  }
  def main(args: Array[String]) {
    println(plus3(1)); // 4
  }
}
```

- 그냥 다음처럼 한줄로 만들어서 처리할 수도 있죠.

```scala
def plus1(x: Int) = x + 1;
println(plus1(10));
```

- 여러 argument를 정의해줄 수도 있죠.

```scala
object HelloWorld {
  def multiply(x: Int, y: Int): Double = {
    return x * y;
  }
  def main(args: Array[String]) {
    println(multiply(3, 4));
  }
}
```
