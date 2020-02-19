---
title: python에서, 2, 8, 16진법을 표현하는 prefix. 
category: python-basic
tags: python python-basic hexagonal number integer
---

## 2 line summary 

- python에서는 `0b`, `0o`, `0x`를 사용해서 2, 8, 16진법을 표현함.
- 16진법(hexagonal)를 표현하기 위해 `0x`를 사용하는 이유는, 사실 별거 없고 우연에 가깝다.

## python: binary, octal, hexa.

- 우리는 흔하게, 10진법을 사용하지만, 수는 다른 다양한 진법들로도 표현이 가능하죠. 
- 그리고, 어렵게 표현할 필요 없이, python에서는 다음과 같이, 숫자 맨앞에 오는 prefix만 바꿔주면 됩니다.
- 말로 하는 것보다, 코드가 편하죠. 다음과 같습니다.     
    - bin => prefix "0b" or "0B"
    - oct => prefix "0o" or "0O"
    - hex => prefix "0b" or "0B"
- 표현법은 다르지만, 세 변수에 할당된 값은 완전히 동일합니다.
```python 
"""
python에서 숫자를 표시할 때, 2진, 8진, 16진은 각각 다음과 같음.
(10진법은 앞에 아무것도 안 붙음)
bin => prefix "0b" or "0B"
oct => prefix "0o" or "0O"
hex => prefix "0b" or "0B"
"""
A_binary = 0b10001 # 2진법
A_octal  = 0o21    # 8진법
A_hex    = 0x11    # 16진법

assert A_binary == A_octal
assert A_octal == A_hex
print("== All same, complete")
```

## why are hexadecimal numbers prefixed with 0x? 

- 사실, 제 관심사는, 오히려, 왜 "0x"가 hexagonal number를 의미하는가? 에 가까워요. 찾아보다가, [stackoverflow: why are hexadecimal numbers prefixed with 0x?](https://stackoverflow.com/questions/2670639/why-are-hexadecimal-numbers-prefixed-with-0x)를 찾았고, 이 내용을 번역하였습니다. 

### Short story.

- `0`은 parser에게 이것이 'number'라는 것을 알려주며, 그 다음, 이 수가 어떤 진법인지 알려주기 위해서 `x`가 쓰인다. 

### Long Story. 

- 1960년대에, 주로 쓰이던 수 체계(numbering system)은 10진법(decimal)과 8진법(octal)이었다. 이는 그 당시 main frame들이 byte별로 12, 24, 36 의 bit를 가지고 있었기 때문이며, 이 값들은 모두 3(=log2(8))에 의해서, 나누어진다. 따라서, octal로 수를 관리할때의 강점이 존재했음(2^12 == 8^4)
- [BCPL(Basic Combined Programming language)](https://ko.wikipedia.org/wiki/BCPL)라는, 1966년에 설계된 프로그래밍 언어는 octal number를 위해서 `8 1234`라는 문법을 사용했는데, [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson)(C의 전신인 B 개발자)가 BCPL로부터 B를 만들고, 이 때, prefix를 `0`으로 하는 신택스를 제시했다. 이 방법의 강점은, 대충 다음이 있다(몇 개는 귀찮아서 날림). 
    - integer가 이제 내부에 "공백"없이, 하나의 token으로서 관리된다는 것, 
    - parser가 이제 그것이 숫자인지 바로 인지할 수 있다는 것, 
    - parser가 base(어떤 진법)인지 바로 알아차릴 수 있다는 것, 
- 이후, B로부터 C가 나왔을 때, 16진법(hexadecimal)에 대한 표현이 필요해졌고, 이때, "우연히", `0x`가 선택되었다.

- 라고 하는군요.



## reference

- [why are hexadecimal numbers prefixed with 0x](https://stackoverflow.com/questions/2670639/why-are-hexadecimal-numbers-prefixed-with-0x)