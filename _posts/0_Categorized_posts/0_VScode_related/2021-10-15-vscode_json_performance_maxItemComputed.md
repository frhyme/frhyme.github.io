---
title: VScode - json file 옮길 때 속도 저하
category: vscode 
tags: vscode json 
---

## VScode - json file 옮길 때 속도 저하

- VScode에서 data를 다룰 때, 중간 값을 json file로 저장하곤 합니다. 코드는 대략 다음의 형태가 되죠.
  - `ensure_ascii=False`는 json파일을 열었을 때, 아스키코드로 보이는 것이 아니라, 한글일 경우 한글로 그대로 보여주는 것을 위해서 세팅한 것이고.
  - `indent=4`는 들여쓰기를 4 space로 고정하기 위해서 집어넣어준 것이죠.

```python
json.dump(output_dict, f, ensure_ascii=False, indent=4)
```

- 위 코드를 사용해서 json 파일을 만들었습니다. 용량은 40.8MB, 줄 수는 110만 줄 정도 됩니다. 절대적으로 봐도 딱히 vs code의 퍼포먼스에 영향을 줄 수 있는 정도의 파일이 아닌데도 불구하고, 심지어 제 맥북 에어는 램이 16기가고 CPU에도 문제가 없는데오, vscode에서 해당 파일을 지우면 문제가 발생합니다.
- 혹시나 싶어서, VScode 외부, 즉 맥북 탐색기에서 해당 파일을 지웠더니 아주 말끔하게 지워지고, vscode에서도 사라집니다. 뭐...앞으로는 오래 걸린다 싶으면 그냥 vscode 외부에서 지우면 되기는 하겠네요.
- 아무튼, 방금 말한 그 json 파일을 열어서 파일 내용을 보다 보면 아래와 같은 팝업이 뜹니다.
  - Document Symbols: 
  - `json.maxItemComputed`: 

```plaintext
For performance reasons, document symbols have been limited to 100 items, Use Setting json.maxItemComputed to configure the limit
```

- 웹에서 "json.maxItemComputed"을 검색해 보니, [VScode - update v1_41](https://code.visualstudio.com/updates/v1_41)라는 업데이트 관련 사항이 뜹니다. 들어가서 보면, 다음과 같은 내용이 있는데요.

> To avoid performance issues with large JSON files, JSON language support now has an upper limit on the number of folding regions and document symbols it computes (for the Outline view and breadcrumbs). By the default, the limit is 5000 items, but you can change the limit with the setting json.

- 번역을 해보면, 대략 다음과 같겠네요. 약간, 명확하지는 않은데 흠.

> 큰 JSON 파일에서 발생하는 성능상 문제를 피하기 위해서, VScode에서 JSON 언어에 대한 지원은 이제, folding regions와 document symbols은 상한 값을 가지게 될 것입니다. 기본적으로 상한값은 5000으로 고정되지만, setting.json에서 바꿀 수 있어요. 

- 흐음. 명확하지는 않지만, 일단 setting.json 파일에서 값을 다음과 같이 변경해 봤습니다

```json
"json.maxItemsComputed": 1
```

- 이렇게 변경하고 나니까, 확실히 속도가 아주 빨라졌습니다. 뭐, 아주 명쾌하지는 않지만, 일단 이정도면 만족합니다. 

## Reference

- [VScode - v1_41](https://code.visualstudio.com/updates/v1_41))
