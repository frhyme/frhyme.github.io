---
title: Hammerspoon04 - ctrl키로 한영 전환 및 충돌 피하기
category: hammerspoon
tags: hammerspoon ctrl hhkb macOS lua
---

## Hammerspoon04 - ctrl키로 한영 전환 및 충돌 피하기

- macOS에서 HHKB를 사용해서 개발을 하고 있습니다.
- macOS 기본 키보드에서는 capslock을 이용해서 한영전환을 하는데요, 이게 기존 방식(오른쪽 엄지손가락 사용하는 방식)보다 훨씬 편해서, HHKB에서도 capslock 위치에 있는 ctrl 버튼을 사용해서 한영 전환을 하도록 설정하였습니다.
- 다만 저는 `ctrl` + `hjkl`을 화살표로 사용하고 있습니다. 이 상태에서 위 코드를 사용하게 되면 화살표를 누를 때마다 한영 변환이 발생하게 되는 문제점이 있습니다. hammerspoon을 사용하였고, 해당 코드는 다음과 같죠.

```lua
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

## 개선된 코드

- 따라서, 다음의 형태로 변경하였습니다.

1. 'ctrl이 눌렸을 때'가 아닌, 'ctrl이 release될 때' 한영변환이 발생되도록 한다.
1. 'ctrl 버튼이 눌리기 전' 입력 소스를 기억하고 있다가, 'ctrl이 눌려 있는 상태'에서 hjkl 등의 키가 눌리면, 한영 변환을 하지 않고, 이전 입력 소스로 전환한다.

- 그 외에도, 만약 ctrl과 함께 쓰이는 다른 단축키들이 있을 경우 해당 키를 아래에 추가하여, 해당 단축키를 사용했을 때, 한영 변환이 발생하지 않도록 할 수 있습니다.

```lua
------------------------------------------------------------------------------------
-- 2022.03.30 - sng_hn.lee - ctrl release change kor en
-- ctrl이 단독으로 눌리는 경우에는 한영 변환을 진행하고,
-- ctrl이 눌린 상태에서, hjkl이 눌린 적이 있으면, 이전 입력 소스로 변경함
-- arrow(Fn + [;/')이 입력되었을 때도 변환되지 않도록 처리함
-- 제외되어야 하는 key_code 들을 set로 빼서, contain 등으로 처리하는 것이 필요함
input_before_ctrl_pressed = nil
hjkl_press_count_during_ctrl_pressed = 0

function only_ctrl_change_kor_en()
  local_function = hs.eventtap.new (
    {
      hs.eventtap.event.types.flagsChanged,
      hs.eventtap.event.types.keyDown
    },
    function (event)
      input_before_ctrl_pressed = hs.keycodes.currentSourceID()

      local flags = event:getFlags()
      local keycode = hs.keycodes.map[event:getKeyCode()]
      --print('hjkl_press_count: ', hjkl_press_count)
      --print('== print_keycode ========================')
      if (keycode == 'ctrl' and flags.ctrl == true and flags:containExactly({'ctrl'}) == true) then
        --print('== ctrl key pressed')
        hjkl_press_count_during_ctrl_pressed = 0
      elseif (keycode == 'h' or keycode == 'j' or keycode == 'k' or keycode == 'l') then
        hjkl_press_count_during_ctrl_pressed = hjkl_press_count_during_ctrl_pressed  + 1
      elseif (keycode == 'left' or keycode == 'right' or keycode == 'up' or keycode == 'down') then
        hjkl_press_count_during_ctrl_pressed = hjkl_press_count_during_ctrl_pressed  + 1
      elseif (keycode == 'ctrl' and flags.ctrl == nil and flags:containExactly({'ctrl'}) == false) then
        --print('== ctrl key released')
        if (hjkl_press_count_during_ctrl_pressed== 0) then
          -- ctrl press 이후 hjkl이 눌린 적 없으므로 변환
          kor_en_lang_lib.change_kor_en_input()
        else
          -- ctrl 이후 hjkl이 눌렸으므로 이전 input으로 변경함
          hs.keycodes.currentSourceID(input_before_ctrl_pressed)
        end
      end
      --print('==========================================')
    end
  )
  local_function:start()
end
```

## Wrap-up

- 이 이슈 때문에 며칠동안 퇴근하고 와서 고생한 것 같은데, 드디어 해결해서 매우 기분이 좋습니다 호호호.
- Hammerspoon 설정을 [frhyme - frhyme_hammerspoon](https://github.com/frhyme/frhyme_hammerspoon) 저장소를 만들어 관리하고 있습니다. 혹시 관심이 있으시거나 도움이 되신 분들을 참고하시면 좋을 것 같아요.
