---
title: swift - chapter 5 - Control flow
category: swift
tags: swift tutorial
---

## swift - chapter 5 - Control flow

- `for`, `while`과 같은 loop를 위한 명령어들과, `if`를 사용하여 제어를 배웁니다. 사실 문법 조차 python과 유사하여, 따로 배울 것들은 없습니다.

### switch

- 다만, `switch`에서 조금 다른 부분들이 있습니다. `switch`는 if와 유사하게, 다양한 상황 변화를 표현하기 위한 명령어인데, C(그리고 Objective-C)에서는 다음과 같이 사용합니다. 물론 python에서는 switch 자체가 존재하지 않죠.
- 코드를 보시면 알겠지만, 모든 Case 다음에 break문이 들어간다는 것이 특이하죠. 만약 break를 넣지 않으면, default로 가서 default값을 실행하게 되죠.
- 저는, 이러한 형태가 직관적이지 않다고 생각하여 쓰지 않았습니다.

```c
char input= 'A';
switch(input){
    case 'A': 
        printf("input = A");
        break; // 모든 case 다음에 break가 들어간다는 것에 유의. 
    case 'B' : 
        printf("input = B");
        break;  
    default :    
        printf("input != A and != B");
}
```

- 하지만, swift에서는 `break`가 필요없습니다. 다음처럼 간소하게 표현해서 처리할 수 있죠. 
- 물론, `break`가 없다는 것을 제외하면 유별난 차이가 보이지는 않습니다만, 이것만으로도 `switch`를 사용해야할 이유는 늘어납니다. 
- `if`보다 `switch`는 특정 변수에 종속되어 있기 때문에, "특정 변수의 상황에 따른 제어"라는 목적에 충실한 명령어죠. 따라서, 훨씬 사용이 용이한 부분이 있습니다.

```swift
var s1:String = "Z"

switch s1{
case "A":
    print("This is A")
case "B":
    print("This is B")
default:
    print("This is default")
}
```
