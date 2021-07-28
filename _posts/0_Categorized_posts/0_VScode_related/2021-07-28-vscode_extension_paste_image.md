---
title: VScode - Extension - paste Image 
category: vscode
tags: vscode extension image paste
---

## VScode - Extension - paste Image

- 저는 vscode를 사용해서 마크다운을 편집합니다. 
- 마크다운은 글의 형식과 내용을 한 번에 맞춰서 정리할 수 있다는 점에서 매우 유용합니다. 다만, 아쉽게도 이미지를 첨부히가가 좀 번거롭죠.
- 마크다운에서는 다음의 형식으로 파일경로를 사용해서 이미지를 첨부해야 합니다.

```markdown
![image_name](image_path)
```

- 따라서, 마크다운에 스크린샷으로 파일을 첨부하려면 다음의 순서를 따라야 합니다.
  1. 스크린샷을 떠서 파일로 저장한다.
  2. 저장된 파일을 해당 마크다운이 저장된 폴더로 옮긴다. 이 작업은 필수는 아니지만, 이미지와 마크다운 파일을 함께 관리하려면, 같은 폴더 내에 둬서 함께 관리할 수 있도록 하는 것이 좋습니다.
  3. 마크다운 내에 마크다운 혀익으로 이미지를 첨부한다.
- 보시는 것처럼, 이 과정이 꽤 번거롭습니다. 따라서, 이를 자동화해주면 좋겠는데, 다행히도 이미 [vscode - marketplace - vscode paste image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)에 좋은 익스텐션이 있습니다.

## VScode Extension - paste image

- [vscode - marketplace - vscode paste image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)를 설치합니다.
- 설치하고 나서, 아무 스크린샷이나 뜹니다. 맥에서는 `cmd + shift + ctrl + 4`를 누르면 스크린샷을 떠서 클립보드에 저장해 둘 수 있습니다.
- 그리고, `cmd + option + v`를 누르면, 해당 파일이 아래와 같은 형식으로 마크다운 파일 내에 추가되고, 마크다운이 존재하는 폴더 내에 image가 추가됩니다.

```markdown
![](2021-07-25-03-25-26.png)
```

### configuration 

- 스크린캡쳐를 통해 클립보드에 저장된 이미지를 마크다운에 첨부하려면, 당연하지만 해당 이미지 파일이 폴더 내에 어딘가에 저장되어야 합니다. 파일이 저장되는 경로를 지정할 수 있는데요. 기본적인 환경변수들로 다음이 제공됩니다.
  - `${currentFileDir}`: 편집하고 있는 마크다운 폴더를 가리킴
  - `${projectRoot}`: 편집하고 있는 프로젝트 폴더를 가리킴
- 위 환경변수들을 사용해서 다음처럼 세팅해 줄 수도 있습니다. 폴더가 없을 경우 알아서 맏늘어 줍니다.
  - `${currentFileDir}/images/`
- 또한 저는 이미지 fileName의 prefix를 `screencapture_`로 변경하고, default_date를 `YYYYMMDDHHmmss`과 같이 변경하였습니다.

## reference

- [vscode - marketplace - vscode paste image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)
