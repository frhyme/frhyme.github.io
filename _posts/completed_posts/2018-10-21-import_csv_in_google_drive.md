---
title: google collaboratory에서 google drive의 파일 읽기
category: python-libs
tags: python python-libs google collaboratory csv google-drive jupyter-notebook 
---

## intro 

- local에서 jupyter notebook을 쓰다가, 이제는 google collaboratory로 완전히 넘어가기로 결정했습니다. 
- 다양한 이유가 있지만, 
    - 우선 구글 드라이브 내에 쥬피터 노트북+관련 문서 들을 함께 관리할 수 있어서 편하고 
    - 로컬에서는 매번 쥬피터노트북을 서버로 키고, 또 문서도 따로 키우고 해서 귀찮았는데, 이제 모두 크롬 브라우저+구글 드라이브를 사용해서 모두 처리할 수 있고
    - 제 맥북 에어에 비해서 별로 느린것 같지 않습니다 허허허허. 제 맥북은 진짜 꾸졌거든요 쿠쿠쿠 

- 아무튼 이러한 이유로 jupyter notebook에서 collaboratory로 넘어가려고 합니다. 

## 문제 발생!!

- 그런데, 약간은 성가신 문제가 생겼습니다. 
- 보통 로컬에서 코딩할 때는 로컬에 있는 파일을 읽을 때 권한등의 문제가 발생하지 않습니다. 
- 즉 그냥 `pd.read_csv('aaa.csv')`를 하면 된다는 이야기죠. 그런데 collaboratory에서는 조금 다릅니다. 

- 생각을 해보면, 제가 google collaboratory 파일을 만들면, 그 파일은 Docker로 인해 만들어지는 어떤 가상의 환경에서 돌아갑니다. 그 가상의 환경은 제 로컬 파일은 물론, collaboratory 파일이 속해있는 google drive와도 분리되어 있죠. 
- 즉, 개념적으로는 제가 만든 collaboratory 파일이 구글 드라이브 내 폴더에 존재해 있어서, 당연히 그냥 `pd.read_csv`를 하면 될 것 같지만, 안된다는 거죠.
- 그래서 제 도커 환경에서 구글 드라이브를 읽을 수 있게 세팅해줘야 합니다.

## Mounting google drive locally

- [collaboratory는 이미 문서화가 상당히 잘 되어 있습니다](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=JiJVCmu3dhFa).
- 해당 문서를 보시면, 비교적 간단한 코드인 다음 코드를 사용해서 구글 드라이브를 제 도커환경에서 인식하도록 할 수 있습니다. 

```python
# Load the Drive helper and mount
from google.colab import drive
"""
- This will prompt for authorization.
- force_remount=True 는 강제적으로 mount를 재개할 때 사용합니다. 
- 또한 drive 내 다른 폴더를 mount point로 지정할 수는 없는 것 같습니다. 
"""
drive.mount('/content/drive')
```

- 그다음에 다음을 실행해서 파일들을 읽거나 하시면 됩니다 

```python
os.listdir("/content/drive/My Drive/")
```

## should not upload gsheet

- 먼저, 저는 csv 파일을 자주 읽습니다. 
- 그래서 google drive에 csv 파일을 업로드하면, 이게 csv로 인식되는 것이 아니라, 자동으로 google sheet로 인식이 됩니다. 
- 뭔 상관이냐, 싶겠지만, collaboratory에서 gsheet를 읽는 것과, csv를 읽는 것은 차원이 다른 문제로, gsheet를 읽으려면 gspread를 사용하거나 해야하죠. 

- 간단하게 설정에 들어가면 아래와 같은 설정이 있는데, 이를 체크해주지 않으시면 됩니다. 

> 업로드 변환, 업로드된 파일을 Google 문서편집기 형식으로 변환 

- 그럼 csv가 자동으로 gsheet로 변환되지 않고 업로드되며, 훨씬 편하게 코딩할 수 있습니다. 

## wrap-up

- 뭐, 당연히 이유는 있겠지만, 약간은 성가시군요. 
- 그런데 그래도 이렇게 분리해두는 것이 더 타당하게 느껴지기는 합니다.




## reference 

- <https://productforums.google.com/forum/#!topic/drive/qZOCSZJ0MrY>
- <https://colab.research.google.com/notebooks/io.ipynb#scrollTo=u22w3BFiOveA>