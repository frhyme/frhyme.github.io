---
title: python의 os module 사용하기 
category: python-lib
tags: python os python-lib bash unix subprocess
---

## python - os lib 사용하기

- 코딩하다 보면, 로컬에 있는 파일을 지우고, 만들고 싶을 때가 있습니다. 
- 저의 경우는, 비디오나 gif를 만드려고 이미지를 여러 개 만들 때가 있는데, 이럴 때 이미지들은 다 임시로 만들어진 파일들이니까요, 이것들을 다 지워버리고 싶을 때가 있어요
- 그래서, 공부했습니다. 아래 코드를 보면, 되고, 별로 어렵지 않으니 자세한 설명은 제외하겠습니다. 

```python
import os
import matplotlib.pyplot as plt
import numpy as np 

#### 현재 경로 이동 
os.chdir('/Users/frhyme/frhyme.github.io/_posts/personal_ipynb/')
#### 현재 파일 경로 변환 
print(os.getcwd())
print("-"*20)
os.chdir('../../')
print(os.getcwd())
#### 현재 위치에 있는 폴더와 파일 프린트 
print(list(filter( lambda x: True if "." not in x else False, 
                  os.listdir())))
print("-"*20)
os.chdir('/Users/frhyme/frhyme.github.io/_posts/personal_ipynb/')

#### sample img generation 
img = np.random.normal(0, 1, (200, 200))
file_name = '180703_os_test_img.svg'
plt.figure(), plt.imshow(img, cmap=plt.cm.gray), plt.axis('off')
plt.savefig(file_name), plt.close()

#### 파일 지우기
#### 둘다 똑같이 동작함. 
print( file_name in os.listdir())
print(os.path.exists(file_name))
os.remove(file_name)
print( file_name in os.listdir())
print(os.path.exists(file_name))
print("-"*20)
```

```plaintext
/Users/frhyme/frhyme.github.io/_posts/personal_ipynb
--------------------
/Users/frhyme/frhyme.github.io
['_includes', '_posts', '_layouts', '_pages', 'Rakefile', '_site', 'Gemfile', '_data', '_sass', 'assets']
--------------------
True
True
False
False
--------------------
```

## bash command를 그대로 사용하고 싶을때

- 저는 bash command를 많이 쓰지는 않습니다. 아 생각해보니, `git status` 같은 것도 모두 배쉬 커맨드로군요. 
- 파이썬 내에서 터미널 작업도 같이 하고 싶을때는 다음처럼 쓸 수 있습니다. 

```python
import os
#### bash command를 실행만 시키고 싶을 때 
#### 하지만, 이 경우, 결과값을 반환하지 않음. 실행결과유무만 리턴됨 
r = os.system('pwd')
print('success' if r==0 else 'failed')
print("-"*30)

import subprocess
#### 실행결과를 리턴받고 싶을때 
#### 하지만, 이 때는 binary string으로 돌아오기 때문에, 변환해주는 것이 필요함. 
for cmd in ['pwd', 'git status']:
    binary_output = subprocess.check_output(cmd, shell=True)
    print("## command: {}".format(cmd))
    print(binary_output.decode('utf-8').strip())
    print("-"*30)
```

```plaintext
success
------------------------------
## command: pwd
/Users/frhyme/frhyme.github.io/_posts/personal_ipynb
------------------------------
## command: git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    ../a_python_os.md
	modified:   180703-os.ipynb

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	../2018-07-03-binary_str_to_str.md
  ../2018-07-03-python_os.md

no changes added to commit (use "git add" and/or "git commit -a")
------------------------------
```

## wrap-up

- 이제 터미널도 따로 안 써도 될것 같긴 한데...흠 좀 봐야겠군요. 
