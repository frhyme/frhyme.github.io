---
title: python string으로 컴파일하기
category: python-basic
tags: python python-basic string 

---

## string을 코드로 바로 돌릴 수 있을까요? 

- 원래는 `ipynb`파일을 파이썬에서 바로 import할 수 없을까? 고민하다가 궁금해진 부분이긴 한데요. 
- 외부에서 만든 코드를 `.py`로 가져오는 경우에는 `import filename`로 하면 그대로 되니까 문제가 없습니다만, `string`으로 가져와야 하는 경우도 가끔 있습니다. 
    - `ipynb`에서 특정 부분만 가져와서 컴파일해야 하는 일도 있을 수 있으니까요. 
- 아무튼 그럴때 `string`을 바로 컴파일해서 해당 `string`에 있는 함수를 사용할 수 있을까요?
- 역시 구글에 찾아보니, [비슷한 답](https://stackoverflow.com/questions/19850143/how-to-compile-a-string-of-python-code-into-a-module-whose-functions-can-be-call)이 있습니다. 하핳

### code 

- 해당 코드를 실행한 다음에는 그냥 foo(a)를 실행해도 에러 없이 실행됩니다. 
```python
exec("""
a = 10
print(a)
def foo(a):
    print(a+10)
foo(a)
""")
```

### result 

```
10
20
```