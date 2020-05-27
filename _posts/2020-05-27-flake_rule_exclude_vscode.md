---
title: VScode에서 flake8 특정, rule 제외하기
category: VScode
tags: vscode flake8 python python-lint
---

## Intro 

- VScode를 IDE로 사용하고, python lint로는 [flake8](https://pypi.org/project/flake8/)를 사용하고 있습니다.
- 전반적으로 좋은데, 몇가지 설정을 고치고 싶어서, 그 방법을 정리합니다.

## flake8 in terminal

- `flake8`은 커맨드라인에서 돌아가는 명령어로, 아래와 같은 방식으로 보통 사용합니다.
- 즉, `aaa.py`라는 파이썬 파일에서 CodingConvention에 위배되는 것이 있으면 확인하고, 이를 알려달라는 말이죠.

```bash
flake8 aaa.py
```

- 물론, flake8에서 알려주는 모든 컨벤션을 고치면 좋겠지만, 몇 가지는 좀 과도하게 느껴지는 rule도 있습니다.
- 그런데, 그냥 무시하기에는 화면 안의 **노란 색 줄**이 신경쓰이죠.
- 따라서, 이 몇 가지 rule을 완화하는 방법을 알아봅니다. 

## setting.json

- 우선 `command + p`를 눌러서 `"setting.json"`을 쳐서, 기본 설정 파일로 들어갑니다.
- 들어가서 다음을 추가로 작성해서 넣어줍니다.
- 해석 그래도, 한 줄의 길이를 120으로 늘리고, 동시에 `W291`이라는 rule을 무시한다고 설정해주는 것이죠.

```json
"python.linting.flake8Args": [
    "--max-line-length=120",
    "--ignore=W291",
],
```

- 이렇게 해주고 나면, 이후부터는 내가 신경쓰고 싶지 않은 에러들이 무시되어, 잘 진행되는 것을 알 수 있습니다.

## Reference

- [How do I get flake8 to reliably ignore rules in VS Code?](https://stackoverflow.com/questions/50177173/how-do-i-get-flake8-to-reliably-ignore-rules-in-vs-code)
