---
title: macOS - hammerspoon00 - ESC로 한영 변환하기
category: hammerspoon
tags: macOS hammerspoon lua vi vim
---

## macOS - hammerspoon00 - ESC 입력하면 항상 영어 입력으로 변경하기

- 저는 주 IDE로 vim을 사용합니다. 글을 작성하다가 command mode로 변경할 때는 Escape를 눌러야 하는데요.
- 영어로 글을 작성하다가 escape를 누르게 될 경우에는 한영변환 키를 누르지 않아도 되지만, 한글로 글을 작성하다가 escape를 누르게 되면 꼭 한영 변환 키를 눌러줘야 합니다. 사소하지만 글을 쓸 때 흐름을해치는 문제라서, "Escape 키를 누르면 항상 영어로 전환"과 같은 기능이 지원되면 좋을 것 같아요.
- 찾아보니 [Hammerspoon](https://www.hammerspoon.org/go/)이 있는데요. "Hammerspoon is a desktop automation tool for macOS"이라고 합니다. 대충 macOS 자동화 도구 인셈인데요. 설치해서 사용해봅니다.

## Do it by Hammerspoon

- "Escape를 눌렀을 때, 항상 영어 입력으로 전환"하도록 해주는 lua code는 다음과 같습니다.

```lua
-- 이건 일종의 리스너륾 만든거임. 키가 입력되면 걔가 특정 키인지 확인하고, 해당되는 행위를 수행하도록 함.
-- hs.eventtap.event.types.keyDown: modifier key가 아닌 다른 일반 key에 down이 발생했을 때
-- 입력된 key의 code가 'escape'이면 input_source를 확인하고 영어가 아닐 경우 영어로 변환해준다.
escape_keyevent = hs.eventtap.new (
  {hs.eventtap.event.types.keyDown},
  function (event)
    local flags = event:getFlags()
    local keycode = hs.keycodes.map[event:getKeyCode()]

    if (keycode == 'escape') then
      -- print("This is escape")
      local input_korean = "com.apple.inputmethod.Korean.2SetKorean"
      local input_english = "com.apple.keylayout.ABC"

      local input_source = hs.keycodes.currentSourceID()

      if (input_source ~= input_english) then
        hs.keycodes.currentSourceID(input_english)
      end
    end
  end
)
escape_keyevent:start()
```

## Reference

- [stackoverflow - key repeats are delayed in my hammerspoon script](https://stackoverflow.com/questions/40986242/key-repeats-are-delayed-in-my-hammerspoon-script)
- [MAC caps lock 을 escape + ctrl 로 사용해보자 (for VIM user)](https://leedo1982.github.io/wiki/ESC_CTRL_CAPSLOCK/)
- [hammerspoon - docs hs.eventtap.event.html - types](https://www.hammerspoon.org/docs/hs.eventtap.event.html#types)
