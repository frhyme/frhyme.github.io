---
title: Hammerspoon02 - 키보드로 마우스 움직이고 클릭하기
category: hammerspoon
tags: hammerspoon mouse keyboard
---

## Hammerspoon02 - 키보드로 마우스 움직이고 클릭하기

- hammerspoon을 이용해서 키보드로 마우스를 움직일 수 있도록 설정해봤습니다.

```lua
------------------------------------------------------------------------------------
-- 2022.03.23 - sng_hn.lee - mouse 움직이도록 설ㅏ
function move_click_mouse ()
  --https://www.hammerspoon.org/docs/hs.mouse.html

  local function func_move_mouse_hjkl (key)
    local step_x_size = 30.0
    local step_y_size = 15.0

    local curr_relative_pos = hs.mouse.getRelativePosition()
    local curr_absolute_pos = hs.mouse.absolutePosition()
    local curr_abs_x = curr_absolute_pos['x']
    local curr_abs_y = curr_absolute_pos['y']

    --print('current absolute position: ', curr_abs_x, curr_abs_y)

    if (key == 'H') then
      --print('go mouse left')

      to_xy_pos = {x=curr_abs_x - step_x_size, y=curr_abs_y}
      hs.mouse.absolutePosition(to_xy_pos)
    elseif (key == 'J') then
      --print('go mouse down')

      to_xy_pos = {x=curr_abs_x, y=curr_abs_y + step_y_size}
      hs.mouse.absolutePosition(to_xy_pos)
    elseif (key == 'K') then
      --print('go mouse up')

      to_xy_pos = {x=curr_abs_x, y=curr_abs_y - step_y_size}
      hs.mouse.absolutePosition(to_xy_pos)
    elseif (key == 'L') then
      --print('go mouse right')

      to_xy_pos = {x=curr_abs_x + step_x_size, y=curr_abs_y}
      hs.mouse.absolutePosition(to_xy_pos)
    end
  end
  -- 현재 맥북에서는 abs, rel 값이 동일한 것 같음.
  for key, value in pairs({'H', 'J', 'K', 'L'}) do
    hs.hotkey.bind({'cmd', 'alt'}, value,
      function () func_move_mouse_hjkl(value) end,
      function () end,
      function () func_move_mouse_hjkl(value) end
    )
  end

  -- left click
  hs.hotkey.bind({'cmd', 'alt'}, 'U',
    function ()
      --print('-- click')
      local curr_absolute_pos = hs.mouse.absolutePosition()
      hs.eventtap.leftClick(curr_absolute_pos)
    end,
    function () end,
    function () end
  )
  -- right click
  hs.hotkey.bind({'cmd', 'alt'}, 'I',
    function ()
      --print('-- click')
      local curr_absolute_pos = hs.mouse.absolutePosition()
      hs.eventtap.rightClick(curr_absolute_pos)
    end,
    function () end,
    function () end
  )
end
```
