---
title: python에서 데이터 암호화하기
category: python-lib
tags: python python-lib RSA AES Crypto PyCrypto
---

## intro

- http와 https 간의 차이점을 정리하고 있었는데, https는 공개키 암호화방식을 사용하여 데이터를 암호화한다고 하더라고요. 그래서, 여기서 '공개키 암호화방식'이 무엇인지 정리해보려고 합니다. 
- 뿐만 아니라, 간단하게 python으로 알고리즘을 사용해봐야 제가 정확하게 이해할 수 있을 것 같아서 파이썬에서 이를 어떻게 활용하는지도 함께 정리해보려고 합니다. 

## 공개키 암호화 방식

- 공개키 암호화방식은 "암호학적으로 연관된 두 개의 키"를 만들어서 하나는 자신이 보관하고 다른 하나는 상대방에게 공개하는 식으로 이루어진다고 합니다. 
    - 상대방에게 공개되는 키를 public key라고 하고, 자신이 보관하는 키를 private key라고 합니다.
    - "암호학적으로 연관된"이라는 말이 무슨 말인지 모르겠지만 일단 넘어갑니다. 

- 아래 그림을 보시면, "Hello Alice"라는 데이터를 송신자(sender)가 수신자(receiver)에게 보낼 때는 이미 공개되어 있는 수신자의 공개키를 가지고 변환을 하고 변환된 데이터를 전송하게 됩니다. 이후 해당 데이터를 읽어들일 때는 공개키가 아니라 수신자만 가지고 있는 private key를 가지고 원래 데이터로 변환을 하게 되죠. 
    - 공개키: 원래 데이터를 암호화할 때 사용 
    - 비밀키: 암호화된 데이터를 원래 데이터로 복원할때 사용 

