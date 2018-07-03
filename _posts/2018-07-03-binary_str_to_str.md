---
title: binary string을 string으로 바꾸기 
category: python-lib
tags: python python-lib binary string subprocess bash ascii utf-8
---

## binary string을 string으로 바꿉시다. 

- python에서 직접 bash command를 사용할 일이 있습니다. 저는 `subprocess` module을 사용해서 직접 커맨드를 치곤 합니다. 
- 그런데, 이 때 결과물을 보면, `string`이 아니라 `binary` format으로 들어오는 것을 알 수 있어요. 
- 그래서 간단하게 binary string을 string으로 바꾸어주려고 합니다. 

## do it

- bash command를 실행해보면, 출력되는 스트링 앞에 `b` 라는 성가신 글자가 붙어 있는 것을 알 수 있습니다. 타입 또한, string이 아니라, `<class 'bytes'>`인 것을 알 수 있습니다. 
- 단순히 `str`로 바꿔주면 맨 앞의 `b`가 그대로 남아 있는 것을 알 수 있죠. 

```python
import subprocess 

bin_a = subprocess.check_output('git status', shell=True)
print(type(bin_a))
print('--'*10)

print(bin_a)
print('--'*10)

str_a = str(a)
print(str_a[0]) 
print('--'*10)
```

```
<class 'bytes'>
--------------------
b'On branch master\nYour branch is up to date with \'origin/master\'.\n\nChanges not staged for commit:\n  (use "git add/rm <file>..." to update what will be committed)\n  (use "git checkout -- <file>..." to discard changes in working directory)\n\n\tdeleted:    ../a_python_os.md\n\tmodified:   180703-os.ipynb\n\nUntracked files:\n  (use "git add <file>..." to include in what will be committed)\n\n\t../2018-07-03-binary_str_to_str.md\n\t../2018-07-03-python_os.md\n\nno changes added to commit (use "git add" and/or "git commit -a")\n'
--------------------
b
--------------------
```

- 그래서, 단순히 `a.decode('ascii')`로 실행하면 깔끔하게 잘 나옵니다. 
- 만약 원래대로 돌리고 싶으면, `encode`로 원래대로 돌리면 됩니다. 

```python
decoded_a = a.decode('ascii')
print(decoded_a)
print('--'*10)
print(decoded_a.encode('ascii')==bin_a)
```

```
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

--------------------
True
```

## 한글의 경우 

- 예전에 프로그래밍 수업을 들어보신 분들은 아시겠지만, 지금 `ascii`라는 값이 지금 들어있잖아요? 이는 해당 문자열을 바이트로 변환할때, 어떤 문자표로 변환할 것인지를 말합니다. 
    - 간단하게 문자표로 생각하셔도 됩니다. 개별 단어들이 숫자에 배치되는 것이죠. 
- 그런데, ascii의 경우는 영문만 표현이 됩니다. 따라서 한글의 경우는 ascii로 인코딩 디코딩하면 문제가 생깁니다. 

- 따라서, 다음처럼 utf-8로 진행해주셔야 합니다. 

```python
test_a = '이승훈'
print(test_a)
print(test_a.encode('utf-8'))
print(test_a.encode('utf-8').decode('utf-8'))
```

```
이승훈
b'\xec\x9d\xb4\xec\x8a\xb9\xed\x9b\x88'
이승훈
```

## reference 

- <https://stackoverflow.com/questions/17615414/how-to-convert-binary-string-to-normal-string-in-python3>