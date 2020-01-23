---
title: cURL을 알아봅시다. 
category: others
tags: python command bash http protocol curl python-lib subprocess requests 
---

## 너는 왜 또 갑자기 curl을 정리했느냐. 

- 왜 갑자기 cURL인가요? 라고 물으실 것 같습니다. [blockchain을 좀 파고 있었는데](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d), 중간에서 블록체인을 만들고, mining하고 할 때 http프로토콜을 이용하거든요. 그런데 이때, 터미널에서 `curl` 이라는 커맨드를 사용합니다. 그래서 이 아이는 무엇인가? 하고 조금 정리를 해봤습니다. 

## what is cURL.

- 언제나 정보는 이미 [위키피디아](https://en.wikipedia.org/wiki/CURL)에 나와 있습니다. 이를 조금 정리하면 다음과 같아요. 

> URL is a computer software project providing a library and command-line tool for transferring data using various protocols.

- 데이터를 다양한 프로토콜(http, ftp 등)에 맞춰서 전송할 수 있는 라이브러리와 **커맨드라인 툴**이다 라는 이야기죠. 라이브러리야 파이썬에서도 `requests`라는 좋은 라이브러리가 있습니다만, **커맨드라인 툴**이라는 건 이야기가 다릅니다. 
- 예를 들면 다음처럼 bash에서 실행할 수 있습니다(저의 경우는 따로 설치하지 않았는데 이미 설치되어 있더군요). 
    - 일단 제가 [임의의 텍스트를 하나 gist에 만들었습니다](https://gist.githubusercontent.com/frhyme/22b8f1dddb53462ca24e9c89f2589e26/raw/fcb152089ac4b65605b3a9e76490bff8e569cb93/gistfile1.txt). 
- 단순하게 curl + url 을 아래처럼 입력하면, 

```bash 
curl https://gist.githubusercontent.com/frhyme/22b8f1dddb53462ca24e9c89f2589e26/raw/fcb152089ac4b65605b3a9e76490bff8e569cb93/gistfile1.txt
```

- 아래처럼 해당 url의 텍스트를 모두 긁어옵니다. 

```bash
## this is test for curl
## second line
## by frhyme
```

- 즉, 이미 우리가 알고 있던 python에서의 `request` lib와 매우 유사하게 동작한다고 할 수 있습니다. 

## curl in python

- 물론, 요즘의 사람들은 command line에서 작업하는 일보다, IDE에서 작업하는 일들이 더 많다고(우물안 개구리인 저는 이렇게 말합니다). 따라서 IDE에서 curl을 직접 사용해보도록 할게요(물론, `requests`를 쓰는게 더 좋을 수도 있습니다만)

- 아래 코드에서 보시는 것처럼 subprocess를 이용하면, bash command를 직접 실행해볼 수 있습니다. 또한 그 결과를 리턴받아서, utf-8로 디코딩해서 출력해봅수도 있죠. 출력 결과는 매우 길어서 굳이 집어넣지는 않았습니다. 

```python
import subprocess

for cmd in ['curl https://en.wikipedia.org/wiki/CURL']:
    output = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
    print("## command: {}".format(cmd))
    print(output)
    print("-"*30)
```

## wrap-up

- 저는 그냥 '이렇게 할 수 있다' 정도만 소개한 것이고, 실제로는 해당 프로토콜을 통해 데이터를 읽어와서 데이터를 쓰고, 다른 파일에 쓰고, 하는 등 여러 가지가 가능해요. [상세한 사용법은 여기를 참고](https://www.lesstif.com/pages/viewpage.action?pageId=14745703)하시면 좋습니다. 


## reference

- [curl 자세한 이용법](https://www.lesstif.com/pages/viewpage.action?pageId=14745703)