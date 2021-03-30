---
title: Excel - VBA - MsgBox
category: MS_Office
tags: MS_Office excel vba macro macOS basic
---

## Excel - VBA - MsgBox

- 윈도우에서 MS office를 사용하는 경우에는 VBA를 편집하거나 할때 아무 문제가 없습니다. 다만, macOS에서 MS-Office를 사용할 때는 꽤 렉이 심하죠. 특히, 엑셀 VBA를 편집할 때는 그 정도가 너무 지나칩니다.
- 따라서, 저는 작성은 VScode에서 하고, 복사하여 엑셀 VBA 창에 집어넣는 식으로 처리해줬습니다.
- 그래도 기본적인 intellisense가 없으니 불편해서 찾아보니, [stackoverflow - using visual studio code for vb net how to enable vb net intellisense](https://stackoverflow.com/questions/52052380/using-visual-studio-code-for-vb-net-how-to-enable-vb-net-intellisense)라는 글이 있습니다. 
- 꼼꼼히 읽어보니, 완벽하지는 않지만, [VScode - marketplace - VB.NET Grammars and Snippets](https://marketplace.visualstudio.com/items?itemName=gordonwalkedby.vbnet) 플러그인을 사용하면 보완이 가능하다고 하네요. 실제로 설치해보니 적당히 쓸만합니다 호호.

## 매크로 실행 버튼 생성

- 개발도구를 활성화했다는 전제 하에서, 개발 도구 > 단추 에 가서 새로운 단추를 생성해줍니다.
- 그리고 해당 단추에서 오른쪽 버튼을 눌러서 '매크로 지정'선택해서 해당 버튼을 클릭했을 때 실행될 매크로를 선택해주고 나면 이후 해당 단추를 누를 때마다 지정된 매크로가 생성됩니다.

## Example - MsgBox

- 다음 매크로 코드는 특정 문자열이 들어간 메세지 박스를 생성해주는 아주 간단한 코드입니다.
- 코드에서 예외가 발생하는 경우 사용자에게 알람을 주는 목적으로 사용할 수 있을 것 같네요.

```vb
Sub FirstFunction()
    MsgBox ("Hello, World!")
End Sub
```
