---
title: python에서 작업한 내용을 바로 피피티로 옮기자!
category: python-lib
tags: python-lib python power-point python-pptx not-yet  not-yet

---

## 왜 이런짓을 하죠? 

- 저는 보통 대부분의 작업을 맥에서 하는데요(윈도우 마우스 쓰기 싫어요 손목 아파여). 맥에서도 물론 마소 오피스를 쓸 수 있지만, 썩 마음에 들게 워킹하지 않아요. 반드시 마우스를 써야 하는 것도 그렇고. 
- 엑셀의 경우는 그래도 어느 정도 안 쓰고 데이터를 읽고 쓰고 할 수 있는데 피피티는 이게 잘 안되요. 그런데 데이터를 분석해서 결과를 (제목, 짧은 글, 그림)의 형태로 넘겨주면 이 각각의 값마다 슬라이드를 만들면 되게 편할 것 같아요. 제 생각에는. 
- 그래서 한번 해보려고요 하하핫

## 일단 남들이 이미 하지 않았는지 찾아봅니다. 

- 사실 이게 좋은 습관인지는 모르겠는데, 뭔가를 하기 전에는 이전에 비슷한 무엇이 있는지를 항상 찾아봅니다. 뭔가를 하려고 찾아보면 이미 남들이 해놓은게 있더라고요. 사실 잘하지는 못해도 본업이 연구자인 입장에서, 기존에 무슨 연구를 했는지 파악하는 것은 중요합니다(라고 변명합니다).
- [python-pptx](https://python-pptx.readthedocs.io/en/latest/)라는 게 있습니다. documentation이 있고, 그래도 비교적 최근(2018년 4월)까지 업데이트가 되고 있습니다. commit 수도 1900을 넘었는데, 높다고 해야할지 낮다고 해야할지 애매하네요. 새로운 라이브러리를 익숙해지는 데는 비용이 들어갑니다. 사실 `pandas`의 경우에도 다양한 방법들이 있는데, 만약 해당 라이브러리를 사람들이 많이 쓰지 않는다면 배울 필요가 있을까요? 
- 아무튼, 그래도 [hello world to python-pptx](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html)을 보니 비교적 쉬운것 같아요. 쉽게 할 수 있을 것 같긴 하군여. 

## install it

- `pip install python-pptx` 네, 저는 pip 종료를 맹신합니다. 사실 `conda`와 `pip`간의 충돌이 발생하지는 않나, 궁금하곤 한데, `conda`가 있으면 `conda`를 하고 없으면 `pip`를 합니다. 둘다 되길래 그냥 막 써요...이럼 안되는데 사실.ㅠㅠ
- 저는 macOS High sierra 를 쓰고, 파워포인트는 2015버전을 씁니다. 

## requirement

- 제가 원하는건 사실 다음이 다입니다. 비교적 간단한 것 같아요. 
    - 제목 넣기 
    - 짧은 글 넣기
    - 그림 넣기
        - 단 여기서 `matplotlib`로 만든 그림을 저장하지 않고 바로 넘길 수 있으면 좋을것 같은데 그게 되려나 모르겠군여 흠
        - [역시 stackoverflow에 있습니다]만, 말한대로 되지 않네요. 이후에 설명하겠습니다. (https://stackoverflow.com/questions/43875424/save-matplotlib-graph-in-a-ppt-file-using-python-pptx-without-saving-figure)
    - 만약 제목 글, 그림 등이 겹치거나 한다면 알아서 크기 조절할 수 있도록 하기 
- 아마도, 파워포인트 자체는 객체화되어 있을텐데, 손쉽게 할 수 있지 않을까요? 

## 역시 잘됩니다. 

- 한글을 넣어도 잘 됩니다. 저는 (`title`, `body`(본문), `img_file_name`)이 개별 element이 리스트를 입력받아서 각 슬라이드를 만들어주는 프로그램읆 만들려고 합니다. 간단하게 다음처럼 만들었습니다. 
```python
from pptx import Presentation
from pptx.util import Inches

def make_ppt(out_ppt_name, content_lst):
    # Presentation()을 일종의 템플릿 객체
    this_prs = Presentation()
    """
    slide_layout[0]는 title, subtitle로 구성된 제목 슬라이드 
    slide_layout[1]는 title, text로 구성된 일반적인 슬라이드 레이아웃
    """
    slide_layout = this_prs.slide_layouts[1] 
    for title, content, img_file_name in content_lst:
        this_slide = this_prs.slides.add_slide(slide_layout)
        shapes = this_slide.shapes
        shapes.title.text = title
        shapes.placeholders[1].text = content
        # placeholders는 개별 slide에 있는 모든 개체를 가져온다고 보면 됨. 
        #shapes.add_picture(img_stream, left, top, height=height)
        #shapes.add_picture(img_file_name, left=Inches(5), top=Inches(10))
        shapes.add_picture(img_file_name, Inches(2.5), Inches(3.2))
        # 변환하지 않고 숫자로 넘기면 잘 되지 않는다. 
    this_prs.save(out_ppt_name)
```

- 다음은 피피티에서 텍스트가 있는 부분만 긁어서 리스트로 가져오는 경우를 말합니다. 리턴하는 결과물은 리스트 오브 리스트 입니다. 

```python
def extract_all_text_from_ppt(file_path):
    # read file 
    try: 
        this_prs = Presentation(file_path)
        lst_of_lst = []
        for slide in this_prs.slides:
            each_lst = []
            for p in slide.placeholders:
                if p.has_text_frame: # slide 에 있는 다양한 요소 중에서 text-frame이 있는 경우에 대해서만 고려 
                    each_lst.append(p.text)
            lst_of_lst.append(each_lst)
        return lst_of_lst
    except:
        print("file path is not correct")
```

## `matplotlib`에서 그림을 따로 저장하지 않고 바로 넘기는 것 

- 매번 파일을 새로 로컬 디렉토리에 저장해두는 것이 내가 생각할 때는 의미가 없다고 생각하기 때문에 buffer에서 바로 pptx에 그림 첨부하는 형식을 선호한다. 항상 IoT다!!
- 아무튼 그러려고 찾아보다 보니, maplotlib.pyplot에서 만든 그림을 파일로 저장하는 것이 아니고 bytestream에 저장하고 이것을 읽어들일 수도 있지 않을까? 라는 생각이 들었다. 
- 아래 도큐멘테이션에서도 `file-lie object`로도 접근이 가능하다고 했습니다만, 안됩니다. 

- `add_picture(image_file, left, top, width=None, height=None)`

> Add picture shape displaying image in image_file. image_file can be either a path to a file (a string) or a file-like object. 

### 뭐가 안됩니까? 

- file like object를 넘기면 된다고 했으니까, bytestream 이나 stringstream을 넘겨도 상관없을 거라고 생각합니다. 
- 하지만 다 안됩니다.

### `io.BytesIO`로 넘기는 경우 

- 안됩니다. 에러메세지가 길어서 다음에 확인해 보시고, 대략 `cannot identify image file <_io.BytesIO object at 0x111d54678>` 이 부분입니다. 한글로 말하면 이미지 파일을 식별할 수 없다는 이야기네요. 
- `io.StringIO`로 해도 차이 없습니다. 
- 글로 이것저것 해봤지만 안됩니다. 그냥 저는 이쯤에서 포기하고 이미지 파일로 읽어서 처리하겠습니다. 

```python
import matplotlib.pyplot as plt
import numpy as np
plt.close('all') # figure가 너무 많아지면 지워주는 것이 필요함. 

from io import BytesIO, StringIO

byte_stream = BytesIO()
plt.savefig(byte_stream)

img_prs = Presentation()
img_slide = img_prs.slides.add_slide(img_prs.slide_layouts[1])
img_slide.shapes.add_picture(byte_stream, Inches(2.5), Inches(3.2))
img_prs.save('test.pptx')
```

## 기타 문제점들 

- `png`는 인식하지만, `svg`는 인식하지 못합니다. 따라서 `dpi`를 높여서 저장해야 할것 같습니다. 

## reference

- [python-ppt documentation](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html)