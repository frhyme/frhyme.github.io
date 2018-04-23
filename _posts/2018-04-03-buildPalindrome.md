# buildPalindrome

## Problem
- 문자열 s 로부터 만들 수 있는 가장 짧은 Palindrome을 만들어주는 함수입니다. 
- s가 이미 Palindrome라면, 해당 문자열을 그대로 리턴하면 되고, 아닐 경우에는 해당 문자열을 이용해 새로 만들어줘야겠죠.

## solution 

- 우선 문자열이 Palindrome인지 확인해주는 함수를 만들어봅니다. 

```python
def isPalindrome(st):
    if len(st)%2==0:
        return st[:len(st)//2]==rev_str(st[len(st)//2:])
    else:
        return st[:len(st)//2]==rev_str(st[len(st)//2+1:])
```

- 또한 문자열을 역으로 만들어 리턴해주는 함수도 만듭니다. 

```python
def rev_str(st):
    return "".join(reversed(st))
```

- 입력받은 문자열 `st`를 문자를 하나씩 순서대로 읽어나가면서 남아있는 문자열이 palindrome인지 확인합니다. 
- 만약 남아있는 문자열이 palindrome일 경우 지금까지 읽어들인 문자열을 역으로 만들고 뒤에 붙여서 리턴해줍니다. 

```python
def buildPalindrome(st):
    for i in range(0, len(st)):
        if isPalindrome(st[i:]):
            return st+rev_str(st[:i])
    return st+rev_str(st)
```
