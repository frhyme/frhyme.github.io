---
title: 웹에서 이미지를 읽읍시다. 
category: python-lib
tags: python-lib python image requests PIL

---

## 웹에서 이미지를 읽어봅시다

- 개발을 하다보면 웹에서 이미지를 가져와야 할 때가 있습니다. 저는 바보라서 그냥 `open('http://~~~', 'r')`로 해도 되지 않을까? 라는 바보같은 생각을 한 적도 있습니다ㅠㅠ당연히 안되죠. 
- 일반 텍스트는 보통 `requests.get(url)`을 사용해서 비교적 쉽게 크롤링할 수 있었는데, 이미지는 조금 다른 것 같습니다. 
- 우선 왜 그럴까요? 이미지는 바이너리로 되어있기 때문이라고 합니다. 여기서 뭔가 더 궁금한 점들이 있지만, 더 파고들어가면 심연의 끝자락으로 빠질 수 있을 것 같아서 더 파고들어가지 않으려고 했는데, 궁금하군여...

## binary 파일이 뭔가요? 

- [여기에 설명이 잘 되어있네요](http://mwultong.blogspot.kr/2006/09/text-file-binary-file.html). 정리하자면 일반적인 텍스트 파일들은 **아스키 코드**를 활용하여 표현이 되어있다면, 이미지, exe 파일등은 **바이너리 코드**로 표현이 되어있습니다. 정확히는 헥사 코드(16진법)이 더 정확하겠네요. 
- 변환 방식이 다르기 때문에, 텍스트 파일과 바이너리 코드는 다른 방식으로 읽어들여야 합니다. 
- 아무튼, 웹에서 데이터 자체는 긁어올 수 있는데, 그럼 이걸 binary로 읽어 처리해야겠네요. 

## solve it.

- 해당 `requests`를 사용해서 url로부터 내용을 가져옵니다. 
- 가져온 내용을 `io.BytesIO`를 활용하여 바이너리스트림 형태로 만듭니다(임시로 바이너리파일을 저장했다고 생각해도 됩니다)
- `PIL.Image`에서 해당 파일을 열면 이미지 파일이 제대로 읽어들여졌습니다. 
- `PIL`을 이용해야 이미지를 매트릭스의 형태로 변환하는 것이 쉽습니다.

```python
import requests
url = "https://amueller.github.io/word_cloud/_images/sphx_glr_colored_003.png"
response = requests.get(url)
print("binary file sample: {}".format(response.content[:20]))

from PIL import Image 
from io import BytesIO 

img = Image.open(BytesIO(response.content))
img_matrix = np.array(img)
# plt.imshow(img_matrix)
# img.save('aaa.png')
```

```plaintext
binary file sample: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x80'
```

## reference 

- <https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python>