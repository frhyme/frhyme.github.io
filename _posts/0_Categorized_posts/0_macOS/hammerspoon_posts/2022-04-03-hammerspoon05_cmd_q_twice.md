---
title: Hammerspoon05 - cmd + q 두 번 눌러야 실행되도록 변경
category: hammerspoon
tags: hammerspoon macOS cmd
---

## Hammerspoon05 - cmd + q 두 번 눌러야 실행되도록 변경

- macOS에서는 "command + q" 를 누르면 현재 어플리케이션이 바로 종료됩니다. 다만 실수로라도 잘못 누르면 바로 종료되어서, 키보드를 던져버리고 싶은 기분이 들 때가 있습니다.
- 따라서, "command + q"를 눌렀을 때 바롷 종료되지 않고, 시간 내에 연속으로 두 번 눌러야 종료되도록 처리하는 기능을 개발했습니다.
- [drewrothstein/cmq.lua](https://gist.github.com/drewrothstein/3568a4624e2e9675fa0dfc2930e9eca5)를 참고하여 코드를 수정하였습니다.

## code

- hammespoon에서는 특정 키가 눌리면 어떤 mode(modal) 상태로 접속하고, 그 상태에서만 발동되는 특정한 키들을 bind할 수 있습니다.

1. "command + q"가 눌리면 `quitModal` 상태로 진입하도록 설정합니다.
1. 사용자가 "command + q"를 누르면 `quitModal` 상태에 진입하게 됩니다.
1. `quitModal` 상태에서 1초 내에 다시 "command + q"를 누르면 현재 띄워져 있는 app(front_most_app)을 kill합니다.
1. 만약 1초 내에 "command + q"가 눌리지 않거나, `escape`를 누르면 `quitModal` 상태에서 탈출합니다.

```lua
local this_module = {}

function this_module.cmd_q_twice()
  -- 2022.04.03 - sng_hn.lee - Init, copy below URL
  -- https://gist.github.com/drewrothstein/3568a4624e2e9675fa0dfc2930e9eca5
  -- Press Cmd+Q twice to quit

  local quitModal = hs.hotkey.modal.new('cmd', 'q')

  function quitModal:entered()
    hs.alert.show("Press Cmd+Q again to quit in 1 seconds")
    -- 1초 동안 modal 상태에서 기다리다가 종료함.
    hs.timer.doAfter(
      1,
      function()
        --hs.alert.show('modal quit')
        quitModal:exit()
      end
    )
  end

  quitModal:bind('cmd', 'q',
    function ()
      -- 아래 코드가 먹히지 않아서 그냥 종료하는 것으로 변경함.
      --local res = hs.application.frontmostApplication():selectMenuItem("^Quit.*$")
      local front_most_app = hs.application.frontmostApplication()
      front_most_app:kill()
      --hs.alsert.show('frontmostApp killed')
      quitModal:exit()
    end
  )

  quitModal:bind('', 'escape',
    function()
      --hs.alert.show('cmd_q modal exit')
      quitModal:exit()
    end
  )
end

return this_module
```
