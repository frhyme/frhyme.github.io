---
title: nodeJS - address already in use
category: nodeJS
tags: nodeJS javascript server http web error
---

## nodeJS - address already in use

- 다음과 같은 오류와 함께 nodeJS로 만든 서버가 구동되지 않는 경우가 있습니다.

```plaintext
events.js:292
      throw er; // Unhandled 'error' event
      ^

Error: listen EADDRINUSE: address already in use :::8081
    at Server.setupListenHandle [as _listen2] (net.js:1318:16)
    at listenInCluster (net.js:1366:12)
    at Server.listen (net.js:1452:7)
    at Object.<anonymous> (/Users/seunghoonlee/NodeJS_proj/main.js:21:4)
    at Module._compile (internal/modules/cjs/loader.js:1063:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1092:10)
    at Module.load (internal/modules/cjs/loader.js:928:32)
    at Function.Module._load (internal/modules/cjs/loader.js:769:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:72:12)
    at internal/main/run_main_module.js:17:47
Emitted 'error' event on Server instance at:
    at emitErrorNT (net.js:1345:8)
    at processTicksAndRejections (internal/process/task_queues.js:80:21) {
  code: 'EADDRINUSE',
  errno: -48,
  syscall: 'listen',
  address: '::',
  port: 8081
}
```

- 이 때는, 보통 이미 포트가 점유되고 있을 경우를 말하죠. 
- 따라서, 다음 커맨드를 사용해서 해당 port를 사용중인 프로세스를 확인하고, PID를 kill해줍니다.

```plaintext
$ lsof -i TCP:8081
COMMAND     PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node      12345 seunghoonlee   
$ kill -9 12345
```

## Reference

- [Node JS already in use](https://jootc.com/p/201912253249)
