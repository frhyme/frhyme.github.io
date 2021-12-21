---
title: vim - normal mode에서 자동으로 한영전환하기
category: vim  
tags: vim vimrc vi hammerspoon lua
---

## vim - normal mode에서 자동으로 한영전환하기

- vim은 영어 자판을 사용해야하지만, 한국인들은 영어 자판과 한글 자판을 오가면서 사용하죠. 따라서, 영어인줄 알고 무의식중에 vim command를 사용했으나, 한글 자판이었다면, 한글로 입력된 부분을 지우고, 다시 영어 자판을 입력해줘야 하는 번거로움이 발생합니다.
- [github - 한국어 키보드로 VIM 사용하기](https://github.com/johngrib/simple_vim_guide/blob/master/md/with_korean.md)에 해당 내용을 극복하기 위한 다양한 방법이 작성되어 있는데요. 
- 처음에는 langmap이라는 plugin을 사용하려고 했으나, 다음을 통해 현재 vim version에 langmap 이 설치되어 있는지 확인해봤으나, 설치되어 있지 않더군요. 해당 플러그인을 설치하려면 vim 자체를 다시 compile해야 하는데요, 이건 너무 큰 일이 되죠.

```bash
vim --version | grep langmap 
```

- karabiner를 사용하는 방법도 있으나, 해당 프로그램은 요새 macOS와 호환이 조금씩 절되는 문제등이 있곤 해서, 지양하려고 합니다.

## Use Hammerspoon

- [hammerspoon](http://www.hammerspoon.org/)은 OS X의 자동화 툴로서, OS와 lua scripting engine 사이의 가교 역할을 한다고 합니다. lua는 프로그래밍언어이므로, 아마도 lua를 사용해서 OS X의 특정 부분을 편하게 변경할 수 있도록 지원하는, 툴이다, 정도로 이해하면 되지 않을까 싶어요.
- 여기서 macOS에 직접 연결해서 진행된다는 것이 중요한데요. 이는 특정 프로그램에 의존적이지 않고 어떤 프로그램을 쓰든 항상 자동화된다는 것을 의미합니다.

This is a tool for powerful automation of OS X. At its core, Hammerspoon is just a bridge between the operating system and a Lua scripting engine. What gives Hammerspoon its power is a set of extensions that expose specific pieces of system functionality, to the user.

### Ctrl + ESC with Hammerspoon

- [Hammerspoon - Getting Started](http://www.hammerspoon.org/go/)를 보면 설치하는 방법이 나옵니다.

1. 일단 [Download the latest release of Hammerspoon](https://github.com/Hammerspoon/hammerspoon/releases/tag/0.9.93)에서 최신 hammerspoon을 다운 받은 다음, /Applications 폴더 내에 넣어주고 압축을 풀어줍니다. 이렇게 해주면 Hammerspoon이 설치되어, 아이콘이 생성됩니다.

2. Hammerspoon 앱을 실행하고, Accessibility를 허용해줍니다(클릭하고, Accessibility를 누르고, 자물쇠를 누르고 클릭하고, 자물쇠를 잠급니다).

3. 그 다음에는 menubar에 있는 Hammerspoon을 눌러서 "Open Config"를 클릭하라고 합니다. 클릭해서 열면, 어떤 설정 창이 열리는 것이 아니라, `init.lua`라는 텍스트 파일이 하나 열립니다. 얘의 경로는 `/Users/<user_name>/.hammerspoon/init.lua`이죠. 즉, 설정은 이 텍스트 파일 내에 직접 코드를 작성해줘야 한다는 말로 보이네요.

- [hammerspoon - helloworld](http://www.hammerspoon.org/go/#helloworld)에 보면 몇 가지 예재들이 나옵니다. 여기에서 해당 세팅을 사용하면 될 것으로 보이는데요.
- 아래와 같은 테스트 코드는 `cmd` + `alt` + `ctrl` + `w`를 함께 눌렀을 때, "Hello World!"라는 메세지가 화면에 표시되도록 하는 코드입니다. lua는 잘 몰라도, 대략 어떤 형태로 코드를 집어넣어야 하는지는 보일 것이라고 생각해요.

```lua
hs.hotkey.bind({"cmd", "alt", "ctrl"}, "W", function()
  hs.alert.show("Hello World!")
end)
```

- 다음과 같이 코드를 변경해 봤습니다. 이렇게 코드를 변경하고, 한글 영어를 변환한 다음, 한글 영어를 변환 다음 `cmd` + `alt` + `ctrl` + `w`를 눌러 보면, 각각의 입력 소스가 무엇인지 알 수 있죠. 여기서 print로 표시된 부분은 console창에 뜨며, console은 hammerspoon을 누른 다음 console을 눌러서 확인하면 됩니다

```lua
hs.hotkey.bind({"cmd", "alt", "ctrl"}, "W", function()
    hs.alert.show("Hello World!")
    hs.alert.show(hs.keycodes.currentSourceID())
    print(hs.keycodes.currentSourceID())
end)
```

```plaintext
2021-12-18 16:12:49: com.apple.keylayout.ABC
2021-12-18 16:12:51: com.apple.inputmethod.Korean.2SetKorean
```

- 이를 이용해서 다음처럼 `control` + `esc` 키를 눌렀을때, 영어로 변환해주고, 기존의 esc키도 그대로 먹히도록 해줬습니다. 저장하고, hammerspoon에서 reload config을 클릭해주면 되죠.
- 그냥 `esc` 단일 키에 해당 메커니즘을 적용해주면, `change_input_english` 함수가 반복적으로 call되는 상황이 발생하여 결과적으로는 무한루프가 빠지게 됩니다. 따라서, 어쩔 수 없이 `control` + `esc`의 형태로 해줄 수 밖에 없었죠. 

```lua
-- 2021.12.18 - esc 를 누르면 영어로 자동 전환되도록 변경함.
local input_english = "com.apple.keylayout.ABC"
local input_korean = "com.apple.inputmethod.Korean.2SetKorean"

-- lua에서 function을 변수에 집어넣을 수 있나?

function change_input_english ()
    if (hs.keycodes.currentSourceID() == input_english) then
        -- input_source를 영어로 변경해줌.
        hs.alert.show(input_english)
    elseif (hs.keycodes.currentSourceID() == input_korean) then
        hs.keycodes.currentSourceID(input_english)
    else
        hs.alert.show(hs.keycodes.currentSourceID)
    end
    -- 연달아 escape를 입력하게 되면, 키가 먹히지 않는 경우가 있어, 
    -- 아래와 같이 "right"라는 별 의미없는 키를 한 번 먹인다음 escape를 입력한다.
    hs.eventtap.keyStroke({}, "right")
    hs.eventtap.keyStroke({}, "escape")
end

hs.hotkey.bind({"control"}, "escape", change_input_english)
```

### Better Hammerspoon - just ESC

- 위 방법도 나쁘지는 않습니다만, 가능하면 esc 단일 키를 사용해서 처리하고 싶습니다.
- 그래서 아래와 같이 변경하였습니다. 아래 코드는 escape 키에 펑션을 매핑하고, 해제하고 다시 매핑하는 식으로 진행됩니다.

```lua
-- 2021.12.18 - esc 를 누르면 영어로 자동 전환되도록 변경함.

local input_english = "com.apple.keylayout.ABC"
local input_korean = "com.apple.inputmethod.Korean.2SetKorean"

function change_input_english ()
    if (hs.keycodes.currentSourceID() == input_korean) then
        hs.keycodes.currentSourceID(input_english)
    end
    -- escape에 매핑된 아이를 비활성화한다.
    hs.hotkey.disableAll({}, "escape")
    -- 다른 키와 mapping 되지 않은 pure한 esc를 눌러주고.
    hs.eventtap.keyStroke({}, "escape")
    -- 연달아 escape를 입력하게 되면, 키가 먹히지 않는 경우가 있어, 
    -- 아래와 같이 "right"라는 별 의미없는 키를 한 번 먹인다음 escape를 입력한다.
    -- 또한 한글 입력 중인 경우에도, esc를 누르면 왼쪽으로 한 칸 움직이는 경우가 있어 아래처럼 변경하였다.
    hs.eventtap.keyStroke({}, "right")
    -- 다시 escape에 function을 mapping 해준다.
    hs.hotkey.bind({}, "escape", change_input_english)
end


hs.hotkey.bind({}, "escape", change_input_english)
```

## Wrap-up

- 흠....쓰다보니 이거 꽤 좋아서 karabiner 필요없이 이걸로 다 세팅해줄 수 있지 않을까? 하는 생각이 드네요 호호호. lua도 좀 공부를 해봐야 할 것 같아요.
- 한가지 드는 걱정은, 현재 코드에서는 매번 새롭게 키매핑을 해주는 식입니다. 가령, 매번 새로운 객체를 new하는 형식으로 보이는데요, 이렇게 처리할 경우 미묘하게 과부하가 걸리거나 하지는 않을까? 하는 생각이 드네요. 물론 아마도 아닐겁니다만.

## Reference

- [github - 한국어 키보드로 VIM 사용하기](https://github.com/johngrib/simple_vim_guide/blob/master/md/with_korean.md) 
- [Vim 사용시 한/영 전환 문제 해결하기](https://johngrib.github.io/blog/2017/05/04/input-source/)
- [hammerspoon - hotkey](https://www.hammerspoon.org/docs/hs.hotkey.html#bind)
