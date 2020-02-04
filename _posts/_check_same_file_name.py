"""
- 가끔 _post 내의 파일들이 같은 이름을 가지고 있을 때가 있다. 
- 이는 과거에 썼던 내용을 최근에 다시 공부해서 새롭게 쓸 때, file_name이 같을 경우, permalink가 중복되어 문제가 발생함. 
- 이를 피하기 위해서, 파일이름을 "yyyy-mm-dd-filename_dsfdd.md"와 같이 맨 끝에 랜덤한 숫자륿 붙이는 것도 방법이지만, 
별로 아름다운 방법이 아님. 
- 따라서, 이 코드파일은 `_posts` 폴더 내에 존재하는 모든 파일을 읽고, 파일 이름이 중복되는지를 확인하기 위해 사용됨.
"""
import os

def return_all_file_names(input_p: str):
    """
    DEF: 경로(input_p) 내에 있는 모든 file을 list로 만들어 리턴함.
    p: path string
    해당 경로 내에 있는 모든 file을 리스트로 합쳐서 리턴함.
    """
    print(f"== recursion start:::: {input_p} ")
    return_file_name_lst = []  # 이 리스트에 모두 담음.
    for path_or_file in os.listdir(os.chdir(input_p)):
        # path가 file일 경우
        if os.path.isfile(f"{input_p}/{path_or_file}"):  # file
            return_file_name_lst.append(path_or_file)
        # path가 directory일 경우
        else:
            if os.path.isdir(f"{input_p}/{path_or_file}"):
                new_path = f"{input_p}/{path_or_file}"
                return_file_name_lst += return_all_file_names(new_path)
    print(f"== recursion end:::::: {input_p} ")
    return return_file_name_lst
#===============================================================

p_str = os.getcwd()
all_original_file_name_lst = return_all_file_names(p_str)
print("=="*20)
"""
- Valid markdown file
    - .md로 끝나고
    - yyyy-mm-dd- rk 정확하게 달려 있고
- 그런 아이들만 permalink만 뽑음.
"""
just_permalink_lst = []
for file_name in all_original_file_name_lst:
    if file_name[-3:]=='.md':
        if file_name[:2]=='20':
            just_permalink_lst.append(
                file_name[11:][:-3]
            )
        else:
            continue
    else:
        continue
# just_permalink_lst: list of permalink 

print("== duplicate check")
for permalink in just_permalink_lst:
    # count가 1보다 크면 duplicate
    if just_permalink_lst.count(permalink)>1:
        print(permalink)
print("== complete")
# check its duplicate 

