---
title: python - byte string, literal string. 
category: python-basic
tags: python python-basic string ascii utf-8
---

## intro

- 가끔 python으로 문자열을 처리하다 보면 앞에 `b`라는 문자 하나가 붙는 것을 볼 수 있습니다. 출력은 문제없이 되니까, 그냥 써도 문제가 없을 때가 있지만, 에러가 발생한다거나, string간의 비교를 정확하게 못해줄때가 있죠. 
- python으로 프로그래밍을 입문하신 분들은 헷갈릴 수 있습니다만, 사실 이 아이는 해당 문자가 'string'이 아니고, '숫자들의 조합'이라는 것을 의미합니다. 그래서, 다음 코드를 보면 이 같은 문자열처럼 보이지만, 타입이 다름은 물론, 비교하면 다르다고 연산해주죠.

```python
s1 = b"frhyme"
s2 = "frhyme"
print(s1, type(s1))
print(s2, type(s2))
print(s1==s2)
```

```plaintext
b'frhyme' <class 'bytes'>
frhyme <class 'str'>
False
```

## ascii code: 컴퓨터의 character 이해 방식

- C를 공부할때의 기억을 더듬어 보면, ascii code라는 것이 있었죠. 사실 컴퓨터는 0과 1로 모든 것을 기억하며, 우리가 쓰는 'a', 'b'를 그대로 기억하지 못하여, 각 문자(character)에 ID를 부여합니다. 즉, 변환 약속이죠. "앞으로 65는 숫자 'A'를 의미한다고 하자"와 같이요. 
- 다만, C에서는 같은 값이라도, 이를 `%d`를 사용해서 "숫자로 표현"할 것인지, `%c`를 통해, "문자로 표현"할 것인지를 `printf`에서 다르게 사용할 수 있었습니다. 즉, 아래의 결과는 같다는 말이죠. 

```c
printf("%c", 'A')
printf("%c", 65)
```

## byte string and literal string in python

- 다만 python에서는 이 두가지가 다릅니다. 각각 "byte string", "literal string"을 말하죠. 
- 즉, 앞서 말한 ascii code처럼 각 문자에 매칭된 숫자를 사용해서 string을 표현해주는 방식(byte string)과 python의 기본 자료 형인 string을 사용하여 문자를 표현해주는 방식(literal string)을 구분하였습니다. 
- 아래 코드를 보면 더 명확할 수 있는데요. `bytes`라고 하는 python에서 "1byte의 값을 연속적으로 저장하는 자료형"을 사용하여, 65, 66, 67을 표현해줍니다. 앞서 말한 것처럼, 아스키 코드 상에서 66은 "A", 67은 "B"를 의미하죠. 
- 당연히 해당 `a`는 bytes라는 자료형으로 표현되며, `b'ABC'`와 동일합니다.

```python
a = bytes([65, 66, 67])
print(type(a))
print(a)
print(a == b'ABC')
```

```plaintext
<class 'bytes'>
b'ABC'
True
```

- 다시, 앞서 "byte string"이라고 말했지만, 사실상 이 아이는 그냥 `bytes`일 뿐입니다. 보여질 때, 아스키 코드 상으로 변환될 수 있는 것들은 이미 변환되어, 문자열처럼 보여지는 것 뿐이죠. 그리고 앞에 bytes형태로 되어 있음을 명확하게 보여주는 `b`라는 글자가 붙습니다. 
- 무슨 소리야? 싶을 수 있습니다. 그럼 다음을 보시죠. 0을 bytes형태로 저장하고 그것을 출력합니다. 이번에는 문자가 아니라, `\x`로 시작하는 16진법의 값들이 막 나왔습니다. 일단은 각 byte에 해당하는 문자를 출력해주지 못하여, 16진법의 형태로 그대로 출력해준 것이죠. 이 경우에도 마찬가지로, 앞에는 `b`가 붙어 있습니다. 

```python
a = bytes([0, 16, 160, 255])
print(a)
```

```plaintext
b'\x00\x10\xa0\xff'
```

- 그럼 또 다시, 아래를 출력하면 어떻게 될까요? 이번에는 "ABC"가 나왔습니다. 16진수 41은 10진수로 65죠. 그리고 `b'ABC'`와 `b'\x41\x42\x43'`을 같다고 연산해줍니다.

```python
print(b'\x41\x42\x43')
print(b'\x41\x42\x43'==b'ABC')
```

```plaintext
b'ABC'
True
```

- 즉, 여러번 말했지만, 앞에 b가 붙으면, 그걸이 설령 `string`처럼 보일지라도 그냥 bytes일 뿐인 것이죠. 헷갈려서는 안됩니다. 

## encoding and decoding

- 자, 지금까지는, `bytes`와 `string`이 다르다는 것을 설명했습니다. 
- 그렇다면, 만약 우리에게 `bytes`로 표현된 text들이 있다면, 이 아이를 어떻게 `string`으로 바꾸어줄 수 있을까요?

### decoding: byte => string 

- decoding이 byte를 string으로 바꾸어주는 역할을 합니다. 

```python
a = b'ABC'
# default utf-8
decoded_a = a.decode(encoding='utf-8')
print(decoded_a)
print(type(decoded_a))
print(decoded_a=='ABC')
```

```plaintext
ABC
<class 'str'>
True
```

### encoding: string => byte

- 반대로 encoding은 string을 byte로 바꾸어주는 역할을 하죠.

```python
a = 'ABC'
# default utf-8
encoded_a = a.encode(encoding='utf-8')
print(encoded_a)
print(type(encoded_a))
print(encoded_a == b'ABC')
```

```plaintext
b'ABC'
<class 'bytes'>
True
```

## wrap-up

- `utf-8`은 뭐냐, `utf-16`은 뭐냐 와 같은 질문이 이어질 수 있지만, 이 아이들은 encoding, decoding 방식의 차이일뿐, 중요하지 않다고 판단되어 정리하지 않습니다.
- 그냥 저장방식의 차이일뿐이죠.

## reference

- [geeksforgeeks: byte objects vs string python](https://www.geeksforgeeks.org/byte-objects-vs-string-python/)
- [stackoverflow: what does the b character do in front of a string literal](https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal)
- [Wikipedia: UTF-8](https://ko.wikipedia.org/wiki/UTF-8)
