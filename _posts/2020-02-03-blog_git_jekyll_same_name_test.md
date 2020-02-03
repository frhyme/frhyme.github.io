---
title: Blog - 다른 폴더 경로에 같은 이름의 마크다운 파일이 있다면? 
category: blog
tags: blog jekyll github
---

## `_posts` 폴더 내에 여러 폴더들이 있어서, 이름이 겹치는 경우가 있습니다. 

- 블로그를 만들고 공부한 것들을 정리하기 시작한 지도 어느새 2년이 다 되어 갑니다. 처음에는 그냥 모든 마크다운 파일들을 하나의 폴더 `_posts`내에 모두 집어넣었었죠. 그런데, 이게 일정 시간을 지나니까 이제는 주체할 수가 없게 되어버린 것이죠. 하나의 폴더내에 몇 백개의 글들이 있으니까, 관리가 안 되고 또한, "제가 어떤 분야의 공부를 어느 정도로 했는지에 대한 정확한 측정"이 어려워졌습니다. 
- 따라서, 얼마전에 각 폴더 별로 글의 내용들을 따로 관리하기 시작했습니다. 처음에는 폴더별로 구분을 해두면, jekyll이 build를 못하는줄 알았는데, 그냥 `_posts` 폴더 내에 `yyyy-mm-dd-filename.md`의 형태로 파일이 있기만 하면, 알아서 잘 읽는 것 같아요.
- 아무튼, 그래서, 폴더별로 만들어서 관리를 하고 있었는데, 갑자기 다음과 같은 warning이 뜹니다. 딱히, 블로그가 build가 안되는 것 같지는 않고, `ing`상태로 진행되더라는 이야기죠. 결과적으로는 별 문제가 없긴 했습니다만. 

> Some checks haven’t completed yet 
> 1 in progress and 1 pending checks

- 아무튼, 결과적으로는 별 문제가 없긴 했습니다만, 신경이 쓰여서, **무엇이 문제일 수 있을까?**하고 고민을 해봤습니다만, 어쩌면 **다른 경로에 있는 같은 이름의 파일때문에 문제가 발생하는 게 아닐까?**라는 생각으로 이어졌습니다. 
- 간혹, 과거에 공부했던 내용을 다시 정리해서 공부할 때가 있는데요. 그럴때 우연히도 file name들이 겹칠 수가 있는 것이죠. 가령 `2020-01-30-aaa.md`, `2020-02-03-aaa.md`이라는 파일이 서로 다른 디렉토리에 동시에 존재한다면, 문제가 될 것 같아요. 왜냐면, 둘다 다음과 같은 경로를 가지게 되니까요
- jekyll은 build 시에 file이름을 가지고 해당 파일에 대한 link를 생성하는 것으로 알고 있습니다. 즉 만약, `yyyy-mm-dd-testA.md`라는 파일에 대해서 category 를 `python-libs`로 만든다면, 다음과 같이 표현되죠. 
    - `https://frhyme.github.io/python-libs/testA/`
- 따라서, 개념적으로, 서로 다른 폴더에 같은 이름의 파일이 있다면, 서로 다른 내용이더라도, 하나의 링크에 연결됨으로써 문제가 발생할 수 있죠. 저는 진짜, 그런지 한번 테스트를 해보기로 했습니다. 


## same date, file name in different folder

- 서로 다른 폴더에 각각 같은 파일 이름인 `2020-02-03-testA.md`을 설정하고, 서로 다른 내용을 집어넣었습니다.
- 뭐, 이건 추가 설명을 넣을 필요가 없을 것 같은데, 앞에서 말한 것과 같이, 이렇게 할경우, 2개의 링크가 있는것처럼 보이지만, 마치, **전화기를 2개 쓰는 배달음식집**처럼 하나의 글만 보이게 됩니다. 


## how to solve it? 

- 이건 어쩌면, 블로그를 오래하게 되면 자연스럽게 발생하는, 문제점이라고 생각됩니다. 결과적으로, 파일 이름만 다르면 되는 것이라면, 그냥 앞과 뒤에 모두 날짜를 적어주면, 서로 다른 `permalink`를 만들어줄 것이므로 문제가 해결될 것 같기는 합니다만, 별로 똑똑한 방법은 아니죠.
- 저는 일단, `_posts` 폴더 내에 있는 모든 파일의 이름들을 recursive하게 읽어서, 리스트로 가져온 다음, 중복되는 링크가 있는지를 체크해봅니다. 
- 아래 python 코드는 해당 폴더 내의 모든 파일의 이름을 가져오는 함수죠. 

```python
import os

def return_all_file_names(input_p:str):
    """
    DEF: 경로(input_p) 내에 있는 모든 file을 list로 만들어 리턴함.
    p: path string
    해당 경로 내에 있는 모든 file을 리스트로 합쳐서 리턴함.
    """
    print(f"== recursion start:::: {input_p} ")
    return_file_name_lst = [] # 이 리스트에 모두 담음.
    for path_or_file in os.listdir(os.chdir(input_p)):
        # path가 file일 경우
        if os.path.isfile(f"{input_p}/{path_or_file}"):# file
            return_file_name_lst.append(path_or_file)
        # path가 directory일 경우
        else:
            if os.path.isdir(f"{input_p}/{path_or_file}"):
                new_path = f"{input_p}/{path_or_file}"
                return_file_name_lst += return_all_file_names(new_path)
    print(f"== recursion end:::: {input_p} ")
    return return_file_name_lst
#===============================================================

p_str = "/Users/frhyme/frhyme.github.io/_posts/"
all_original_file_name_lst = return_all_file_names(p_str)
```


## wrap-up

- 어쨌거나, 여전히 무엇대문에 앞서 말한, 아래의 오류가 발생했는지는 모르겠네요. 그냥 잊어버리기로 합니다 호호호

> Some checks haven’t completed yet 
> 1 in progress and 1 pending checks




