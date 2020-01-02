---
title: matrix decomposition
category: python-lib
tags: python python-lib numpy matrix-decomposition linear-algebra scipy
---

## matrix decomposition 을 정리합니다. 

- 원래는 matrix decomposition을 해서, 이후에 또 어디에 쓰일 수 있다, 뭐 이런 부분까지 쓰려고 했는데, 정작 정리하고 나니, 그부분을 쓰는게 모호해지더라구요. 
- 그냥, 필요에 따라서 행렬방정시에서 계산을 좀 효율적으로 하거나 하는 데 쓰이곤 합니다. 

```python
import numpy as np 
from scipy.linalg import lu, inv, svd, cholesky
## decomposition 

a = np.arange(1, 10).reshape(3, 3)
print("--------------------")
print("triangular upper: \n{}".format(np.triu(a)))
print("triangular lower: \n{}".format(np.tril(a)))
print("--------------------")
print("inverse array: \n{}".format(inv(a)))
print("--------------------")
p, l, u = lu(a)
print('p l u factorization: \n{}, \n{}, \n{}'.format(p, l, u))
print("--------------------")
print("p.dot(l).dot(u): \n{}".format(p.dot(l).dot(u)))
print("--------------------")
U, s, V = svd(a)
print("singular value decomposition: \n{}, \n{}, \n{}".format(U, s, V))
```

```
--------------------
triangular upper: 
[[1 2 3]
 [0 5 6]
 [0 0 9]]
triangular lower: 
[[1 0 0]
 [4 5 0]
 [7 8 9]]
--------------------
inverse array: 
[[  3.15251974e+15  -6.30503948e+15   3.15251974e+15]
 [ -6.30503948e+15   1.26100790e+16  -6.30503948e+15]
 [  3.15251974e+15  -6.30503948e+15   3.15251974e+15]]
--------------------
p l u factorization: 
[[ 0.  1.  0.]
 [ 0.  0.  1.]
 [ 1.  0.  0.]], 
[[ 1.          0.          0.        ]
 [ 0.14285714  1.          0.        ]
 [ 0.57142857  0.5         1.        ]], 
[[  7.00000000e+00   8.00000000e+00   9.00000000e+00]
 [  0.00000000e+00   8.57142857e-01   1.71428571e+00]
 [  0.00000000e+00   0.00000000e+00  -1.58603289e-16]]
--------------------
p.dot(l).dot(u): 
[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  9.]]
--------------------
singular value decomposition: 
[[-0.21483724  0.88723069  0.40824829]
 [-0.52058739  0.24964395 -0.81649658]
 [-0.82633754 -0.38794278  0.40824829]], 
[  1.68481034e+01   1.06836951e+00   3.33475287e-16], 
[[-0.47967118 -0.57236779 -0.66506441]
 [-0.77669099 -0.07568647  0.62531805]
 [-0.40824829  0.81649658 -0.40824829]]
```