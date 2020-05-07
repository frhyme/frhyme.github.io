---
title: VS-code의 sidebar의 font 를 변경합니다.
category: vs-code
tags: vs-code font
---

## Intro

- 얼마전에는 vs-code의 editor 내의 font를 변경했습니다. 전에도 비슷한 이야기를 했지만 민감하지 않은 사람이라면, 그냥 기본 font을 써도 되겠지만 저는 그런 사람이 아니거든요.
- editor 내에서 한글 폰트를 바꾸었고 이제 이전보다 훨씬 가독성이 좋아졌습니다. 이제 남은 것은 오른쪽 sidebar, 즉 file directory를 보여주는 부분의 code를 바꾸려고 합니다.

## Try to change font in sidebar

- 이미 [stackoverflow에 올라와 있는 질문](https://elementaryos.stackexchange.com/questions/10246/how-can-i-change-vscode-sidebar-font)에 의하면, 다음 두 가지를 알 수 있습니다.

```quote
VS Code is an Electron app (built using web technologies), as opposed to a native app (using GTK). I don't believe you have any control over the fonts beyond whatever settings Microsoft have exposed in the config; and it doesn't look like there is an option to change the sidebar font.

There is a GitHub issue here requesting added support for changing the sidebar font, so keep an eye on that.
```

- 첫번째 답변은, VScode는 Electron app(web-technology로 만들어진 것)이며, 이 아이는 OS에서 제어할 수 있는 것이 아닌, 프로그램 자체에 환경 변수(config)이 내재되어 있는 것이다. 따라서, 변경할 수 있는 설정이 있지 않다면 못 바꿀껄? 이라는 말이고.

```quote
/usr/share/vscode/resources/app/out/vs/workbench/workbench.main.css

Just edit font-family CSS to get different font in sidebar
```

- 두번째 답변은, "야, 들어가서, `workbench.main.css` 이 아이를 바꾸면 될 것 같은데?" 라는 말이죠. 그런것 같기는 합니다만. 음, 이건 어째 조금은 위험해 보이기도 합니다. 하지만, 제가 한번 해보도록 하죠.

- 그냥 `setting.json`에 다음을 추가하는 식으로 한다고 해도, 잘 되는 것 같지는 않습니다.

```json
"workbench.fontFamily": "Menlo, Monaco, 'Courier New', monospace, NanumGothicCoding",
```

- 아래와 같은 경우에도 마찬가지에요.

```json
"explorer.fontFamily":"Menlo, Monaco, 'Courier New', monospace, NanumGothicCoding",
```

## 진짜 못 바꾸는건가

- 저렇게 하면 바꿀 수 있을 것이라고 생각했는데, 너무 안이한 생각이었죠. 또한 아래 경로가 달라진 것인지, 저 파일과 동일한 파일이 존재하지 않는 것 같습니다.

```filepath
/usr/share/vscode/resources/app/out/vs/workbench/workbench.main.css
```

- 정말 못 바꾸는 것이라면, 저는 화가 나지 않아요. 그렇게 글러먹은 것이니까요. 다만, "바꿀 수 있는데, 내가 방법을 못 찾았다면 빡칩니다". 따라서, 저는 우선 이 것을 바꿀 수 있는지 없는지를 다시 정리해야 할 것 같아요.
- 이미 약 3년전에 이 링크에서 [github- Allow to change the font size and font of the workbench #519](https://github.com/Microsoft/vscode/issues/519) "workbench에서 font와 size를 바꾸는 것이 허용되어야 하는가?"라는 문제가 제기되었습니다만, 아직까지도 변경되지 않았죠.
- 주로 제기되는 문제는 "위 file_name간의 위아래 간격이 좁다", "i, j, l을 구별하기 어려우니, 고정폭 글꼴로 변경해달라는 것"이고, 그 외로는 VS-code가 늦어지면서 "Atom으로 돌아가자"와 같은 싸움들이 대부분입니다.
- 아무튼, 뭐 어떤 의미로는 맞는 이야기일 수도 있죠. 하지만, 저는 [Atom](https://atom.io/)을 별로 좋아하지 않습니다. 얘는 생각보다 좀 많이 느렸거든요(물론 VS-code도 꽤 느리긴 합니다만).
- 
- [해당 내용은](https://www.reddit.com/r/vscode/comments/dayl90/is_there_a_way_to_change_the_font_in_the_sidebar/)

## Only way to do it now

- 현재로서, 적용할 수 있는 방법은 하나 있습니다. [VScode Extension- Custom CSS and JS Loader](https://marketplace.visualstudio.com/items?itemName=be5invis.vscode-custom-css)을 설치하는 것이죠.
- 앞서 말한 것처럼, VScode는 web application이고 그냥 전체에 css, 를 덮어씌워버리면 본인이 원하는 형태로 전체 스타일링을 변경할 수 있습니다. 다만, 저는 이렇게까지 하는 것은 좀 오바라는 생각이 들어요. 뭐 하려면 하는데, 이정도까지 좀 번잡스럽지는 않아도 될것 같으니까요.

## wrap-up

- 뭐, 별거 아니지만, 저는 제가 겪는 '불편함'이 지금처럼 이미 큰 thread로 존재할 때, 약간의 기쁨을 느낍니다. 하나는, "내가 겪고 있는 불편함이 나만의 것이 아니라는 것"이고, 다른 하나는 "나도 저들과 비슷한 성향을 가진 프로그래머가 되었구나"라는 것 때문이죠(엄밀히 따지면, 아닙니다만)
- 아무튼, 일단은 고치지 않기로 했습니다.
