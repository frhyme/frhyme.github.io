# kpalindrome

## Problem

- palindrome이 무엇인지는 이미 다들 알고 계신것 같아용, 앞뒤로 읽어도 똑같은 스트링을 말합니당(1577 1577말고 1577 7751 이용)
- 다만, kpalindrome의 경우는 해당 문자열에서 k개 이하의 문자를 삭제했을때, palindrome이 되는지를 확인해주는 함수를 말합니다. 
	- 왠지 간단하게 풀 수 있을 것 같은 착각이 드는데, 아마도 그렇다면 이 문제 또한 계산시간이 오래 걸리겠죠. 

## solution

- 생각보다 쉽게 해결되어서 좀 당황스러운데....
- 아무튼, palindrome은 우선 끝에서부터 체크를 하면 될것 같았습니다. 
	1. 왼쪽 끝과 오른쪽 끝의 문자가 같은 경우: call kpalindrome(s[1:-1], k)
	2. 다를 경우: 
		1. 왼쪽을 삭제할 경우: call kpalindrome(s[1:], k-1)
		2. 오른쪽을 삭제할 경우: call kpalindrome(s[:-1], k-1)
- 아무튼 이렇게 풀었습니다. 

```python
def isPalindrome(s):
    if len(s)<=1:
        return True
    else:
        if len(s)%2==0:
            return s[:len(s)//2]==s[len(s)//2:][::-1]
        else:
            return s[:len(s)//2]==s[len(s)//2+1:][::-1]
def kpalindrome(s, k):
    if len(s)<k:
        return True
    else:
        if k==0:
            return isPalindrome(s)
        else:
            if s[-1]==s[0]:
                return kpalindrome(s[1:-1], k)
            else:
                return any([kpalindrome(s[1:], k-1), kpalindrome(s[:-1], k-1)])
```
