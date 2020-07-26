---
title: swift - chapter 3 - Strings and Characters
category: swift
tags: swift string
---

## swift - String and Charaters

- swift에서 String은 독자적인 타입으로서 존재합니다. C를 떠올려 보면, 문자열이 독자적으로 존재하는 것이 아니라, array의 부분집합과 같은 개념으로 존재하죠. 사실 이런 부분때문에, C를 과외할 때 힘들었던 기억이 있습니다. 과외학생이 "String이 뭔가요?"라고 물으면, array이면서, 끝에 null이 존재하는 것 정도로만 설명해야 하니까요. 그래서 array로 접근하면서 헷갈려하는 경우들이 있었던 것 같아요.
- 아무튼, 다음처럼 선언 및 정의하여 사용할 수 있습니다. 

```swift
let str1 = """
first sentence
second sentence
"""

print(str1)
```

- 빈 스트링은 다음을 통해 사용할 수 있습니다. `String()`을 통해 정의할 수 있고 또 `""`로 정의해줘도 되죠. 

```swift
var s1 = ""
print(s1=="")
print(s1==String())
print(""==String())
print(s1.isEmpty)
```

- String을 정의 할 때, 내부에 특수문자가 있거나, unicode가 있거나 할 경우 이 아이들을 변환해서 출력해줍니다. 가령, `"\u{24}"`는 `$`를 의미하며, print해보면 unicode 값이 나오는 것이 아니라, `$`가 출력되죠. `"\u"`는 이 뒤에 나오는 값이 유니코드라는 것을 의미하고, `{}`내에 유니코드 번호를 넘겨줌으로써, 유니코드를 전달해주는 것이죠. unicode interpolation 같은 기법이라고 생각하시면 될 것 같습니다.
- 다만, 이렇게 하지 않고 안에 들어 있는 text를 그대로 보고 싶다면, String 앞 뒤에 `#`를 넣어서 출력하면 됩니다.
- 아래 코드에서 보는 것처럼, 앞 뒤로 `#`을 넣어주면 텍스트가 그대로 나오고 그렇게 하지 않으면 특수문자들은 변환되어 출력되죠.

```swift
var s3 = #"""
Line 1\nLine 2
\u{24}
"""#
print(s3)
print("====")

var s4 = """
Line 1\nLine 2
\u{24}
"""
print(s4)
```

```plaintext
Line 1\nLine 2
\u{24}
====
Line 1
Line 2
$
```

## String ar value type

- swift에서 `String`은 *value type*입니다. 이 말은 copy-by-default라는 것을 말하죠. 특정 변수에 다른 변수의 값을 assign하게 되면, 하나의 값을 공유하는 것이 아니라, 새로운 메모리에 새로운 값을 생성해서 넣어준다는 것을 의미합니다. 뭐, 이건 python도 그렇기는 하죠.

```swift
var s1:String = "ABC"
var s2:String = s1

print("s1: \(s1)")
print("s2: \(s2)")
print("==========")
s1 = "NEW_ABC"
// 이렇게 s1의 값을 변경해도, s2의 값이 변경되지 않음.
print("s1: \(s1)")
print("s2: \(s2)")
```

- 아래에서 보는 것처럼, `s1`의 값을 중간에 변경해줬지만, `s2`의 값이 변경되지는 않았습니다. 

```plaintext
s1: ABC
s2: ABC
==========
s1: NEW_ABC
s2: ABC
```

### Character: Extended Grapheme Clusters

- 사실 이건 string은 아니고, `Character`에 관한 이야기이기는 합니다.
- 개인적으로, 굉장히 재미있다고 생각한 swift의 특징이 바로 grapheme cluster입니다. *Grapheme*은 "한 언어 체계 내에서 가장 최소가 되는 단위"를 의미합니다. 영어로 치면 알파벳이 될 것이고, 한글로 치면 ㄱ, ㅏ 등의 자모음이 되겠죠.
- 영어는 하나의 문자가 하나의 단위를 그대로 차지합니다. 가령 3칸이면 영어를 알파벳 3개, 즉 3개의 grapheme이 들어갑니다. 하지만, 한글의 경우는 한 글자이지만, 2개, 3개 혹은 4개의 grapheme이 들어갈 수도 있다는 이야기죠. 
- 아래 코드를 보시면 더 명확해지는데요. `precomposed`에는 "한"이 들어있고, `decomposed`에는 "ㅎㅏㄴ"이 들어 있습니다. 
- 다만, 두 변수 모두 String이 아닌 Character죠. 이 때, swift는 알아서 해당 단어들을 묶어서, 새로운 하나의 글자를 완성합니다.

```swift
let precomposed: Character = "\u{D55C}"//한
let decomposed: Character = "\u{1112}\u{1161}\u{11AB}"// ᄒ, ᅡ, ᆫ

print("precomposed: \(precomposed)")
print("decomposed: \(decomposed)")
print(precomposed==decomposed)
```

- 각 Character를 정의할 때 방식이 조금은 달랐지만, 결과적으로는 동일한 값이 두 변수에 assign되었죠.

```plaintext
precomposed: 한
decomposed: 한
true
```

