---
title: bash vs. zsh vs. fsh
category: others
tags: shell terminal fsh bash zsh
---

## Intro: shell

- 대부분의 프로그래머들은 개발하는 과정에서 terminal을 필연적으로 사용하게 됩니다. 
- 과거에는 GUI가 편하다고 생각했던 것 같은데, 어느새 저는 CLI(Command-Line-Interface)가 더 편한 사람이 되어버렸죠.
- 보통 그냥 terminal이라고 부르지만, 정확하게 표현하자면 `Shell`이라고 부르는 것이 맞습니다. 운영체제와 사람 사이에서 마치 "껍질"처럼 존재한다는 의미로 shell이라는 이름이 붙은 것이죠.
- 하지만, 여기에도 약간씩은 서로 다른 shell들이 존재합니다. 오늘은 그 아이들을 정리해볼게요.

## Bash: Bourne-again shell

- [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))는 가장 보편적으로 볼 수 있는 shell인데, GNU 진영에서 기존의 shell을 대체하기 위해서 만들어진 shell이죠.
- 맥에서는 기본적으로 터미널이 내장되어 있는데, 2019년 가을, 즉 macOS 카탈리나가 나오기 전까지는 bash가 기본 shell이었습니다. 
- 무려, 처음으로 Bash가 macOS의 기본 shell이 되었던 것은 Mac OS X Jaguar부터, 즉 2002년 8월부터였는데, 약 17년 정도 사용된 다음 빠지게 된 것이죠.

## zsh: Z-shell

- [zsh](https://en.wikipedia.org/wiki/Z_shell)은 기존의 Bash를 확장한 shell인데, 2019년 가을부터는 이 아이가 macOS의 기본 shell이 되었죠. 
- 결론부터 말하면 라이센스의 문제이고, 기사 [Why does macOS Catalina use Zsh instead of Bash? Licensing](https://thenextweb.com/dd/2019/06/04/why-does-macos-catalina-use-zsh-instead-of-bash-licensing/)를 읽어보면 조금 더 자세한 내용이 나옵니다.
- 간략하게 말하자면, Bash의 새로운 버전은 GPLv3(GNU General Public License version 3)에 속해 있고, GPLv3에 작성된 내용들이 애플로서는 꽤나 성가셨고, 그래서 갈아탄 것이죠. 뿐만 아니라, 이 과정에서 bash뿐만 아니라, 다른 GPLv3에 속하는 패키지들을 대거 축소하기도 했습니다.
- 반면, Zsh는 MIT 라이센스를 가지고 있고, 따라서, 다른 특허들과 충돌이 발생하지 않아서, 변경하게 된 것이죠.

## fish: Friendly Interactive SHell

- [fish shell](https://fishshell.com/), "친화적인 상호작용저인 shell"이라는 말이겠죠.
- 다른 shell에 비해 좀 유용한 것은 auto-suggestion 기능이라고 하는데, 그 외로는 뭐 zsh와 유사하다고 합니다. 
- 다만, [fishshell 사용기](https://velog.io/@evanjin/fishshell-%EC%82%AC%EC%9A%A9%EA%B8%B0-ubjvbyajo0)를 보면, "맥북에서 기본 제공하는 zsh에 부가기능을 추가하여 진행하였지만 auto-suggestion이 잘 되지 않아서 fish로 넘어왔다는 의견도 있고. 
- [피쉬 쉘 (Fish Shell) 자습서 한글 번역 [입문, 강좌, 소개, 튜토리얼]](https://okky.kr/article/454099)를 보면 한글화에서의 문제가 조금 있다고 이야기를 합니다. 

## reference

- [Medium: fish vs zsh vs bash](https://medium.com/better-programming/fish-vs-zsh-vs-bash-reasons-why-you-need-to-switch-to-fish-4e63a66687eb)