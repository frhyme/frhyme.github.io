---
title: jekyll에서 마크다운 적용할 때 latex 도 렌더링되게 하기 
category: other
tags: blog jekyll markdown latex
---

## latex 이 뭔가요? 

- 한글 워드 프로세서(정확한 명칭이 뭔지는 모르겠는데)에서 수식을 써보시면 약간 코딩하듯이 수식을 만들 수 있다는 것을 알 수 있습니다. [latex](https://en.wikipedia.org/wiki/LaTeX)는 문서 조판 언어인데(학술계에서 많이 쓰는), 이 중에서 대부분 수식을 표현하기 위해서 많이 씁니다 라고 말할 수 있겠네요(발음은 라텍스 가 아니라 레이텍 이 맞습니다. 라텍스는 어감이 좀....). 
- 마크다운에서도 latex 을 쓸 수 있는 것으로 알고 있는데, 예전에 쓴 [marp](https://yhatt.github.io/marp/)의 경우는 latex으로 표현된 부분을 잘 렌더링해줬거든요.
- 아래처럼 latex의 수식으로 표현하면 알아서 잘 해줬는데, Jekyll에서는 잘 안되는 것 같습니다. 아마도 제가 따로 뭐 설정을 해줘야 하는것 같네요.
```
$$
\sqrt{3x-1}+(1+x)^2
$$
```

- 아래 [이 블로그](https://helloworldpark.github.io/jekyll/update/2016/12/18/Github-and-Latex.html)를 참고했습니다.

## mathjax??

- 문법 자체는 latex을 사용하지만, 사실 latex은 로컬에 설치하는 프로그램입니다. 예전에 저도 한번씩 설치는 했었는데 은근히 오류가 많아서 자주 사용안했던 것 같아요. 또 요즘에는 워드에서도 latex으로 변환한다거나 하는 다른 플러그인들이 워낙 많아서 문제없는것 같고. 
- 아무튼 마크다운에서 latex 언어를 이용해 수식을 입력하려면 `mathjax`를 설치해줘야 한다는 것 같습니다. 
- `mathjax`: **A JavaScript display engine for mathematics that works in all browsers.** 라고 하네요. 
- 간단히, 설치만 해주면 됩니다만, html head 부분에 다음 내용을 추가해주면 됩니다. 

## `mathjax` 설치하기

- layout 폴더의 `default.html` 파일의 head에 아래 코드 부분을 추가하면 됩니다.
- head에 들어가는 부분은 쉽게 말하면, `python`에서 `import` 같은 부분입니다. 이 부분에 다음 내용을 작성해서 붙여넣으면 됩니다. 내용은 저도 모릅니다, 그냥 붙여 넣은거에요 하하핫. 
- 어떤 jekyll theme을 쓰느냐에 따라서 다를 수 있습니다. 참고하시고, 일반 post의 템플릿이 되는 부분에 넣어주시면 됩니다.

```html
<script type="text/javascript" async 
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

### CDN

- CDN은 Content Delivery Network 의 약자입니다. 파이썬에서 import할 때 보통 로컬에 설치되어 있는 library로부터 내용을 가져온다면, CDN으로 가져오는 것은 사용될때, 그때 웹에서 긁어온다고 생각하시면 될것 같습니다. 
- 단 그렇기 때문에 너무 많은 javascript engine을 가져올 경우에는 과부하가 걸려서 페이지 로딩이 오래 걸리거나 하는 일이 발생하지 않을까 싶습니다.

## 자 이제 됩니다. 

- 그래서 이제 됩니다. 아직은 페이지 로딩에 큰 차이가 없는 것 같네요.
- dollar sign 사이에 내용을 넣어주시면 됩니다. 
- 더 자세한 활용법은 [여기](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)를 참고하세용
- 
```
$$
\sqrt{3x-1}+(1+x)^2
$$
```
$$
\sqrt{3x-1}+(1+x)^2
$$

## problem 

- 그런데 이렇게 하고 났더니, `tag` page 에서도 레이텍이 렌더링되는 문제가 발생했다. 
    - archieve, category 모두 괜찮은데 tag에서만 이러함.
- ![latex error screenshot](/assets/images/markdown_images/latex_achieve.png)
- 내부 소스를 보자!

### 어디가 문제인가? 

- backtick 으로 제목에서 표현된 부분이 code block으로 표현되는 것이 아니라, latex로 표현되는 것을 알 수 있당. 

### 해결법

- 제목에 backtick을 쓰지 않는다......ㅠㅠ현재로서는 다른 방법을 못찾겠음...ㅠㅠ



