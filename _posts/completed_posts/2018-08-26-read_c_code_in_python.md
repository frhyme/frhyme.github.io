---
title: python에서 c 코드 읽어오기
category: python-lib
tags: python python-lib ctypes c 
---

## python에서 c 코드를 읽어옵시다. 

- [여기에](http://book.pythontips.com/en/latest/python_c_extension.html) 있는 내용을 참고했습니다. 새로운 부분은 없다고 봐도 됩니다. 영어를 한글로 바뀌었다는 것 정도? 아주 사소하죠.
- 흔히들 말합니다. 일단 크게는 파이썬으로 다 만들고 그 다음에 계산이 오래 걸리는 특정 부분들은 다른 언어 c, rust 등으로 작업하면 되는거 아니냐? 뭐 그렇게들 말하잖아요. 
- 그래요 만약에, 실제로 파이썬으로 대략 다 구현했고, 문제가 되는 부분은 c로 빨리 계산되도록 구현했다고 하면, 그 코드를 파이썬에서 어떻게 읽어올 수 있나요? 

## using ctypes 

- 일단 아주 간단한 c 코드를 작성해봅니다. 오랜만에 보는 코드네요. 아래 코드를 `add.c`라는 파일에 저장하고 

```c
#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}
```

- 이 코드를 바로 파이썬에서 쓸 수 없으니까 컴파일 해줍니다. gcc 오랜만에 보네요 극혐. 
- rust에서는 `rustc build`처럼 간단한 커맨드로 `.so`파일을 쉽게 만들 수 있었던 것 같은데 흠. 

```bash
gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
```

- 여기서 몇몇 분은 `.so`파일이 무엇인가? 라고 궁금해하실 수 있는데, 자세한 내용은 [여기에서](https://stackoverflow.com/questions/9688200/difference-between-shared-objects-so-static-libraries-a-and-dlls-so) 확인할 수 있습니다. 간단히 말하면, so는 shared object의 약자인데, 유닉스 계열에서 쓰는 말이고, dll은 dynamically linked library의 약자죠. 같은 말입니다. 

- 아무튼 위 커맨드를 수행하면 디렉토리에 `adder.so`라는 파일이 생성됩니다. 
- 아래 파이썬 코드에서 CDLL을 통해 `.so`파일을 읽어오면 그 다음부터 함수를 그대로 쓸 수 있습니다. 
- 가능하면 얼마나 더 빨라지는지까지도 체크해보면 좋을텐데 귀찮아요 하하하핫. 

```python
from ctypes import *

#load the shared object file
adder = CDLL('./adder.so')## DLL을 읽어옴 

#Find sum of integers
res_int = adder.add_int(4,5)
print("Sum of 4 and 5 = " + str(res_int))

#Find sum of floats
a = c_float(5.5)## ctypes에 정의된 float 
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print("Sum of 5.5 and 4.1 = ", str(add_float(a, b)))
```

## wrap-up

- ctypes에 대한 자세한 documentation은 [여기서](https://docs.python.org/3.7/library/ctypes.html) 볼 수 있습니다. 
- 속도가 문제라면 그냥 rust를 사용합시다 하하하핫. 