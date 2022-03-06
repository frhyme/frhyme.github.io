---
title: NodeJS - Passing Command line arguments
category: javascript
tags: nodejs javascript argument
---

## NodeJS - Passing Command line arguments

- nodejs를 command line에서 실행할 때, argument를 넘겨주는 방법은 다음과 같습니다.

```sh
node pass_argv.js arg1 arg2
```

- 그리고 `process.argv`에 담기는데요, 다음과 같이 array의 형태로 담깁니다.
- node의 실행 경로, 현재 file의 경로 그리고 command line에서 입력받은 argument

```plaintext
[
  '/usr/local/bin/node',
  'current file path',
  'arg1',
  'arg2'
]
```

## Wrap-up

- 간단히 command line에서 argument를 node로 넘겨주는 방법을 정리하였습니다.

## Reference

- [stackoverflow - How do i pass command line arguments to a node js program](https://stackoverflow.com/questions/4351521/how-do-i-pass-command-line-arguments-to-a-node-js-program)
