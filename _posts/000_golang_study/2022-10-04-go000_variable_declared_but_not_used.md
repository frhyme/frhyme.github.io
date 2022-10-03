---
title: go lang - variable declared but not used
category: golang
tags: go golang variable readability
---

## go lang - variable declared but not used

- golang에서는 code 내에 선언되었으나 사용되지 않은 package나 variable이 존재할 경우, error가 raise되며 코드가 실행되지 못합니다.
- 아래 코드를 작성한 다음 `go run main.go`를 사용해서 해당 코드를 실행해보면 `fmt` package, `a` variable들이 사용되지 않았기 때문에 에러가 발생하며 아래 코드가 정상적으로 컴파일 및 시행이 되지 못하는 것을 아실 수 있습니다.

```go
package main

import "fmt"
/*
"fmt" imported but not used
Compiler: UnusedImport
*/

func main() {
    var a int = 10
    /*
    a declared but not used
    Compiler UnusedVar
    */
}
```

### unused variable and readability

- [go - doc - effective go](https://go.dev/doc/effective_go)에 그 이유가 짤막하게 나와 있는데요. 대략 번역을 하자면, 다음과 같습니다.
- 사용하지 않는 package가 존재할 경우 프로그램 혹은 코드의 양이 팽창되고(bloat), 컴파일 속도가 늦춰집니다. 음, 이건 몹시 타당하죠. 하지만 python에서는 이런 경우 warning을 띄워주는 경우들이 있지, compile 혹은 interpreting이 되지 않도록 막지는 않습니다.
- 사용하지 않는 variable는 computing을 낭비하고, 큰 버그의 원인이 될 수 있습니다, 라고 하는데요. 쓸데없이 resource를 잡아먹는다는 것에는 동의를 하겠지만, 버그의 원인...은 명확하게 와닿지 않습니다. 사용되지 않았는데 어떻게 버그의 원인이 될 수 있을까요?

> It is an error to import a package or to declare a variable without using it. Unused imports bloat the program and slow compilation, while a variable that is initialized but not used is at least a wasted computation and perhaps indicative of a larger bug. When a program is under active development, however, unused imports and variables often arise and it can be annoying to delete them just to have the compilation proceed, only to have them be needed again later. The blank identifier provides a workaround.

- [stackoverflow - would lots of unnecessary variable cause performance issues in c#](https://stackoverflow.com/questions/9018602/would-lots-of-unnecessary-variables-cause-performance-issues-in-c)를 보면, "요즘 compiler는 똑똑하기 때문에 unused variable의 경우는 알아서 제거해준다"는 대답이 있습니다. 저도 그렇게 생각합니다. 요즘 컴파일러가 좋은데 굳이 unused variable을 사용하지 않도록 강제할 필요가 있을까요? warning으로 충분하다고 생각되는데요.
- [stackoverflow - why unused variable is such an issue?](https://softwareengineering.stackexchange.com/questions/340444/why-unused-variables-is-such-an-issue?newreg=0f89a7b773ad46a9ab3dbdd1874d6ed9)를 보면 "code 내에 unused variable이 존재하는 경우 코드의 가독성이 떨어진다. 만약 당신 코드를 담당할 newbie가 온 경우 당신이 무의미하게 만들어놓은 unsued variable을 해석하기 위해 많은 시간을 소요할 수 있다. 이 또한 일종의 performance 낭비로 생각될 수 있다", 라는 말이 정리되어 있습니다. 이 내용은 충분히 공감합니다.

### avoid unused variable error

- 그래도 테스트를 위해 임시로 사용하지 않는 변수를 포함시켜야 할 필요가 있다면, 다음과 같이 blank identifier(`-`)를 사용하면 됩니다.

```go
package main

import _ "fmt"
/*
"fmt" imported but not used
Compiler: UnusedImport
*/

func main() {
    var a int = 10
    _ = a
    /*
    a declared but not used
    Compiler UnusedVar
    */
}
```

### blank identifier

- blank identifier(`-`)는 unused variable로 인해 발생하는 error를 회피하기 위한 목적으로 보입니다. 가령, 다음과 같은 코드가 있을 때, variable `b`는 사용되지 않았기 때문에 error가 밣생합니다.

```go
package main

import "fmt"

func test_func() (int, int) {
    return 3, 4
}

func main() {
    a, b := test_func()
    /*
    b 는 unused variable이기 때문에
    compiler에서 error를 발생함.
    */

    fmt.Println(a)
}
```

- 따라서, 이런 경우 아래와 같이 코드를 변경해 주면 에러가 발생하지 않습니다.

```go
package main

import "fmt"

func test_func() (int, int) {
    return 3, 4
}

func main() {
    a, _ := test_func()
    /*
    b 는 unused variable이기 때문에
    compiler에서 error를 발생함.
    */

    fmt.Println(a)
}
```

## Wrap-up

- 결론적으로 말씀드리자면 저도 "code 내에 unused variable이 존재하면 안된다"라는 사실에는 절대적으로 동의합니다. golang에서는 아예 compile도 되지 않도록 만들어놓은 사실이 좀 놀라워서 배경을 좀 찾아봤습니다.
- compile 시간을 지연시키기는 하지만 크리티컬한 문제는 아닌 것으로 보이고, memory 사용량 측면에서도 큰 문제가 아니기는 하지만, 결국 "모든 variable은 사용되어야 한다"는 가정으로 인해 가독성을 현저히 떨어뜨릴 수 있기 때문에 사용하지 않는 변수는 모두 compile 전에 삭제해주는 것이 좋겠네요.
- 그러함에도 함수의 리턴 값 등으로 인해 사용되지 않는 변수가 정의된다면, blank identifier를 사용하여 일종의 예외처리를 해주는 것이 필요합니다.

## Reference

- [stackoverflow - how to avoid annoying error declared and not used](https://stackoverflow.com/questions/21743841/how-to-avoid-annoying-error-declared-and-not-used)
- [go - doc - effective go](https://go.dev/doc/effective_go)
- [geeksforgeeks - what is blank identifier underscore in golang](https://www.geeksforgeeks.org/what-is-blank-identifierunderscore-in-golang/)
