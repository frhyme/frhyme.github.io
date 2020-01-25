---
title: mac에서 backtick을 편하게 칩시다. 
category: trivia
tags: markdown macOS

---

## intro

- [여기를 참고했스니다, 아니 거의 같아요](https://ani2life.com/wp/?p=1753)
- 맥북에서는 한영전환시에 백틱이 표현하는 것이 다릅니다. 영어로 되어 있을 때에는 backtick 이지만, 한글로 되어 있을 때에는 원화가 표시됩니다. 왜일까요....원화를 쳐야 할일이 세상에 얼마나 있다고, 정 필요하면 웹에서 검색해서 하면 될것 같은데. 

- 다만 [맥에서 원화(￦) 기호를 손쉽고 간편하게 입력하는 방법](http://macnews.tistory.com/4112)는 2016년 2월에 작성된 글인데, 이 당시에만 해도 오히려 맥북에서 원화 기호를 입력하는 방법이 달랐나보네요. 아마 macOS를 업데이트하면서 변경된 것이 아닐까 싶습니다. 

## anyway solution. 

1. `~/Library` 폴더로 이동해서 `KeyBindings` 폴더를 추가합니다. 
    - 이유는 잘 모르겠는데 `Finders`에서 보여지는 경로와 terminal에서 보여지는 경로는 달라요. terminal 에서는 `Library` 폴더가 보이는데, `Finders`에서는 안 보여요. 
2. `~/Library/KeyBindings` 폴더에 `DefaultkeyBinding.dict` 파일을 만들고
3. `DefaultkeyBinding.dict`에 다음 코드를 추가합니다. 
```
{
    "₩" = ("insertText:", "`");
}
```

- 어플리케이션들만 껐다가 켜도 된다고 하던데, 저는 맥 자체를 재시동 한 다음에야 이대로 되더군요. 
- 만약 원래대로 되돌리고 싶으면 `DefaultkeyBinding.dict`파일을 지우시면 됩니다. 
- 추가로 이외에도 여러가지 키 바인딩을 여기서 할 수 있는데, 저는 일단 필요없어서 안합니다하하핫



