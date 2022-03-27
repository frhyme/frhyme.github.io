---
title: Lua - Read function from module
category: lua
tags: lua function module hammerspoon
---

## Lua - Read function from module

- 최근에는 [hammerspoon](https://www.hammerspoon.org/)을 이용해서 맥에서 불편했던 사소한 부분들을 수정하고 있습니다. 가령 ctrl + hjkl을 누르면 화살표가 되도록 한다거나, esc를 누르면 자동으로 한영 전환이 되도록 한다거나, 하는 짓들을 구현하고 있습니다. hammerspoon을 사용하려면 lua를 사용해서 코드를 작성해야 하고요.
- 현재는 전체 코드가 `main.lua` file 내에 모두 있는데요. 코드가 길어짐에 따라서 코드가 지저분해지고 디버깅이 어려워져서 코드를 분리하려고 합니다. 네, 모듈화한다는 말이죠.
- 따라서, lua에서는 각 함수를 어떻게 모듈로 처리하는지를 정리합니다.

## Do it

- 메인 코드는 `main.lua`에 작성하고, 참조하는 함수들은 `calculator.lua` 파일에 작성하였습니다.

### module - calculator.lua

- `calculator.lua`를 만들고, 아래와 같이 모듈을 정의해줍니다.
- 다른 lua code에서 사용되기 위해서는 다음처럼 table 내에 함수가 작성되어야 합니다. 이렇게 쓰고보니, 마치 javascript의 객체와 유사하게 보이네요.

```lua
--[[
2022.03.27 - Init
Simple caclulator
--]]

local this_module = {}

function this_module.print_this ()
  print("function: print_this")
end

function this_module.add(a, b)
  print('add function: ', a + b)
  return a + b
end

function this_module.subtract(a, b)
  print('substract function: ', a - b)
  return a - b
end

function this_module.multiply(a, b)
  print('multiply function: ', a * b)
  return a * b
end

return this_module
```

### main.lua

- `main.lua`는 다음과 같이 만들고, 앞서 만든 `calcuator.lua` 파일을 가져옵니다.
- 가져올 때는 `require`를 사용하고, file 확장자 명을 사용하지 않습니다.

```lua
print("This is main.lua")

local lib = require('calculator')

print(lib.add(3, 4))
print(lib.subtract(3, 4))
print(lib.multiply(3, 4))
```

## Wrap-up

- 조금 더 파보면 재밌는 부분들이 많을 것 같지만, 일단은 이렇게만 하고 사용하면서 고쳐보도록 합니다. 저는 미리 배우는 것보다는, 필요할 때 배우는 편이 훨씬 도움이 되더라고요.

## Reference

- [Learn X in Y minutes Where X=Lua](https://learnxinyminutes.com/docs/lua/)
