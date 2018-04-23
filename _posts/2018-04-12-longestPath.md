# longestPath(fileSystem)

## Problem

- string `a`를 입력받고, 존재하는 파일 중 string size가 가장 긴 path 를 찾아서 리턴해주는 함수를 만든다. 
- `a = "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt"` 를 프린트하면 다음과 같다. 
	- picture와 documents의 경우, user의 하위폴더이며, photo.png, camera의 경우 picture 폴더의 하위 파일과 폴더. 

```
user
	pictures
		photo.png
		camera
	documents
		lectures
			notes.txt
```


## solution

- 지난번에 배웠던 tree 구조와 유사하기 때문에 tree 구조를 활용해보기로 한다. 
	- 단, binary tree가 아니어서 여러 명의 child node를 가질 수 있다
	- 상위 node는 여전히 하나만 가능함. 
	- 단 값을 가진 최상위 node는 두 개가 될 수도 있기 때문에, root를 값을 가지지 않는 dummy node로 만들었다. 

- node 정의는 다음과 같다. 
	- 기존 binary tree와 유사하게 느껴질 수 있으나, downs에는 list가 들어올 예정이다. 

```python
class node(object):
    def __init__(self, x):
        self.name = x
        self.upper = None
        self.downs = None
```


- string `fileSystem` 은 다음으로 변환되어 make_tree로 넘어온다. 
	- temp = [(f.replace('\t', ''), f.count('\t')) for f in fileSystem.split("\f")]
		- "\f"는 "\n"과 같다. 
- temp의 각 원소는 (name, count of "\t")로 이루어지는데, "\t"가 tree에서 위치한 level이므로 이를 고려하여 배치해주고, 새로운 node가 생성되었을 때, upper, downs를 잘 배치하여 넣어준다. 

```python
def make_tree(temp):
    top = node("")
    top.downs = [node(temp[0][0])]
    top.downs[0].upper = top
    cursor = top.downs[0]
    for i in range(1, len(temp)):
        name = temp[i][0]
        level = temp[i][1]
        #print(name, level)
        #print('cursor', cursor.name)
        if temp[i-1][1]<level:
            if cursor.downs is None:
                cursor.downs = [node(name)]
                cursor.downs[0].upper = cursor
                cursor = cursor.downs[0]
            else:
                cursor.downs.append(node(name))
                cursor.downs[-1].upper = cursor
                cursor = cursor.downs[-1]
        else:
            k = temp[i-1][1]-level+1
            for j in range(0, k):
                cursor = cursor.upper
            cursor.downs.append(node(name))
            cursor.downs[-1].upper = cursor
            cursor = cursor.downs[-1]
    return top
```


- make_tree로부터 만든 tree에서 생성할 수 있는 모든 path를 리턴해준다. 
	- 단, 해당 path의 leaf는 반드시 file name이어야 한다. 폴더는 불가함. 

```python
def all_paths(t):
    rs = []
    def all_paths_helper(t, prefix):
        if t is None:
            rs.append(prefix)
        else:
            if t.downs is None:
                rs.append(prefix+t.name)
            else:
                for d in t.downs:
                    all_paths_helper(d, prefix+t.name+"/")
    all_paths_helper(t, "")
```


- longestPath에서 이전에 정의한 함수를 활용하고 예외를 처리한 다음, 리턴한다. 

```python
def longestPath(fileSystem):
    fileSystem= fileSystem.replace("    ", "\t")
    temp = [(f.replace('\t', ''), f.count('\t')) for f in fileSystem.split("\f")]
    if len(temp)==1:
        if "." in temp[0][0]:
            return len(temp[0][0])
        else:
            return 0
    else:
        t = make_tree(temp)
        ps = all_paths(t)
        ps = filter(lambda p: True if "." in p.split("/")[-1] else False, ps)
        ps = list(map(lambda p: p[1:], ps))
        if len(ps)>0:
            return len(max(ps, key=lambda x: len(x)))
        else:
            return 0
```
