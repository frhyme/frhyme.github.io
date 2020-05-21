---
title: [vs-code] - jediEnabled?
category: vs-code
tags: vs-code intellisense
---

## Intro

- vs-code에서 intellisense는 기본으로 [jedi](https://jedi.readthedocs.io/en/latest/)에 의해서 지원됩니다.
- 보다 정확하게 말하자면, vs-code에서 python을 사용하기 위해 설치하는 [python extension by MS](https://marketplace.visualstudio.com/items?itemName=ms-python.python)가 jedi를 기본으로 사용하고 있는 것이죠.
- 보통 setting.json 부분에서 아래와 같이 기본으로 설정되어 있죠(default입니다.).

```json
"python.jediEnabled": true,//이 부분을 false로 변경하면 jedi가 동작하지 않음.
```

## what is jedi?

- [jedi](https://jedi.readthedocs.io/en/latest/)는 공식 홈페이지에서 다음과 같이 정의되어 있습니다.

> Jedi is a static analysis tool for Python that is typically used in IDEs/editors plugins. Jedi has a focus on autocompletion and goto functionality. Other features include refactoring, code search and finding references.

- 대충 번역하자면, python을 위한 정적 분석 도구고, 자동완성(autocompletion)과 goto functionality를 포함한 다양한 기능을 지원한다는 이야기죠.

## jediEnabled: false?

- 앞서 말한 것처럼, vscode의 기본 설정은 jedi를 활성화해둔 것이기는 합니다. 다만, 만약 이를 아래와 같이 false로 변경하면 어떻게 될까요?

```json
"python.jediEnabled": false,
```

- [vscode-python-setting](https://code.visualstudio.com/docs/python/settings-reference)을 확인해보면 `python.jediEnabled`에 대해서 다음과 같이 작성되어 있습니다.

```plaintext
Indicates whether to use Jedi as the IntelliSense engine (true) or the Microsoft Python Language Server (false). Note that the language server requires a platform that supports .NET Core 2.1 or newer.
```

- 해석하자면, `true`인 경우에는 Jedi를 IntelliSense engine로 설정하고, 그렇지 않고 `false`일 경우에는 Microsfot PYthon Language Server를 사용한다는 이야기죠. 더불어, MS language server는 ".NET Core 2.1"이상을 지원하는 플랫폼을 요구하고 있습니다.

## MS-python language server

- [MS-python language server](https://github.com/microsoft/python-language-server)는 마이크소프트에서 직접 개발한 jedi와 유사한 종류의 IntelliSense라고 보시면 됩니다.
- 그리고, 이 아이를 개선한 아이가 얼마전 나왔던 [MS-IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)죠.

## wra-up

- jedi는 마이크로소프트가 아닌 외부에서 만든 것이고, 차츰차츰 기본 engine이 jedi가 아닌 다른 아이로 바뀔 가능성이 있다고 생각합니다.
- 다만, IntelliCode는 써봤지만, 그 성능이 좋지 못하게 느껴지고, python language server는 어째서인지 제 vs-code에서는 동작도 하지 않더군요.
- 따라서 저는 한동안은 그냥 jedi를 사용할 계획입니다.
