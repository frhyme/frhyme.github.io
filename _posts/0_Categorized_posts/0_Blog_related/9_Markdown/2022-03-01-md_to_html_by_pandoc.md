---
title: Pandoc를 사용하여 markdown file을 html로 변환하기 
category: markdown
tags: markdown pandoc html
--- 

## Pandoc - Convert markdown to html

- [pandoc](https://pandoc.org/index.html)은 "Universal markup converter"로 조판 문법은 다르지만 비슷한 애들을 변환해주는 도구, 라고 해석하시면 됩니다. 가령, markdown과 html은 markup syntax는 다르지만 각 요소의 의미는 동일하다고 볼 수 있는데요. 이 경우 markdown에서 heading으로 표시된 부분을 html에서 heading으로 표시해주도록 변환해주는 것을 말하죠. 
- pandoc을 설치하려고 보니, 이미 설치되어 있습니다. 제가 언제 설치했는지는 모르겠네요. 현재 설치되어 있는 버전은 다음과 같습니다.

```sh
$ pandoc -v
pandoc 2.2.3.2
Compiled with pandoc-types 1.17.5.1, texmath 0.11.0.1, skylighting 0.7.2
Default user data directory: /Users/seunghoonlee/.pandoc
Copyright (C) 2006-2018 John MacFarlane
Web:  http://pandoc.org
This is free software; see the source for copying conditions.
There is no warranty, not even for merchantability or fitness
for a particular purpose.
```

- 사용법은 간단합니다. 아래처럼 그냥 파일명만 명확히 명시해주면 알아서 변환해줍니다.
  - `-o`: output을 의미하며, 변환 결과가 담길 파일명을 명시합니다. 이 argument로 넘어가는 파일명에 띠라 변환형식이 결정됩니다.
  - `-f`, `-t`: 기본적으로는 from, to 를 정해서 어떤 문서 형식에서 어떤 문서 형식으로 변경해줄지도 정해줘야 합니다. `pandoc a.md -f markdown -t html -o a.html`이 명확하겠죠. 하지만, 파일 이름에서 대략 유추할 수 있어서 이 부분은 굳이 명시해주지 않아도 알아서 넘어가는게 아닐까 싶습니다.

```sh
$ pandoc a.md -o a.html
$ pandoc a.html -o a.md
$ pandoc a.html -o a.pdf
```

- pdf의 경우로도 변환이 가능하지만, pdf로 변환하려면 pdf 변환 엔진이 따로 필요한 것 같네요.

```sh
$ pandoc cccc.html ddd.pdf
pandoc: ddd.pdf: openBinaryFile: does not exist (No such file or directory)
```

## Wrap-up

- 처음에는 markdown 파일을 만들고 블로그에 올리기 전에 html로 만들어서 확인해보자는 마음으로 이 글을 작성했는데요. 생각해보니. 그냥 `bundle exec jekyll serve`를 사용해서 블로그를 띄우는 게 낫지 않나 싶기도 합니다. 라고 말하고 실제로 블로그를 띄워보니 생성되는 게 드럽게 느리네요. 언제 한번 정리하고 갈아타고 해야되는데, 블로그 갈아치우는 작업은...아시죠? 너무 힘들어요.
- 보고 그냥 pandoc을 사용해서 html로 변환한 다음 브라우저로 접속해서 잘되는지 대충 보는 것도 나쁘지 않을 것 같습니다 호호.  

## Reference

- [pandoc.org](https://pandoc.org/index.html)
- [wikipedia - Pandoc](https://en.wikipedia.org/wiki/Pandoc)
