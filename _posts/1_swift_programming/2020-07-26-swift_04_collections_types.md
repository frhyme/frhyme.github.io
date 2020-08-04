---
title: swift - chapter 4 - Collection Types
category: swift
tags: swift array collection
---

## swift - chapter 4 - Collection Types

- swift에는 array, set, dictionary라는 3가지 종류의 collection이 존재합니다
  - array는 순서가 있는 리스트. 
  - set는 순서 없는 집합 
  - dictionary는 key, value가 존재하는 사전형식의 저장소죠.
- 다만, python의 예를 들어보면, python의 list에서는 타입과 상관없이 어떤 값이든 넣을 수 있었습니다. 가령 다음과 같이 String, int, double이 뒤섞여서 하나의 리스트에 있는 것이 가능했죠.

```python
lst = ["abc", 1, 3.0]
```

- 하지만, swift에서는 이것이 불가능합니다. 동일한 타입에 대해서만 값을 넣을 수 있죠. 불편하게 느껴질 수 있지만, 오히려 이 편이 좀 더 not error-prone한 방식이죠.

## swift - collection - Array 

- Array는 다음과 같은 형태로 만들고 값을 넣어줍니다. 아래를 보시면 여러 가지 방식이 있는데, 저는 `var arr2:[Int] = []`가 좀 더 편한 것 같네요.
- `var arr3:Array<Int> = []`의 형식은 마치 C++에서 본 것과 유사하군요.

```swift
var arr1 = [Int]() // Empty array
var arr2:[Int] = [] // Also empty array
var arr3:Array<Int> = []
print(type(of:arr1)) // Array<Int>
print(type(of:arr2)) // Array<Int>
print(type(of:arr1)==type(of:arr2))
```

```plaintext
Array<Int>
Array<Int>
true
```

- `.append`를 통해 원소를 뒤에 넣고, 
- `[0]`와 같이 integer index로 각 포지션의 원소에 접근 가능하고, 
- `+`를 통해 두 어레이를 합칠 수 있고, 
- 기본적으로 deep copy를 지원합니다. 아래와 같은 코드를 돌려보면, `arr1`과 `arr2`는 동시에 달라지지 않습니다.

```swift
var arr1:[Int] = [1, 2]
var arr2 = arr1
print(arr1) // [1, 2]
arr1.append(3)
print(arr1) // [1, 2, 3]
print(arr2) // [1, 2]
```

- python에서는 `enumerate`라는 함수를 통해서 리스트에 들어 있는 값을 integer index와 함깨 가져왔다면, swift에서는 `.enumerated` 메소드를 사용해야 합니다. 다음과 같죠.

```swift
var arr1:[Character] = ["a", "b", "c"]

for (i, c) in arr1.enumerated(){
    print("i: \(i), c: \(c)")
}
```

```plaintext
i: 0, c: a
i: 1, c: b
i: 2, c: c
```

## swift - collection - Set

- 아래와 같이 선언하고 사용합니다. set는 list와 다르게, 중복을 허용하지 않고, hashable한 object에 대해서만 값을 넣을 수 있고, 다양한 set operation을 지원하는 장점들이 있는데, 이는 python과 별반 다르지 않아서, 자세하게 정리하지는 않습니다.
- 다만, python에서는 set를 `()`을 사용해서 정의했는데, swift에서는 또 `[]`을 사용해서 정의합니다. 따라서, 타입을 직접 써주지 않고, 그냥 넘겨주면 set로 이해하지 않고 array로 인식할 것 같군요.

```swift
var set1:Set<Int> = [1, 2, 3, 4, 5, 5, 5, 5]

print(type(of:set1))
print(set1)
```

## swift - collection - Dictionary

- dictionary는 key, value로 구성된 자료구조이고, 뭐 워낙 많이 쓰이니까 따로 설명을 더 하지는 않겠습니다.
- `.keys`와 `.values`로 키와 밸류에 각각 접근할 수 있고, 아무것도 쓰지 않고 그냥 접근할 경우 python에서의 `.items()`처럼 접근하게 됩니다.

```swift
var dict1:[String:Int] = [:]
dict1["A"] = 1
dict1["B"] = 2
dict1["B"] = 3
print(dict1)

for (k, v) in dict1{
    print("k: \(k), v: \(v)")
}
```

```plaintext
["A": 1, "B": 3]
k: A, v: 1
k: B, v: 3
```

## wrap-up

- swift에서 사용하는 array, set, dictionary에 대해서 간략하게 정리하였습니다. 뭐 python과 유사해서 별로 공부할 것은 없었던 것 같네요.
