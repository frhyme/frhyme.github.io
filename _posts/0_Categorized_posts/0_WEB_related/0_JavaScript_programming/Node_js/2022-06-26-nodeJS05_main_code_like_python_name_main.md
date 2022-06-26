---
title: nodeJS - 직접 실행될 때와, library로 require되는 경우 구분하기
category: nodeJS
tags: nodeJS javascript
---

## nodeJS - 직접 실행될 때와, library로 require되는 경우 구분하기

- python에서 code를 작성할 때, 각 file별로 다음과 같은 두 가지 경우가 발생할 수 있습니다. 가령 `a_lib.py` 라는 file을 작성한다고 한다면.

1. 직접 실행되는 경우: `a_lib.py`가 `python a_lib.py`의 형태로 직접 실행되는 경우
1. library로 import되는 경우: `import a_lib`로 다른 file에서 library로 사용되는 경우

- python에서는 다음을 통해 두 형태를 구분할 수 있습니다.

```python
# a.py
if __name__ == '__main__':
    # this code is executed
    # when a.py called by command line interface
    # ex) python a.py
```

## Do it

- js file이 node에서 바로 실행되는 경우(`node a_lib.js`)인 경우에는 `require.main` 값이 `module`로 설정됩니다.
- `testLib.js` file 내에 code를 다음과 같이 작성합니다. browser에서 실행되는 경우를 먼저 구분하고, 해당 js file이 직접 실행되는 경우와 직접 실행되지 않는 경우를 구분합니다.

```javascript
// browser에서 실행되는 경우에는 require가 undefined 로 설정됩니다.
if (typeof require !== 'undefined') {
  // This is executed directly
  if (require.main === module) {
    // main code
    console.log('called directly');
    for (const x of Object.entries(module)) {
      console.log(x);
    }
  } else {
    // required by other other code
    console.log('required as a module');
    for (const x of Object.entries(module)) {
      console.log(x);
    }
  }
} else {
  // This is executed on browser
}
```

### JS file is called directly

- `testLib.js` file이 직접 실행되었을 때의 `module` 값은 대략 다음과 같습니다.
- 'parent'가 null로 설정되어 있습니다. `testLib.js` file이 직접 실행되었으므로 다른 code에서 참조되는 형태가 아니죠. 따라서, parent가 null로 설정되었습니다.

```javascript
[ 'id', '.' ]
[ 'path', '.../js/testJS' ]
[ 'exports', {} ]
[ 'parent', null ]
[
  'filename',
  '.../js/testJS/test_lib.js'
]
[ 'loaded', false ]
[ 'children', [] ]
[
  'paths',
  [
    '/node_modules'
    '...'
  ]
]
```

### JS file is required as a module

- `testLib.js`를 `testMain.js`에서 다음과 같이 library로 require(import)합니다.

```javascript
require('./testLib.js')
```

- `testLib.js` file이 다음의 형태로 다른 JS file에서 require되었을 때, module 값은 다음과 같습니다.
- `testLib.js`를 직접 실행했을 때는 parent가 null이었던 반면, require되었을 때는 parent가 null이 아닙니다.
- 따라서, 아주 엄밀하게 따지면, `module['parent']`이 null인지 확인하며, 해당 library가 직접 실행되었는지 혹은 require되었는지를 확인할 수 있습니다.

```javascript
[ 'id', '.../js/testJS/test_lib.js' ]
[ 'path', '.../js/testJS' ]
[ 'exports', {} ]
[
  'parent',
  Module {
    id: '.',
    path: '.../js/testJS',
    exports: {},
    parent: null,
    filename: '.../js/testJS/testMain2.js',
    loaded: false,
    children: [ [Module] ],
    paths: [
      '...'
    ]
  }
]
[
  'filename',
  '.../testJS/test_lib.js'
]
[ 'loaded', false ]
[ 'children', [] ]
[
  'paths',
  [
    '/node_modules'
    '...'
  ]
]
```

## Wrap-up

- javascript file은 다음과 같은 3가지 경우로 구분될 수 있습니다.

1. 웹브라우저에서 실행되는 경우: `require` module은 nodeJS에서만 import되므로 web browser에서 실행될 때는 `require`가 undefined로 처리됩니다.
1. nodeJS에서 직접 실행되는 경우: `module['parent']` 가 null입니다.
1. nodeJS에서 다른 js file에서 require되는 경우: `module['parent']` 가 null이 아닙니다.

## Reference

- [stackoverflow - detect if called through require or directly by command line](https://stackoverflow.com/questions/6398196/detect-if-called-through-require-or-directly-by-command-line)
- [stackvoerflow - node js quivalent of pythons if name main](https://stackoverflow.com/questions/4981891/node-js-equivalent-of-pythons-if-name-main)