![](https://www.lesstif.com/download/attachments/18219486/image2014-7-29%2023%3A33%3A40.png?version=1&modificationDate=1406644244000&api=v2)

- 공개키 암호화방식은 따라서 '비대칭 암호화방식'이라고 하기도 합니다
- RSA가 공개키 암호화 알고리즘 이라고 합니다. 

## RSA 

- 대표적인 공개키 암호화 알고리즘인 RSA를 설명해보겠습니다. 
- 아래 그림에서 KU는 공개키이고, KR은 비밀키입니다(물론 공개키와 비밀키를 잘 찾는 것이 제일 중요합니다)
- 일단은 아래와 같은 방식으로 진행된다는 사실만 알고 계시면 될 것 같습니다.

![RSA algorithm](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwi0lLeO9I7cAhUCVbwKHX3IA48QjRx6BAgBEAU&url=https%3A%2F%2Fwww.nexg.net%2Frsa-%25EC%2595%2594%25ED%2598%25B8%25ED%2599%2594-%25EC%2595%258C%25EA%25B3%25A0%25EB%25A6%25AC%25EC%25A6%2598%25EC%259D%2598-%25EC%259D%25B4%25ED%2595%25B4%2F&psig=AOvVaw205QMqa2SOinSyKNAWraOp&ust=1531118765073162)

### rsa do it

- 직접 코딩한 부분은 [여기서](https://gist.github.com/JonCooperWorks/5314103) 보시면 됩니다. 
- 저는 귀찮기 때문에....그냥 잘 만들어져 있는 라이브러리를 직접 써보기로 했는데요. 

```python
import Crypto
from Crypto.PublicKey import RSA
## 일단 random_generator를 만들어서 넘겨주어야 합니다. 
#random_generator = Crypto.Random.new().read
msg = "I am a boy, you are a girl hi man"*2
bin_encoded_msg = msg.encode()
print('==binary encoded msg==')
print(bin_encoded_msg)
print("="*20)
## key를 만들어줍니다. 
## 어느정도의 크기로 만들어줄지 값을 세팅. 단 값이 len(msg)보다 커야 함 
## 또한 256의 배수, 최소 1024 
s = 1024 if len(bin_encoded_msg)*8 <1024 else 2**int(math.log(len(bin_encoded_msg), 2)+1)*8
key = Crypto.PublicKey.RSA.generate(s)
publickey = key.publickey()#.exportKey("PEM") 

print('==Public key==')
print(publickey.exportKey("DER"))
print("="*20)

print('==Private key==')
print(key.exportKey('DER'))
print("="*20)

ciphered_msg = publickey.encrypt(bin_encoded_msg, 32)[0]
print('==Ciphered msg==')
print(ciphered_msg)
print("="*20)

deciphered_msg = key.decrypt(ciphered_msg)
print('==deCiphered msg==')
print(deciphered_msg)
print("="*20)
```

```
==binary encoded msg==
b'I am a boy, you are a girl hi manI am a boy, you are a girl hi man'
====================
==Public key==
b'0\x81\x9f0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x81\x8d\x000\x81\x89\x02\x81\x81\x00\xd0\x1c\x89\xf6\r\t(N\x00;\x84cH1\xb4\x04\xaa/v\xf5EyVh&\x99\x14C\xe3\xa7v\xf7^\xba\xdf_7+\x18\xafr\x19\xc8\xb7\x03`\xc0\xcd\x13\x86\xea~\x85\xf4w-\x9f\x10\xfa\x9d\xa7\x85\xb4n8_R\x00d\xa2\xab\xa6\xdd\xe3\xea\xe9\x8f\x0e\x98-&\xd6\x9cE@\xfe\xc5\x8d\x00\x8bd\x0b_\x11R\xffX`\xca\xb9\xe2\xca~S\xba\xf5\xa8\x96\xed\xc2{n\xa2\xa7|?r\xe0B\xfa\xdc\x03\x8b"\x1c\x87\xda\xb5\x02\x03\x01\x00\x01'
====================
==Private key==
b'0\x82\x02]\x02\x01\x00\x02\x81\x81\x00\xd0\x1c\x89\xf6\r\t(N\x00;\x84cH1\xb4\x04\xaa/v\xf5EyVh&\x99\x14C\xe3\xa7v\xf7^\xba\xdf_7+\x18\xafr\x19\xc8\xb7\x03`\xc0\xcd\x13\x86\xea~\x85\xf4w-\x9f\x10\xfa\x9d\xa7\x85\xb4n8_R\x00d\xa2\xab\xa6\xdd\xe3\xea\xe9\x8f\x0e\x98-&\xd6\x9cE@\xfe\xc5\x8d\x00\x8bd\x0b_\x11R\xffX`\xca\xb9\xe2\xca~S\xba\xf5\xa8\x96\xed\xc2{n\xa2\xa7|?r\xe0B\xfa\xdc\x03\x8b"\x1c\x87\xda\xb5\x02\x03\x01\x00\x01\x02\x81\x80z\xdd\x9e\x85\xe9\xc4RKZ\xcf\xc8\xa5d\xe6\x13E\xfd\xc3\xf0\x13vd\xe0\xa2\xb4\xc7\x03\xb3\xe1\x1f\xe9\x98\xba\x10\xd1\xf7\xc0\xf6l\xa8\x88P\xb8\xb3t\x07\x17L\xfc\x0eW;C\x92\xc5\x19\xe6#|\x12\xbf\xe8\xacP\xa5\xcb\xda\xf3%\x8c\xb9\xb9\x81\t\xd5\xf4k\x9az\xf7\xd1V.\xfbm\xc3:n\x03,r\x97\xaf"z\x86\xa5A\x16\x01{\xa8\reeMj\xb1\x1a\x03I\xeb\x19\x86\xc75W\xde;q\xbb=~\xfb\x05I\xf61\x02A\x00\xe0\xd8\xab\xb5I\xe6eh\x8a\x19\xd5\x87m\x90\xeb\x96\x10>\xa6+j\x83\xa9\x91\xa59\r\xd5S\xcc\x06!\x8d\xc7s#~\xe8\x91\'\x03\x91\x87\x7f\xec\x81\xa6\x8f\x8e\xfa\x14V\xbd/\xbbz\x06\x9fR\x84\x8f\xce5\x9b\x02A\x00\xec\xf2G\x8d\xc4|I*\x97\x9f\xe7\x80\xfa\xace%\x12\xbe,\xdf\xa9r\x15T\xb1\x80\xd3\'J\x96\x90\x87\xf0d\xb5\x12\xa2b9N\\\xce\xcf\xb7\xef\xbb\x05\xd7\xd4:2r\xb4\xdf8\x07 \xb7\x99W\xd6\x87\xdd\xef\x02A\x00\xc2\x0b[\xcc\xbd\xf5?IC\xfd\xdd\xa0\xdd\xf6\xf6\xc9\xf0E\x11\x05a\x0c5\x98C^\x04\xc99cW[7\xcf\x8cWr\xdb\xe5\x01%|?\xd3/\xda\x08S\xd6\x91\x8ea\xf9-\xab\x7f9\x1d\xe0\x8a\x14\xcdb\xc7\x02A\x00\xe4\n\xa1v\xfd\x9d\xa8EG\xbck\xf0$Qz\xde\xddU\x0e\x97\x0b\xdbrP\x1a\xad\xa3\x8a\xf3,IY\xab\xb1 \xdc\x18PtZ\xc8\xd3y\xf2\xca\xd4\xb2`\xf0.:\x93O$n%\xde\x05\x15\x9e\x06(\xa9\x1d\x02@7\xcd\xed$LO\xf9\x03.k"\x91w\x8a\xa8\r\xea^\xear[8\xeepD\xd4\xba\x99/\x17\xee\x80\x12M\x01`W\xf68W30\x1d&o\xe2P3\xf5\x03S\xe5HV\x8c\x15\xde\xbdG6C2?\x1f'
====================
==Ciphered msg==
b"#\x1f\xa8\x85\xa5\x14i\x87j\x99z\xd5s\nn\xae|\x8a\xf4\x1f!\x03$.8BA\xd9\xe5\x94\xb3\xf2\xces\x0ca2\xe2\x95d\xf4\xe8\xedj\x01\xf8,\x19\xd0\xcbF\xe4\xcar\t^\x15\xa9'\x1a\xf66R\xe7\xf5,\x8d@\x1cA\xd2\xad\xb4q\x84\xa0\x9aT<\xef\x16\xb4A\xa7W\xcf\xab\x8d\xb1\xe40B\xa4~t\xf5''\xaa\x13\xb3=\xc574|\xb6\x166\xcd0\xd2\x8e\x90t\xb8\xed\x19\x1f\xafVj\x07<\xe9\x01\x8do"
====================
==deCiphered msg==
b'I am a boy, you are a girl hi manI am a boy, you are a girl hi man'
====================
```


## 대칭 암호화방식

- 공개키 암호화방식의 경우는 encode(암호화)할때 쓰는 key와 decode(복호화)할때 쓰는 key가 다른데, "대칭 암호화방식"에서는 암호화할때와 복호화할때 쓰는 key가 같습니다. 
- AES(Advanced Encription Standard)가 대칭 암호화방식 알고리즘이라고 하네요. 자세한 내용은 이 [블로그](http://newstein03.tistory.com/1)를 참고하시면 될것 같습니다. 
- 대칭 암호화방식의 강점은 1) 일단 암호화할때 속도가 비대칭에 비해서 훨씬 빠르다는 것, 2) 암호화된 데이터가 기존 데이터와 큰 차이가 나지 않는다는 것 을 말할 수 있습니다. 
    - 다르게 말하면, 비대칭 암호화방식의 경우 대칭 암호화방식에 비해서 암호화된 데이터가 커진다는 것이죠. 
- 따라서 매우 중요한 데이터(키 교환 등)에는 비대칭 암호화방식을 쓰고 일반적인 데이터에는 대칭 암호화방식을 쓰는 형태로 사용하기도 합니다. 

### AES

- 파이썬에서 AES를 사용하여 암호화하기 위해서는 [Pycripto](https://pypi.org/project/pycrypto/)라는 라이브러리를 사용합니다. 
- random하게 `key`와 `iv`를 세팅해주고 크기를 조절합니다. 
    - 정확하게 파악하지는 않았지만, AES의 경우는 약간 컨볼루션-풀링처럼 텍스트들을 매트릭스 구조로 변환해서 처리하는 것처럼 보입니다. 
    - 따라서 크기들이 16에 맞춰서 정리되는 것이 필요한 것 같아요. 

```python
import Crypto

original_message = "I am a boy"
if len(original_message)%16!=0:
    original_message+= " "*(16 - len(original_message)%16)
original_message = original_message.encode()

key = Crypto.Random.new().read(16) 
iv = Crypto.Random.new().read(16)

cipher_ = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, iv)
## original message의 length가 16의 배수여야함 

## 들어오는 string의 길이가 16의 배수여야 함
ciphered_message = cipher_.encrypt(original_message)

## 새롭게 세팅해줘야함 
cipher_ = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, iv)
deciphered_message = cipher_.decrypt(ciphered_message)

print("-"*30)
print("original   msg: {}".format(original_message))
print("-"*30)
print("ciphered   msg: {}".format(ciphered_message))
print("==> to utf-16 : {}".format(ciphered_message.decode('utf-16')))
print("-"*30)
print("deciphered msg: {}".format(deciphered_message))
print("-"*30)
```

```
------------------------------
original   msg: b'I am a boy      '
------------------------------
ciphered   msg: b'\x9f\xb7\xb9\x87\xf9\x92\x02\xb8E_\xc9\x8c\x1f\xc5\xa4\xf7'
==> to utf-16 : 랟螹鋹렂彅賉씟
------------------------------
deciphered msg: b'I am a boy      '
------------------------------
```

## reference

- <https://medium.com/@ismailakkila/black-hat-python-encrypt-and-decrypt-with-rsa-cryptography-bd6df84d65bc>

- <https://gist.github.com/JonCooperWorks/5314103>
- <https://sahandsaba.com/cryptography-rsa-part-1.html>
- <https://lesstif.gitbooks.io/web-service-hardening/content/public-key-encryption.html>