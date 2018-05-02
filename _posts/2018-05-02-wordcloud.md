---
title: wordcloud를 만들어봅시다. 
category: python-lib
tags: python python-lib PIL wordcloud

---

## wordcloud가 뭘까여

- 보통 이런걸 워드클라우드라고들 하지요. 
    
    ![python_wordcloud](http://sebastianraschka.com/images/blog/2014/twitter-wordcloud/my_twitter_wordcloud_2_small.jpg)
- 파이썬에서 워드클라우드를 만들수 있다고 해서 정리해보았습니다.
- 일단 해당 라이브러리를 `conda install -c conda-forge wordcloud` 일단 설치를 합시다.

## simple example 

- 텍스트를 `WordCloud().generate()` 객체에 넣어주고, 다음을 실행하면 실행됩니다. 어렵지 않아요. 
- 단 입력된 text에서 자동으로 noun이 필터링되고 verb 등은 걸러집니다. 사이즈는 알아서 조절되고요.

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt
%matplotlib inline

text = "coffee phone phone phone phone phone phone phone phone phone cat dog dog"

# Generate a word cloud image
wordcloud = WordCloud(max_font_size=100).generate(text)

# Display the generated image:
# the matplotlib way:

fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/wordcloud_ex1.svg')
```

![](/assets/images/markdown_img/wordcloud_ex1.svg)

## Image colored wordcloud 

- 그런데 위는 그냥 직사각형에 그대로 들어가서 별로 안 예쁜것 같습니다. 
- 예쁘게 만들려면 다음처럼 해주면 됩니다. 하하 참 쉽죠. 
- 원하는 이미지로부터 이미지 매트릭스를 가져오고, 
- 그 값을 넣어주면 모양과 색깔이 비슷하게 들어갑니다. 하하

```python
import requests
def read_img_from_url_and_return_matrix(url):
    response = requests.get(url)
    #print("binary file sample: {}".format(response.content[:20]))

    from PIL import Image 
    from io import BytesIO 

    img = Image.open(BytesIO(response.content))
    img_matrix = np.array(img)
    # plt.imshow(img_matrix)
    # img.save('aaa.png')
    return img_matrix

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

def make_ImageColoredWordcloud(text, img_matrix, outputfile_name):
    wc = WordCloud(background_color="white", max_words=2000, mask=img_matrix, max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)
    f = plt.figure(figsize=(20, 20))
    plt.imshow(wc.recolor(color_func=ImageColorGenerator(img_matrix)), interpolation="bilinear")
    plt.axis("off")
    plt.savefig(outputfile_name)
    
url = "https://amueller.github.io/word_cloud/_images/sphx_glr_colored_003.png"
img_matrix = read_img_from_url_and_return_matrix(url)
text = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)").text
make_ImageColoredWordcloud(text, img_matrix, '../../assets/images/markdown_img/'+'coloredWordCloud.svg')
```
![](/assets/images/markdown_img/coloredWordCloud.svg)

## reference 

- [Documentation](https://amueller.github.io/word_cloud/)