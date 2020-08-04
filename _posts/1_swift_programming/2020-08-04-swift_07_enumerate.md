---
title: swift - chapter 7 - Enumerations
category: swift
tags: swift tutorial enumeration
---

## swift - chapter 7 - Enumerations

- swift에 enumeration이라는 자료형이 있습니다. C에서는 보통 '열거형'이라고 번역해놓았는데, 저는 이보다, "연관된 상수 집합"이라고 번역하는 것이 더 좋다고 생각해요. 물론 C에서도 저는 enumeration을 직접 사용해본 적은 매우 적습니다만, 그건 늘 학부 수준에서의 프로젝트만 진행해서 그랬던 것이죠.
- 구글에 검색해서 찾아보시면 많은 사람들이 왜 `enum`을 쓰는 것이 좋은지에 대해서 정리를 해두기는 했습니다. 대부분, "가독성이 좋아지고 코드의 라인 수가 줄고, 에러를 발생시킬 가능성이 준다"라는 것이 주요 이유네요.
- 아무튼, 여기서는 swift에서의 enum과 C에서의 enum과의 차이 들에 대해서 대략적으로 정리하겠습니다.

## why enum

- `enum`은 "연관된 상수 집합"입니다. 사실 얘가 없어도 그냥 다음과 같이 써도 별 문제는 없죠.
- 다만, 코드가 좀 지저분해진다는 것과, 오타 등으로 인해 에러가 발생할 확률이 있다는 점이 좀 신경쓰이는 부분이죠.

```swift
let North = "North"
let South = "South"
let West = "West"
let East = "East"

var currentCompass = "South"

switch currentCompass{
case North:
    print("This is North")
case South:
    print("This is South")
case West:
    print("This is West")
case East:
    print("This is East")
default: // Warning: default will never be execueted
    print("This is default")
}
```

- 위 코드를 `enum`을 통해서 보다 간결하게 표현할 수 있습니다. 
- c와 비교했을 때의 차이점이라면, "C는 North, South, 에 순서대로 0, 1, 과 같은 값을 부여했고", swift는 각각 독립적인 값을 가지기 때문에 서로 다른 열거형 자료 형에 대해서 비교가 불가능하다, 정도가 있겠네요.
- 이 표현형태는 오히려 c보다는 java에서의 enum과 유사하다고 볼 수 있습니다.

```swift
enum CompassPoint{
    // same as "case North, South, West, East"
    case North; case South; case West; case East
 }

 var currentCompass = CompassPoint.North

 switch currentCompass{
 case CompassPoint.North:
     print("This is North")
 case CompassPoint.South:
     print("This is South")
 case CompassPoint.West:
     print("This is West")
 case CompassPoint.East:
     print("This is East")
 default: // Warning: default will never be execueted
     print("This is default")
 }

```

### Iterating over enum in swift

- `enum`을 열거형 자료 타입이며, 필요에 따라서 해당 자료형에 속해 있는 상수들이 무엇인지 iterate할수도 있습니다.
- 다만, 이게 기본 값은 아니고, 다음과 같이 `CaseIterable`을 뒤에 붙여주어야 하죠.

```swift
// enum 자료 이름 뒤에 CaseIterable 을 붙여주면 iteration이 가능해짐.
enum CompassPoint:CaseIterable{
    case North, South, West, East
 }

for c in CompassPoint.allCases{
    print(c)
}
```

### enum with type

- enum은 상수에 대해서만 정의할 수 있는 것이 아니라, 좀더 세부적인 타입에 대해서도 정의할 수 있습니다.
- barcode를 정의할 때, 필요에 따라서 숫자 조합과 문자열이 모두 사용될 수 있죠. 
- swift에서는 enum을 이용해서 이 두가지만 해당 enum에 속할 수 있다는 것을 강제합니다. 만약 다른 형태로 값이 들어오게 된다면 compile 단계에서 에러가 발생하게 되죠.

```swift
enum BarCode{
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}

var barcode1 = BarCode.upc(1, 3, 4, 5) // valid
var barcode2 = BarCode.qrCode("THIS IS STR") // valid

print(barcode1)
print(barcode2)
```

```plaintext
upc(1, 3, 4, 5)
qrCode("THIS IS STR")
```

- 그리고 이 형식에 따라서, switch 문을 사용할 수도 있죠.

```swift
enum BarCode{
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}

var barcode1 = BarCode.upc(1, 3, 4, 5) // valid


switch barcode1{
case BarCode.upc(let dgt1, let dgt2, let dgt3, let dgt4):
    print("This is upc")
    print("upc: \(dgt1), \(dgt2), \(dgt3), \(dgt4)")
case BarCode.qrCode(let str1):
    print("This is qrCode")
    print(str1)
}
print("=========")

barcode1 = BarCode.qrCode("THIS IS STR")


switch barcode1{
case BarCode.upc(let dgt1, let dgt2, let dgt3, let dgt4):
    print("This is upc")
case BarCode.qrCode(let str1):
    print("This is qrCode")
    print(str1)
}
```

## wrap-up

- 그 외에도, enum에 RawValue를 함께 넣어주는 방식과, recursive하게 처리해주는 방식등이 있는데, 지금은 당장 필요하지 않을 것 같아서 그냥 넘어가기로 합니다.