- 그런데, 만약 조합될 수 없는 grapheme을 넣어도 이런 결과가 나올까요?
- 아래 코드를 보시면, `ㅎ`으로만 연속된 긴 문자를 하나의 Character에 집어넣었습니다. 실제로는 하나로 합쳐질 수 없는 문자죠. 그러나, swift에서는 이게 일단은 가능하고, 문제없이 출력됩니다.

```swift
let decomposed: Character = "\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}\u{1112}"// ㅎ*12

print("decomposed: \(decomposed)")
print("----------")

var decomposed_to_str = String(decomposed)

print("count: \(decomposed_to_str.count)")
print("utf16.count: \(decomposed_to_str.utf16.count)")
```

- Character를 String으로 변환해서, 그 길이를 확인해도, 길이는 1인 것처럼 나옵니다. 
- 하지만, 이 아이를 utf16으로 변환한다음, 길이를 확인하면 12가 나오죠. 

```plaintext
decomposed: ᄒᄒᄒᄒᄒᄒᄒᄒᄒᄒᄒᄒ
----------
count: 1
utf16.count: 12
```

- 정리하자면, swfit에서는 하나의 Character에 여러 unicode를 조합하여 Grapheme Cluster로서 표현할 수 있습니다. 만약, 조합해서 새로운 문자형태가 나온다면 해당 문자에 맞춰 변환해서 출력해주겠지만, 그렇지 않을 경우 그냥 string처럼 출력됩니다. 하지만, string이 아니라 character이죠. 
- 간단히 말하면, swift에서 Character를 좀더 범용성 있게, 표현할 수 있도록 변수 타입 자체를 좀 유연하게 만들었다고 보는게 좋을 것 같네요.

## Accessing and Modifying String

- C도 그렇고 python도 그렇고 String은 array, list와 같이 integer position으로 각 character를 접근할 수 있습니다. 다음과 같죠. 

```python 
a = "abcd"
print(a[0])
```

- 하지만, swift에서는 String을 이처럼 Integer position으로 접근하는 것이 불가능합니다. 
- 이건 앞에서 말했던 Grapheme Cluster와도 연결되는 이야기인데, swift는 각 Character가 사용하는 메모리가 동일하다고 가정하지 않습니다. 어떤 아이는 여러 유니코드를 조합해서 하나의 캐릭터로 구성되어 있을 수도 있고 어떤 아이는 그냥 1개의 캐릭터로 구성되어 있을 수도 있으니까요.
- 해당 포지션으로 다이렉트로 접근하는 것은 불가능하고, iterable하게 접근하는 것만이 가능합니다.
- 고정된 것은 `.startIndex`를 통해서 첫번째 캐릭터의 인덱스를 가져올 수 있고, `.endIndex`를 통해서 마지막 캐릭터의 인덱스를 가져올 수 있죠. 이로부터 인덱스 값을 구한 뒤, 해당 인덱스에 존재하는 캐릭터를 가져와야 합니다.
- 즉 integer로 접근하는 것이 아니라, `Index`라는 타입의 변수를 넘겨줌으로써 접근할 수 있다는 것이죠. 이렇게 쓰고 보니, 마치 linked list처럼 느껴지는군요. 아, 아니 그냥 swift에서의 String은 linked list로 보는 것이 맞다고 느껴집니다. 다이렉트로 접근할 수 없고, 처음 그리고 끝의 인덱스를 통해서 해당 인덱스를 추출해야 하고, 그 다음에 값을 넘김으로써 파악할 수 있다는 점에서 매우 적절하네요(이렇게 처리할 경우 매 스트링마다 시간이 오래 걸릴 수도 있다는 생각이 드는데, 흠 이건 나중에 알아보도록 하겠습니다.)

```swift
let greeting:String = "ABCDEF"
print("greeting: \(greeting)")
print("greeting.startIndex: \(greeting.startIndex)")
print("greeting.endIndex: \(greeting.endIndex)")
print("-----------------")

// greeting.startIndex에서 2칸 뒤에 있는 인덱스 값을 저장.
let startIndex_next_next = greeting.index(greeting.startIndex, offsetBy:2)
// Index라는 타입.
print("type of startIndex_next_next: \(type(of:startIndex_next_next))")
print(startIndex_next_next)
print(greeting[greeting.startIndex])
print(greeting[startIndex_next_next])
```

```plaintext
greeting: ABCDEF
greeting.startIndex: Index(_rawBits: 1)
greeting.endIndex: Index(_rawBits: 393217)
-----------------
type of startIndex_next_next: Index
Index(_rawBits: 131329)
A
C
```

## wrap-up

- 다른 것보다, integer로 String을 접근할 수 없다는 것이, 불편하게 느껴집니다. 이건 제가 생각했던 것보다 훨씬 크리티컬하게 느껴지는데, 아마 파이썬을 능숙하게 다루시는 분들은 대부분 그럴거에요. 쉽게 스트링을 가져오고 복사하고, subtring에 접근하고 해서 처리할 수 있는 부분들이 swift에서는 모두 주어진 메소드를 통해서 처리해야 합니다. 물론 그러함으로 인해 grapheme cluster와 같은 것이 가능한 것이겠죠.
- 그외로도 unicode와 관련된 다른 이슈들도 있지만, 여기서는 더 진행하지 않겠습니다.
- 다음시간에는 collection를 정리해서 가져오겠습니다.
