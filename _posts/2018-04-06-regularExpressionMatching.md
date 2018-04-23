# regularExpressionMatching(s, p)

## Problem

- https://codefights.com/interview-practice/task/Sx8ndFtwEyCRRqF7q/
- string s가 regular expression 으로 정의된 pattern p를 따르는지를 체크하는 함수를 만들어봅니당
	- regular expression은 많이 써보지는 않았지만, 쓰다보면 편하다고들 합니다. 물론 미리 배워둘 필요는 없을 것 같고 나중에 헤헤. 
- 여기서 전부를 다 만들지는 않고, 간단히 * , . 에 대해서 만듭니다. 
	- * 은 바로 이전에 나온 캐릭터가 0번에서 n 번까지 나올 수 있다는 것을 표현
	- . 은 어떤 캐릭터든 될 수 있다 를 말합니다. 

### regular expression example 

- 예시는 대략 다음과 같지만, 사실 아래만으로 헷갈릴 수 있습니다. 구글에서 '정규표현식'이라고 치시면 다양한 자료들이 나오니까 간단하게 보시면 좋을 것 같아용. 
	- a* : "", "a", "aa", ...
	- b* : "", "b", "bb", ...
	- ab* : a, ab, abb, abbb.
	- a\*b\* : "", "a", "ab", "abbb", "aaabbbb", ...
	- . : a, b, c, d, e, ....
	- .* : can be any string. 

### solution 

- 우선 예제로 나오는 pattern에서는 . * 이 복잡하게 얽혀서 나오기 때문에, 입력받은 pattern을 * 로 split하는 함수를 만듭니다. 

```python
def splitPattern(p):
    if "*" in p:
        i = 0 
        j = i+1
        rs = []
        while j<len(p):
            if p[j]=="*":
                temp= p[i:j]+"*"
                if temp[:-2]!="":
                    rs.append(temp[:-2])
                rs.append(temp[-2:])
                i = j+1
                j = i+1
            else:
                j=j+1
        if i<len(p):
            rs.append(p[i:j])
        return rs
    else:
        return [p]
```

- 그 다음 해당 string이 해당 pattern으로 시작하는지를 확인하는 함수를 만듭니다. 
	- 여기서 pattern에는 * 가 포함되어 있지 않다고 가정했습니다. 

```python
def startWith(s, p):
    if len(s)<len(p):
        return False
    else:
        for i in range(0, len(p)):
            if p[i]=='.':
                continue
            else:
                if s[i]!=p[i]:
                    return False
        return True
```

- 여기가 본 함수인데요, dynamic programming에서 가장 중요한 것은, 음 뭐 recursive라고 해도 상관없죠, 아무튼 여기서 중요한 것은 언제 break point가 걸리냐는 것인데, 가장 작을 때, 즉 우선 딱 하나의 pattern에 대해서만 완벽하게 처리하고 이후에는 다 남은 pattern에 대해서 처리하는 식으로 reduction을 하면 되는 것이긴 합니다. 
- 저는 앞서 설계한 `splitPattern` 이라는 함수를 활용해서 pattern을 쪼개주고 이후에는 이미 쪼개진 패턴을 argument로 입력받는 함수를 만들어 전개했습니다. 

- 여기서 제가 어려워 했던 부분은 `.*`부분인데요, 
	- `.*` 은 같은 문자가 반복되지 않는 경우도 포함합니다. 
		- ab, abc, abcd 모두 포함됩니다. 
	- 따라서 이 부분이 조금 해결하기가 어렵죠. 물론 풀고 나면 너무 간단하기는 합니다만. 

```python
def regularExpressionMatching(s, p):
    def re_with_plst(st, ps):
        if len(ps)==1:
            if "*" in ps[0]:
                cand_lst = []
                if ps[0][0]=='.':
                    return True
                else:
                    c = ps[0][0]
                    for i in range(0, len(st)):
                        if st[i]!=c:
                            return False
                        else:
                            continue
                    return True
            else:
                if len(st)!=len(ps[0]):
                    return False
                else:
                    return startWith(st, ps[0])
        else:
            if "*" in ps[0]:
                if ps[0][0]=='.':
                    return any([re_with_plst(st[i:], ps[1:]) for i in range(0, len(st)+1)])
                else:
                    c = ps[0][0]
                    start_pos = 0
                    for i in range(0, len(st)):
                        if st[i]!=c:
                            start_pos=i
                            break
                    zero_count = re_with_plst(st, ps[1:])
                    nonzero_count = re_with_plst(st[start_pos:], ps[1:])
                    return any([zero_count, nonzero_count])
            else:
                if startWith(st, ps[0]):
                    return re_with_plst(st[len(ps[0]):], ps[1:])
                else:
                    return False
    return re_with_plst(s, splitPattern(p))
```
