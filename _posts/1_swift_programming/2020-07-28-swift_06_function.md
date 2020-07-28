---
title: swift - chapter 6 - function
category: swift
tags: swift tutorial function
---

## swift - chapter 6 - function

- function, 함수는 "특정일을 수행하도록 만들어진 코드"정도로 이해하면 됩니다. 그냥 코드를 길게 짜다 보면 느끼는 것이지만, 내가 반복적으로 비슷한 코드를 만들고 있다, 라는 생각이 들면 코드를 효율적으로 관리하기 위해 그 중복되는 부분을 하나의 함수로 만들게 됩니다. 이를 통해 전체 코드의 줄 수를 줄이며, 각각의 역할이 무엇인지 명확하게 작성하여, 코드를 좀 깔끔하게 볼 수 있죠.
- 어떻게 함수를 나누는 것이 가장 좋은가? 라는 질문은 유효하며, 항상 코드를 짜면서 고민해야 합니다. 이 아이를 어떻게 함수로 만들어야 효과적일까? 와 같은 질문은 항상 중요하죠.

## defining and calling function in swift

- swift는 본질적으로, python보다는 C에 닮아 있습니다.
- python의 경우 변수 타입은 물론 함수에서도 어떤 타입이 들어오고 어떤 타입이 나가는지에 대해서 명확하게 작성하지 않는 반면, swift는 이를 면밀하게 작성해야 합니다. 이를 작성하지 않을 경우, 컴파일 되지 않습니다.
- 책에서는 다음과 같이 간단한 함수 예제를 보여줬습니다. 보시면, input과 output의 type을 명확하게 작성해준 것을 알 수 있죠. 

```swift
func Greet(person_name:String) -> String{
    var greeting = "Hi! " + person_name
    return greeting
}
```

- 그리고, 기정의된 함수를 call하여 사용하려면 다음과 같습니다. 
- 좀 번거롭지만, 매번 parameter와 argument를 모두 써서 넘겨줘야 합니다. 
  - `parameter`: 보통 함수에서 필요로 하는 인수, `person_name`
  - `argument`: 해당 parameter에 들어가서 넘어오는 **값**, `"Seunghoon Lee"`

```swift
// Greet("Seunghoon Lee") 으로 실행되지 않음.
Greet(person_name:"Seunghoon Lee")
```

### omitting argument label

- 만약, 이렇게 넘겨주는 것이 귀찮다는 생각이 들면, 다음과 같은 방식으로 parameter 이름 없이 넘겨줄 수도 있습니다.
- 그냥 함수 정의 할때 parameter 앞에 `_` 만 하나 붙여주면 됩니다.
- 하지만, 굳이 이를 강제하는 이유가 있을 것이므로 저는 가능하면 매번 parameter label을 모두 작성하면서 써주려고 합니다. 사실 그래야, 이후 가독성 측면에서도 훨씬 좋은게 사실이니까요.

```swift
func Greet(_ person_name:String) -> String{
    var greeting = "Hi! " + person_name
    return greeting
}

Greet("Seunghoon Lee")

```

### In-out parameter

- C에서 함수를 쓸 때, 값을 넘기는 것을 보통 다음 두 가지로 처리하죠. 
  - call by value: 값을 넘기는 경우 
  - call by reference: 값이 존재하는 주소를 넘기는 경우
- 많은 경우에는 그냥 값을 넘기는 것만으로 충분한데, 이미 배열을 정렬하거나 해야 할 때는 주소를 통해 해당 주소에 저장된 값을 바꿔주는 것이 필요할 때가 있습니다.
- 만약 두 Int 에 저장된 값을 바꾸려면 `inout`을 작성해서 다음처럼 하면 되죠.

```swift
func swapTwoInts(a:inout Int, b:inout Int){
    var temp:Int = a
    a = b
    b = temp
}

var i1 = 10
var i2 = 20

print("i1: \(i1), i2: \(i2)")
swapTwoInts(a: &i1, b: &i2)
print("i1: \(i1), i2: \(i2)")
```

```plaintext
i1: 10, i2: 20
i1: 20, i2: 10
```

### Closure 

- Closure는 흔히 말하는 lambda function이라고 보시면 됩니다. 딱히 필요하지 않을 것 같아서, 일단은 더 정리하지 않습니다.
- closure를 정의하는 문법 자체는 크게 어렵지 않고, 필요할 때 보고 쓰면 될 것 같아요.

### etc

- function을 parameter로서 받아들일 수도 있고, return type이 될 수도 있습니다. 이럴 때는 해당 function의 타입이 꽤나 지저분하게 보일 수는 있지만, 가능하죠. 뭐, 이건 원래 python에서도 가능하던 일이기는 합니다. python에서는 그냥 따로 타입을 지정하지 않고 그냥 쓰면 되죠.

## wrap-up

- swift는 꾸준하게 타입을 명시해주는 것이 필요하네요. 사실 이게 좀 더 전통적인 코딩방식이고, 솔리드하게 코딩하는 방식이기는 합니다.
- 다른 프로그래밍 언어에서는 lambda라고 부르는 것을 여기서는 closure라고 부릅니다. 흠.