import numpy as np

## 테스트할 함수를 만들어봄 
def func1(s):
    a = np.array([i for i in range(0, s)])
    return a.mean()
def func2(s):
    a = [i for i in range(0, s)]
    return sum(a)/len(a)

#assert func1(s)==func2(s)
def test_func1(benchmark):
    benchmark(func1, 10000000)
def test_func2(benchmark):
    benchmark(func2, 10000000)