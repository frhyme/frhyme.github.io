---
title: swift - chapter 1 - The Basics.
category: swift
tags: swift 
---

## Constant and variable

- C와 유사하게, swift에서도 상수(constant)와 변수(variable)이 존재합니다. 
- 상수는 한번 값을 초기화한 다음 바꿀 수 없고, 변수는 아무 때나 언제든지 바꿔도 됩니다.
- 아래 코드에서 보는 것처럼, `let`을 쓰면 상수로 만들고, 값을 지정할 수 있는 것이죠.

```swift
var var1 = 10 // variable, 변수
let const1 = 1000 // constant, 상수, 값을 바꿀 수 없음.

var1 = 10
const1 = 20 // ERROR: Cannot assign to value: 'const1' is a 'let' constant
```

### Type annotation 

- swift에서는 각 변수/상수의 타입을 뒤에 붙여주는 형식을 가집니다. 다음과 같죠.
- 물론, swift는 type inference도 해주기 때문에 type annotation 없이 값을 집어넣으면 알아서 타입을 추론해주기도 합니다.

```swift
var var1:String = "aaa"
var var2:Int = 50 
```

## print with String Interpolation 

- 긴 문자열 내에 특정한 변수/상수를 집어넣어서 출력하고 싶다면, 아래와 같이 쓰면 됩니다.

```swift
var MyName = "SeunghoonLee"

print(MyName)
print("My name is \(MyName)")
```

## comments 

- 주석은 다음과 같은 방법들로 달 수 있구요. 

```swift
// comment1
/* comment2 */
```

## multiline with semicolon

- semicolon 없이 사용해도 되지만, 만약 한 줄에 여러 라인을 집어넣고 싶다면 세미콜론을 사용하면 됩니다.

```swift
var MyName = "SeunghoonLee"; print(MyName);
```

## Type safety and type inference

- swift는 type-safe 언어입니다. 즉, 각 변수에 주어진 타입이 고정되어 있는 것을 말하죠. 
- 파이썬의 경우 어떤 변수에 정수를 넣었다가, 스트링을 넣었다가 해도 아무 문제가 없지만, swift에서는 이런 것이 불가능합니다. 한번 정수를 넣었다면, 정수만 넣을 수 있고, 문자열을 넣었다면 문자열만 넣을 수 있죠.
- 코드 컴파일 시에, 해당 코드에 type-safety를 확인하고 잘못되었을 경우, 에러를 던져줍니다.
- 그리고, 만약 개발자가 type을 선언해주지 않았다면, 입력된 값을 토대로 해당 변수의 타입을 유추하죠. 
- 가령 다음과 같이 값만 넣어줘도 알아서 type을 결정해놓습니다.

```swift
var MyName = "SeunghoonLee"
print(type(of:MyName)) // String
```

## Booleans

- C언어의 문제점으로, `if`와 같은 로지컬 오퍼레이터에 대해서, Boolean이 아닌, Integer값도 문제없이 돌아간다는 게 있죠.
- swift는 logical operator에 대해서는 boolean 값만이 작동합니다.

```swift
var i = 10
if i {
    // i는 boolean이 아니므로 컴파일 시에 문제가 발생함.
    print("ERROR")
}
```

## tuple

- tuple은 `()`로 묶여 있는 기본적인 자료 구조죠. 관련 있는 값들을 함께 관리하기 편한데. 
- 대충 다음과 같이 사용합니다. 다만, python의 경우 tuple의 값에 접근할 때, `tuple1[0]`과 같은 방식을 사용하지만, swift의 경우, `tuple.0`과 같은 방식을 사용하는 것이 다르죠.
- 그리고, python에서는 tuple이 mutable합니다. 값을 한번 정하면 바꿀 수 없는데, swift에서는 tuple 내부의 값들도 바꿀 수 있습니다. 물론 타입은 변경할 수 없구요.

```swift
var tuple1 = ("elem1",123, 132.5, true)
print(tuple1)
print(tuple1.0) // tuple의 값에 접근하려면, .
tuple1.0 = "ssss"
print(tuple1.0)
```

```plaintext
("elem1", 123, 132.5, true)
elem1
ssss
```

### namedtuple

- 또한, tuple이지만, 아래처럼 딕셔너리처럼 사용할 수도 있죠. namedtuple처럼 사용할 수도 있습니다.

```swift
var tuple_with_keys = (k1: "value1", k2: 30, k3:50.0)
print(tuple_with_keys)
print(tuple_with_keys.0)
print(tuple_with_keys.k1)
```

```plaintext
(k1: "value1", k2: 30, k3: 50.0)
value1
value1
```

## Optionals

- 이게 swift의 큰 특징중 하나입니다. 앞서 말한 것처럼 swift에서는 모든 변수들이 초기화가 되어야 합니다. 즉, 모든 변수에는 값이 있다는 걸 전제하고 프로그래밍을 하게 되는데, 필요에 따라서, 값이 없는 상태, 즉 valueless를 설정할 수 있는 것이죠. 
- 다르게 말하면, 어떤 동작을 했을 때 그 값이 확정적으로 주어진다고 말하기 어려운 상황들이 있습니다. 본문에서는 이를 `String`을 `Int`로 conversion하는 경우로 설명합니다. 
- 아래 코드를 보면 `"1234"`라는 String을 Integer로 변환합니다. 변환이 가능하기는 한데, 사실 모든 string에 대해서 Integer로 변환이 가능한 것이 아니죠. 즉, 어떤 String은 Integer로 변환이 가능하지만, 어떤 String은 변환이 불가합니다. 
- 따라서, 이런 경우, `convertedNumber`는 `Int`의 타입을 가지는 것이 아니라, `Optional<Int>`의 형태를 가지게 됩니다.

```swift
var possibleNumber = "1234"
var convertedNumber = Int(possibleNumber)
print(type(of:possibleNumber))
print(type(of:convertedNumber))
```

```plaintext
String
Optional<Int>
```

### nil

- 그리고, 만약 변환할 수 없어서,아무 값도 존재하지 않는 경우를 `nil`로서 표현합니다.
- 아래 코드에서 보는 것처럼, `Int` 뒤에 붙는 `?`는 해당 변수가 `nil`을 상태로서 가질 수 있다는 것을 의미합니다. Int가 아닌 다른 어떤 타입에 대해서도 그냥 뒤에 `?`를 붙여주면 `nil`이라는 값을 가질 수 있게 되죠. 

```swift
var v1: Int? = 30
print(v1)
v1 = nil
print(v1)
```

```plaintext
Optional(30)
nil
```

## wrap-up

- 그외에도 assertion, precondition 으로 런타임 시에 문제가 없는지 확인하는 기능이 있고, 또 간단하게 error handling도 언급되었습니다. 
- 다만, error handling은 나중에 더 자세하게 배우는 것이 좋을 것 같아 제외하였고, assertion, precondition은 당장 필요하지 않아서 마찬가지로 제외하였습니다.
