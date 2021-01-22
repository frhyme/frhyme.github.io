---
title: Java - Variable used in lambda expression should be final or effectively final
category: java
tags: java final variable lambdaExpression
---

## Java - Variable used in lambda expression should be final or effectively final

- 가령 다음과 같은 코드가 있을 때, "Variable used in lambda expression should be final or effectively final"라는 오류가 발생합니다.
- "lambda expression에서 사용되는 변수는 final이거나, effecitvely final이어야 한다"라는 말이죠.
  - **final**: 변수를 선언할 때 `final`도 함께 선언되어 한번 값이 지정되면 바뀔 수 없는 것을 말함.
  - **effectively final**: `final`이 선언되지는 않았지만, 값이 바뀌지 않은 경우, 즉 컴파일러 단에서 해당 변수의 값이 한번도 바뀌지 않았다면 "애는 충분히 final이야"라고 분류해주는 것을 보이네요.
- 즉, lambda exrpression 내에서 외부에서 정의된 변수가 사용될 경우, 이 변수는 최소 effectively final이어야 한다는 말이죠.

```java
public class Main {
    public static void main(String[] args) throws Exception {
        for (int i=0; i < 10; i++) {
            // Variable used in lambda expression should be final or effectively final
            new Thread(
                () -> {
                    System.out.printf("Thread %03d\n", i);
                }
            );
        }
    }
}
```

## Why lambda expression needs effectively final? 

- local variable `i`는 main thread의 stack에 존재합니다. lambda expression에서 생성되는 thread는 main thread의 stack과 구분되죠. 따라서, 원래는 서로 다른 thread에서 변수에 접근할 수 없습니다. 또한, 만약 접근이 가능하다고 하더라, lambda expression이 있는 thread보다 main thread가 먼저 terminated되면, `i` 또한 자연히 stack에서 사라지므로, 접근이 불가능해집니다. 즉, 코드가 이상해지므로 이를 애초부터 막는 것이죠.
- 그런데 왜 되냐고요? 사실 이건 lambda expression에서 `i`를 복사해서 가져왔기 때문이죠. 즉 존재하는 값을 그대로 접근하는 것이 아니라, 외부에서 선언된 변수 `i`를 내부로 가져올 때 복사해서 가져옵니다. 이를 `Capturing Lambda`라고 합니다. 
- 그런데 그럼, "야 capturing lambda를 사용해서 복사해왔는데, 그럼 그냥 내부에서 막 바꿔도 되는거 아냐? 왜 final이어야 해?"라는 생각이 들 수 있습니다만, 복사해놓는 것은 마음대로 값을 변경하기 위한 목적이 아니라, 외부 stack에서 사라지는 것을 막고 내부에서 접근할 수 있도록 하기 위함입니다. 변경을 하지 못하도록 막은 것은 여러 thread에서 해당 변수가 사용될 때 sync를 맞추기가 어려워지기 때문이죠. 
- 자세한 건 [baeldung - java lambda effetively final local variables](https://www.baeldung.com/java-lambda-effectively-final-local-variables)에 나와 있습니다.

## Reference

- [baeldung - java lambda effetively final local variables](https://www.baeldung.com/java-lambda-effectively-final-local-variables)
- [자바 람다에서 final이거나 final처럼 쓰인 지역 변수만 접근할 수 있는 이유](https://jeong-pro.tistory.com/211)
