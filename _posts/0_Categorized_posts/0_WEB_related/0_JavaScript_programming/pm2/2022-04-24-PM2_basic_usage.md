---
title: nodeJS - PM2 - Basic usage
category: nodeJS
tags: nodeJS javascript PM2
---

## nodeJS - PM2 - Basic usage

- nodeJS에는 [pm2](https://pm2.keymetrics.io/)라는 개쩌는 놈이 있습니다. 대충 알아서 꺼지면 켜주고, 리소스 관리하고 로깅 해주고 하는 완벽한 인프라 관리 서비스? 정도로 해석하면 될것 같네요.
- 아무튼, 보통은 걍 nodeJS로 개발을 끝내고, pm2로 나머지를 처리해주면 되는데요. 아직 간단한 명령어도 숙달되지 않아서, 몇몇 주요 상황에 대해서 어떻게 사용해야 하는지를 정리해 봅니다.

## pm2 usage

- pm2 로 `main.js`를 실행합니다.
  - `pm2 start main.js --watch`: code에서 변경점이 발생하면 바로 적용하여 서버를 구동한다.
  - `pm2 start main.js --no-daemon`: background기가 아닌 foreground에서 돌아가도록 처리한다. 개인적으로는 terminal 창이 여러 개 있기 때문에 background보다는 foreground에서 돌리는게 상황을 파악하는 데 더 좋은 것 같더라고요. 나가기 위해서는 `ctrl + c`를 눌러주면 됩니다. 나가면 pm2는 바로 종료 처리되죠.
  - `pm2 start main.js --watch --ignore-watch="data/*"`: folder 내에 변경점을 계속 확인하고 있다가, 변경점이 발생하면, 껐다가 켜주는데, `data/*`에 있는 file 들의 경우에는 파일이 추가되거나 변경되어도 끄거나 켜주지 않는다. 라는 의미입니다. `--ignore-watch`를 지정하지 않았을 경우 해당 폴더 내에 그냥 file이 추가되기만 해도 꺼지거나 하는 데요, 이럴 경우 여러 사용자가 동시에 접속한다거나 하는 경우에는 문제가 발생할 수 있습니다. 따라서, 껐다가 켜질 필요가 없는 폴더는 제외해주는 것이 좋죠.

```sh
> pm2 start main.js
[PM2] Spawning PM2 daemon with pm2_home=/Users/seunghoonlee/.pm2
[PM2] PM2 Successfully daemonized
[PM2] Starting /Users/seunghoonlee/HelloJS/nodeJS_study/main.js in fork_mode (1 instance)
[PM2] Done.
┌─────┬─────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id  │ name    │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
├─────┼─────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
│ 0   │ main    │ default     │ N/A     │ fork    │ 50073    │ 0s     │ 0    │ online    │ 5%       │ 20.6mb   │ seu… │ disabled │
└─────┴─────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
```

- 현재 사용중인 app list 출력하는 방법

```sh
pm2 start main.js --watch
[PM2] Starting /Users/seunghoonlee/HelloJS/nodeJS_study/main.js in fork_mode (1 instance)
[PM2] Done.
┌─────┬─────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id  │ name    │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
├─────┼─────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
│ 0   │ main    │ default     │ N/A     │ fork    │ 50660    │ 0s     │ 0    │ online    │ 0%       │ 9.5mb    │ seu… │ enabled  │
└─────┴─────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
```

- 현재 사용중인 app 의 resource 사용 현황 확인하는 방법

```sh
pm2 monit
```

- pm2 로 실행한 모든 프로세스를 종료합니다.

```sh
> pm2 kill
[PM2] Applying action deleteProcessId on app [all](ids: [ 0 ])
[PM2] [main](0) ✓
[PM2] [v] All Applications Stopped
[PM2] [v] PM2 Daemon Stopped


```

## Wrap-up

- 일단은 간단한 사용법을 정리하였습니다.

## Reference

- [생활코딩 - 보충수업 - PM2 사용법](https://opentutorials.org/course/3332)
- [pm2](https://pm2.keymetrics.io/)
