---
title: Hammerspoon03 - ctrl키로 한영 전환 하기
category: hammerspoon
tags: hammerspoon ctrl hhkb
---

## Hammerspoon03 - ctrl키로 한영 전환 하기

- hammerspoon을 사용하여 ctrl 키가 눌렸을 때, 한영 전환이 발생하도록 설정했습니다.
- 저는 CTRL키가 Caps Lock 위치에 있는 HHKB를 사용하기 때문에, CTRL 키에 한영 전환을 매핑하는 것이 더 효율적입니다.

```lua
------------------------------------------------------------------------------------
-- 2022.03.20 - sng_hn.lee - test
-- hs.eventtap.event.types.flagsChanged: modifier key event 가 발생했을 때.
function control_key_change_kor_en()
  control_keyevent = hs.eventtap.new (
    {
      hs.eventtap.event.types.flagsChanged,
      hs.eventtap.event.types.keyDown
    },
    function (event)
      local flags = event:getFlags()
      local keycode = hs.keycodes.map[event:getKeyCode()]
      if (flags:containExactly({'ctrl'}) == true) then
        if (flags.ctrl == true) then
          --print("This is ctrl")
          change_kor_en_input()
        end
      else
        --print('not only ctrl other pressed or released')
      end
    end
  )

  control_keyevent:start()
end
```
