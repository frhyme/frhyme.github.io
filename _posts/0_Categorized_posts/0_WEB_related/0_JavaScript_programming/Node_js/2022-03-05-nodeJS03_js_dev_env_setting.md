---
title: Vim - Javascript 개발 환경 구축
category: javascript
tags: vim javascript vundle eslint npm syntastic
---

## Vim - Javascript 개발 환경 구축

### javascript syntax highlighting

- vim에서 javascript를 작성중에 syntax highlighting이 예쁘게 되지 않아서, vim-javascript라는 플러그인을 vundle을 사용해서 설치해줍니다.
- 부분적으로 syntax highlight이 되는 것도 있긴 한데, rich하지 않아서 추가로 설치해주는 것이 더 좋아보여서요.

```vim
" 20220305 - javascript syntax highlight
Plugin 'pangloss/vim-javascript'
```

```vim
:VundleInstall
```

- 이후 확인하면, syntax highlight가 더 화려하게 되는 것을 알 수 있습니다.

### Javascript syntastic checker

- Syntastic을 이용해서 javascript의 syntax를 check하기 위해서는 우선 [npmjs - eslint](https://www.npmjs.com/package/eslint)를 설치하고, 그 다음 syntastic에서 ESLint를 사용하도록 설정해줘야 합니다.
- eslint를 설치할 때, global로 설정해주는 것은 해당 모듈을 syntastic에서도 사용하기 때문인 것 같습니다.
- 저는 mac을 사용하고 있으며, 설치 중에 권한 문제로 인하여 `sudo`로 설치하였습니다.
- `npm init @eslint/config`은 `eslint --init`와 동일합니다.
- `package.json` 파일이 있는 상태에서 eslint를 설정해줘야 하므로, 처음에는 `npm init`을 통해 `package.json` 파일을 생성해주고, 그다음에 eslint를 설정해줍니다.

```sh
$ npm install eslint --global
$ npm list -g
/usr/local/lib
├── @google/clasp@2.3.0
├── eslint@8.10.0
└── npm@8.5.3
$ npm init
$ ls
helloworld.js package.json
```

- `package.json` file 내에는 아래와 같은 내용이 작성됩니다. 대충 보니, 현재 프로젝트에 대한 메타데이터네요.

```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "",
  "main": "helloworld.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "eslint": "^8.10.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-plugin-import": "^2.25.4"
  }
}
```

- 이제 eslint를 설정해줍니다.

```sh
$ npm init @eslint/config
✔ How would you like to use ESLint? · style
✔ What type of modules does your project use? · commonjs
✔ Which framework does your project use? · none
✔ Does your project use TypeScript? · No / Yes
✔ Where does your code run? · browser
✔ How would you like to define a style for your project? · guide
✔ Which style guide do you want to follow? · airbnb
✔ What format do you want your config file to be in? · YAML
Checking peerDependencies of eslint-config-airbnb-base@latest
Local ESLint installation not found.
The config that you've selected requires the following dependencies:

eslint-config-airbnb-base@latest eslint@^7.32.0 || ^8.2.0 eslint-plugin-import@^2.25.2
✔ Would you like to install them now with npm? · No / Yes
```

- 위 명령어 정상적으로 진행되면 폴더 내에 `.eslintrc.yml` 파일이 생성되며 내용은 다음과 같습니다.

```yaml
env:
  browser: true
  commonjs: true
  es2021: true
extends:
  - airbnb-base
parserOptions:
  ecmaVersion: latest
rules: {}
```

- 그리고, 간단한 js 파일을 만들고, eslint가 실행되는지 테스트 해봅니다.

```sh
eslint helloworld.js
```

- 그 다음 `.vimrc` file 내에 아래 내용을 추가하여, syntastic에서 javascript checker를 설정해줍니다.

```vim
let g:syntastic_javascript_checkers = ['eslint']
```

- 만약 아래 오류 로그가 발생한다면, 해당 폴더 내에 `package.json` 파일이 존재하지 않아서 eslint가 설정되지 않는 것이므로 `npm init`을 통해 `package.json` 파일을 생성해준 다음, eslint를 다시 설정해줍니다.

```sh
Oops! Something went wrong! :(

ESLint: 8.10.0

ESLint couldn't find a configuration file. To set up a configuration file for this project, please run:

    npm init @eslint/config

ESLint looked for configuration files in /Users/seunghoonlee/HelloJS/nodejs and its ancestors. If it found none, it then looked in your home directory.

If you think you already have a configuration file or if you need more help, please stop by the ESLint chat room: https://eslint.org/chat/help
```

## Wrap-up

- shell command만 정리하면 다음과 같습니다.

```sh
npm init # package.json 생성
npm init @eslint/config
eslint a.js
```

## Reference

- [npmjs - eslint](https://www.npmjs.com/package/eslint)
- [remarkablemark - vim syntastic eslint](https://remarkablemark.org/blog/2016/09/28/vim-syntastic-eslint/)
