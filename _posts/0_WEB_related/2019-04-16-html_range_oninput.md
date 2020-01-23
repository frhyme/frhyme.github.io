---
title: html에서 range를 이용해서 input을 받고 input 변화값 보여주기. 
category: html
tags: html javascript
---

## html에서 range를 이용해서 input을 받고 input 변화값 보여주기. 

- 사용자가 직접 키보드를 이용해서 원하는 값을 매번 선택할 수도 있습니다. 그게 기본적인 input이죠. 
- 그런데, 아주 정확한 값을 측정하지는 않아도 되고 대략적인 값만 해도 되고, 또 입력해야 하는 값이 매우 많다면, 그냥 scroll의 형식으로 값을 입력받을 수 있도록 해도 됩니다. 
- 즉 이를 위해서 input에서 type을 `range`라는 걸로 설정해서 진행할 수 있죠. 
- 하지만, 그냥 range만을 가지고 사용하면, range를 통해서 입력받은 값이 어떤지를 정확하게 알 수 가 없습니다. 
- 따라서, 이 값도 그 변화에 따라서 보여줄 수 있도록 하는 것이 더 좋죠. 

## do it.

- 다음처럼 하면 됩니다. 
    - input의 type을 range로 정하고 
    - min, max, step, value등을 정합니다. 
    - 그 다음, oninput에 해당 값이 들어올 때 해야 하는 일을 정하죠. 
    - 여기서는 따로 값을 보여주는 span을 만들어놓고, 그 id를 찾아서, 해당 부분의 텍스트가 변하도록 세팅했습니다. 

```html
<form>
    <div>
        <label> Value1: </label>
        <input type="range" name="points" min="0" max="1.0" step="0.05" value="0" oninput="document.getElementById('value1').innerHTML=this.value;">
        <span id="value1"></span>
    </div>
    <div>
        <label> Value2: </label>
        <input type="range" name="points" min="0" max="1.0" step="0.05" value="0" oninput="document.getElementById('value2').innerHTML=this.value;">
        <span id="value2"></span>
    </div>
</form>
```

## wrap-up

- 언제나 그렇듯이, 간단합니다 하하하.