---
title: macOS - hammerspoon01 - ctrl + hjkl 화살표 사용하기
category: hammerspoon
tags: macOS hammerspoon lua vi vim
---

## macOS - hammerspoon01 - ctrl + hjkl 화살표 사용하기

- 키보드 위에서 손이 움직이는 영역을 줄이기 위해, 화살표를 ctrl + hjkl을 이용해서 사용하려고 합니다.
- [Hammerspoon](https://www.hammerspoon.org/go/)을 이용합니다.

## Do it by Hammerspoon

### Ctrl + hjkl

- "Ctrl + hjkl 을 화살표로 이용할 수 있도록" 해주는 lua code는 다음과 같습니다.

```lua
------------------------------------------------------------------------------------
-- 2022.03.19 - sng_hn.lee - Arrow keys
-- hs.hotkey.bind(mods, key, [message,] pressedfn, releasedfn, repeatfn)
-- 누르고 있는 경우를 고려하기 위해서는 repeatfn 이 정의되어야 함.
function stroke_arrow(arrow_key)
  -- hs.eventtap.keyStroke()의 경우 중간에 timer.usleep()이
  -- 포함되어 있어, 연속 입력이 어려우므로, 다음처럼 처리하였다.
  local event = require("hs.eventtap").event
  event.newKeyEvent({}, arrow_key, true):post()
  event.newKeyEvent({}, arrow_key, false):post()
end

hs.hotkey.bind({"ctrl"}, "H",
  function () stroke_arrow('left') end,
  function () end,
  function () stroke_arrow('left') end
)
hs.hotkey.bind({"ctrl"}, "J",
  function () stroke_arrow('down') end,
  function () end,
  function () stroke_arrow('down') end
)
hs.hotkey.bind({"ctrl"}, "K",
  function () stroke_arrow('up') end,
  function () end,
  function () stroke_arrow('up') end
)
hs.hotkey.bind({"ctrl"}, "L",
  function () stroke_arrow('right') end,
  function () end,
  function () stroke_arrow('right') end
)
```

### Ctrl + Shift + hjkl

- shift + arrow를 입력하면 커서 위치부터 block을 지정할 수 있습니다.
- ctrl + shift + hjkl을 입력할 때도, 커서 위치부터 block을 지정할 수 있도록 하는 코드는 다음과 같습니다.

```lua
------------------------------------------------------------------------------------
-- 2022.03.20 - sng_hn.lee - ctrl + shift + hjkl => block
-- function을 만들어서, 아래 간소화할 것.
-- https://www.hammerspoon.org/docs/hs.eventtap.event.html#newKeyEvent
function stroke_shift_arrow(arrow_key)
  return function ()
    local event = require("hs.eventtap").event
    event.newKeyEvent({'shift'}, arrow_key, true):post()
    event.newKeyEvent({'shift'}, arrow_key, false):post()
  end
end
hs.hotkey.bind({"ctrl", "shift"}, "H",
  stroke_shift_arrow('left'),
  function () end,
  stroke_shift_arrow('left')
)
hs.hotkey.bind({"ctrl", "shift"}, "J",
  stroke_shift_arrow('down'),
  function () end,
  stroke_shift_arrow('down')
)
hs.hotkey.bind({"ctrl", "shift"}, "K",
  stroke_shift_arrow('up'),
  function () end,
  stroke_shift_arrow('up')
)
hs.hotkey.bind({"ctrl", "shift"}, "L",
  stroke_shift_arrow('right'),
  function () end,
  stroke_shift_arrow('right')
)
```

## Wrap-up

- Ctrl + hjkl을 화살표로 입력하도록 하는 방법을 정리하였습니다.

## Reference

- [hammerspoon - docs hs.eventtap.event.html - types](https://www.hammerspoon.org/docs/hs.eventtap.event.html#types)
