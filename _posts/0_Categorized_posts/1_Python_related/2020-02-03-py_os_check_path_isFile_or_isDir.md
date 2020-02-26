---
title: Check path where it is file or directory?
category: python-libs
tags: python python-libs os 
---

## path가 file인지 director인지 확인합시다. 

- 보통, python에서 해당 경로에 위치한 path를 모두 읽고, file인지, path인지에 따라서 다른 제어를 해야 한다고 합시다. 
- 가령, 폴더인 경우는 recursive하게 다시 해당 폴더 내의 파일들을 쭉 읽고, 파일인경우에는 그냥 끝내면 되겠죠. 대략 다음의 코드와 같습니다. `os` library를 이용하고요. 
    - Check if it is file type: `os.path.isfile(path)`
    - Check if it is Directory type: `os.path.isdir(path)`

```python
import os

# 절대 경로를 넘기면 됨. 
path = "/Users/frhyme/Downloads"
isFile = os.path.isfile(path)
isDir  = os.path.isdir(path)
print(f"path: {path} => isFile: {isFile} - isDir: {isDir}")

path += "/" + "networkx.algorithms.centrality.katz_centrality.html"
isFile = os.path.isfile(path)
isDir = os.path.isdir(path)
print(f"path: {path} => isFile: {isFile} - isDir: {isDir}")
```

```
path: /Users/frhyme/Downloads => isFile: False - isDir: True
path: /Users/frhyme/Downloads/networkx.algorithms.centrality.katz_centrality.html => isFile: True - isDir: False
```


## reference

- [python-check-if-path-is-file-or-directory](https://pythonexamples.org/python-check-if-path-is-file-or-directory/)