---
title: Mermaid Test
category: mermaid
tags: mermaid
---

## What is mermaid? 

- [mermaid](https://mermaid-js.github.io/mermaid/#/)는 마치 html을 보다 간편한 문법인 Markdown을 통해 그릴 수 있도록 해준 것처럼, 복잡한 diagram을 마치 마크다운처럼 편한 문법으로 그릴 수 있도록 해주는 tool입니다.
- 가령, 아래와 같은 mermaid 문법을 `mermaid` 태그와 codeblock으로 작성해주면 diagram으로 그려주죠.

```plaintext
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

- 처음에는 VScode에서 간단하게 사용했습니다.
  - [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)를 설치하여, Markdown Preview를 눌렀을 때, Diagram이 그려지도록 처리하고.
  - [Mermaid Markdown Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting)를 사용하여, 문법들에 대해서 highlight해줬습니다.
- 그런데, 이렇게만 쓰지 않고 github 블로그에서도 사용해보려고 합니다.

## Rendering Mermaid in jekyll

- 저는 jekyll을 사용하고 있기 때문에, jekyll에서 mermaid를 렌더링해야 합니다.
- jekyll에서 Mermaid를 사용하는 방법은 다음 두 가지가 있습니다.
  - [jekyll-mermaid](https://github.com/jasonbellamy/jekyll-mermaid)
  - [jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship)
- 이미 위 두 가지의 방식을 적용해봤지만, 적용되지 않는 것을 발견했습니다. 이는 제가 Github Page를 사용하고 있기 때문이며, [Github plugins - set of whitelisted plugins](https://pages.github.com/versions/)에 두 plugin이 존재하지 않기 때문입니다. 즉, github page에서는 이 두 plugin에 대해서 허용해주지 않는다는 이야기죠.
- 따라서, plugin을 통해서는 안되고, 우회해서 진행해야 합니다.

### Embedding Mermaid 

- [Mermaid-js](https://mermaid-js.github.io/mermaid/#/)에 들어가보면 해당 js file의 CDN이 존재합니다.
- 각 html 문서 앞에 아래 항목을 공통적으로 집어넣고,

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
```

- html 문서 내에서 mermaid를 사용하는 경우는 다음처럼 표현해주면 될것 같습니다. 그렇게 처리한다면, 될 것 같아요. 

```html
<div class="mermaid"> 
  graph TD; A-->B; A-->C; B-->D; C-->D; 
</div>
```


<div class="mermaid"> 
  graph TD; A-->B; A-->C; B-->D; C-->D; 
</div>


## Reference

- [jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship)
