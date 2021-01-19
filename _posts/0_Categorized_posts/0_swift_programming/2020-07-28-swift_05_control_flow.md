---
title: swift - chapter 5 - Control flow
category: swift
tags: swift tutorial switch
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

- 또한, 다음처럼, 한번의 케이스에 n개를 묶어서 처리할 수도 있습니다.

```swift
var s1:String = "Z"

switch s1{
case "A", "a":
    print("This is A or a")
default:
    print("This is not A neither a")
}
```

- 그리고, 다음처럼 일정 범위에 대해서 처리할 수도 있죠. 다만, 이 부분이 `float`형태의 변수들에 적용되는 것은 아닙니다. 해당 범위에 속하는 Integer에 대해서만 허용되죠.

```swift
for i in 1...10{
    switch i{
    case 1..<3:
        print("\(i) : This is 1..<3")
    case 3..<5:
        print("\(i) : This is 3..<5")
    default:
        print("\(i) : This is in any")
    }
}
```

### with tuple 

- 또한, tuple에 대해서 비교하는 것도 가능합니다. x, y 좌표로 구축된 `point1`이라는 변수에 대해서 control-flow를 만든다고 하겠습니다.
- 아래와 같이, 4가지 경우로 쪼갠다고 할게요.
  - case1) 원점에 있다. 
  - case2) x 축에 있는 경우 
  - case3) y 축에 있는 경우 
  - case4) 3가지 경우가 모두 아닌 경우.
- 이를 `if-then-else` 문을 사용해서 처리할 경우, 다음과 같습니다. 익숙한 패턴이기는 하지만, 흠, switch문에 비해서는 조금 지저분하고 가독성이 떨어지는 느낌이 있죠.

```swift
var point1 = (0, 1)// 실제로는 tuple이지만, (Int, Int)의 타입으로 기록된다.

if(point1.0==0){
    if(point1.1==0){
        print("\(point1) is at origin")
    }else{
        print("\(point1) is at x axis")
    }
}else{
    if(point1.1==0){
        print("\(point1) is at y axis")
    }else{
        print("\(point1) is at somewhere")
    }
    
}
```

- 이를 switch 문을 사용해서 표현하면 다음과 같이 됩니다.
- 흥미로운 것은 `_`라는 놈이 나온것인데, 이 아이는 일종의 wildcard pattern이며, 그냥 `"any"`를 의미한다고 생각하시면 됩니다.
- 쓰고 보니, `if-else` 문보다는 switch를 쓰는 것이 더 가독성 측면에서도 그렇고 더 깔끔해보이기는 하네요.

```swift
var point1 = (0, 1)// 실제로는 tuple이지만, (Int, Int)의 타입으로 기록된다.

print(type(of:point1))

switch point1 {
case (0, 0):
    print("\(point1) is at origin")
case (_, 0): // _ 는 wildcard로 'any'를 의미한다고 생각하면 된다. 
    print("\(point1) is at y axis")
case (0, _):
    print("\(point1) is at x axis")
default:
    print("\(point1) is at somewhere")
}
```

- 그 외로도, case 내에서 해당 변수의 이름을 새롭게 만들어줘서(value binding) 비교를 한다거나, 하는 방법들이 있지만, 중요하지 않다고 생각하여 추가로 설명하지는 않습니다. 필요성도 딱히 모르겠네요.

## control transfer statement

- `continue`, `break`의 일반적인 사용은 워낙 익숙하니까 넘어가도록 합니다.

### fallthrough

- C에서는 case 문별로 break가 존재하지 않으면 항상 default에 있는 명령어가 실행되었습니다. 
- 하지만, swift에서는 반대로, break가 기본값인 것이죠. 항상 해당 case만 실행되고 넘어가게 되는데, 만약 default가 항상 실행되도록 하고 싶다면, `fallthrough`를 사용해서 처리할 수 있습니다.
- 보통은 control-flow 문에서는 exclusive를 기본으로 합니다. 논리명제를 따질 때, 서로 배반적인 것을 기본으로 가정하기 때문에, 하나의 case에 속한다면 다른 case에 속하는지 여부는 따지지 않죠. switch문에서도 마찬가지인데, 만약 다음처럼 `fallthrough`를 끝에 넣는다면, 다른 case들에 대해서도 모두 따지게 됩니다.

```swift
let integerToDescribe = 6
var description = "The number \(integerToDescribe) is"

switch integerToDescribe {
case 2, 3, 5, 7, 11, 13, 17, 19:
    description += " a prime number, and also"
    fallthrough // 현재 case에 속하지만, 이 switch문을 빠져나가지 않고, 다른 case에 대해서도 맞는지 체크함.
case 2, 4, 6, 8, 10, 12, 14, 16, 18:
    description += " multiples of 2, and also"
    fallthrough
case 3, 6, 9, 12, 15, 18:
    description += " multiples of 3, and also"
    fallthrough

default:
    description += " an integer."
}
print(description)
```

- 이렇게 할 경우 여러 케이스에 대해서 동시에 확인해주기 때문에, 아래와 같이 여러 case의 결과가 혼합되어 나오게 되죠.

```plaintext
The number 6 is multiples of 2, and also multiples of 3, and also an integer.
```

### etc

- 그 외로, 함수에서 if 대신 guard를 사용하는 방법도 있는데, 굳이 써야 하는지 잘 모르겠네요.

## wrap-up

- 흥미롭게도, 이번 챕터에는 전반적으로 `switch`에 대한 이야기들이 많이 작성되어 있습니다. apple이 `switch`를 매우 좋아하나 봅니다 호호호
- 몇몇 경우에 대해서는 switch로 작성하는 것이 좀 더 가독성 측면에서 그리고 속도 측면에서 좋을 것으로 보이기도 합니다. 특히, C와 비교했을 때는 좀 더 편해지기도 했구요.
- 하지만 과연 제가 쓸지는 모르겠네요 호호호.
