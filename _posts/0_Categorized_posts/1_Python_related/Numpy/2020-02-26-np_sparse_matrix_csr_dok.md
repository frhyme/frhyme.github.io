---
title: scipy - sparse matrix. 
category: python-libs
tags: python python-libs scipy sparse-matrix dictionary
---

## What is sparse matrix? 

- [Sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix)는 한국말로 "희소행렬"이라고 할 수 있으며, 대부분이 비어 있는 행렬(matrix)라고 생각하시면 됩니다. 
- 예를 들어 보겠습니다. 우리에게 행이 100, 열이 100개인 matrix가 있습니다. 즉, 10,000개의 원소가 존재하는 것이죠. 이 때, 0이 아닌 실제 값이 존재하는 경우는 10개밖에 없다고 합시다. 그렇다면, 10개의 원소를 저장하기 위해서, 9990개의 자리와 계산이 낭비되고 있는 것이죠.
- 따라서, 이렇게 낭비되는 것을 막기 위해서 "희소행렬"이 존재하는 것이죠. 

## sparse matrix types. 

- sparse matrix는 다양한 종류가 있지만, 저는 다음 두 가지에 대해서만 설명하려고 합니다. 
    - `csr_matrix` : Compressed Sparse Row matrix 라고 하며, 보통 가장 많이 사용되는 형태. 
    - `dok_matrix` : Dictionary Of Keys based sparse matrix이며, dictionary처럼 데이터를 관리하고, dictionary로 정의해줄 수 있으므로 interface가 편함.

### `csr_matrix`

- `csr_matrix`는 "Compressed Sparse Row matrix"를 의미하며, 보편적으로 많이 사용되는 matrix죠. 거의 대부분의 scipy function들에서도, [scipy.sparse.csr_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html)를 기본 형태로 사용하는 일이 많습니다.
- `scipy.sparse.csr_matrix`는 `row_position`, `col_position`, `values` 이렇게 세 값을 argument로 넘겨서 만들 수 있습니다.

```python 
import numpy as np
from scipy import sparse

row_positions = np.array([0, 0, 1, 2, 2, 2])
col_positions = np.array([0, 2, 2, 0, 1, 2])
values = np.array([1, 2, 3, 4, 5, 6])
# 당연히 위 세개의 길이는 동일해야 함.
assert len(row_positions) == len(col_positions) == len(values)

csr_mat1 = sparse.csr_matrix((values, (row_positions, col_positions)), shape=(3, 3))
```

### dok(Dictionary Of Key) matrix

- [`dok matrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_matrix.html)는 그냥 dictioanry의 형태로 데이터를 관리해준다는 이야기입니다. 그게 다에요.
- 따라서, 생성해줄 때도 마치 dictionary처럼 만들어줍니다.

```python 
from scipy.sparse import dok_matrix

shape = (5, 5)
dok_mat = sparse.dok_matrix(shape)
for i in range(0, 5):
    dok_mat[i, i] = i**3
print(dok_mat)
```

## file size.

- `csr_matrix`에 대해서 `npz` format으로 저장하는 경우와, `np.array`를 저장하는 경우를 모두 파일로 저장하여 파일 용량이 어느 정도나 차이 나는지 체크해봤습니다. 
- 사실, 당연히, `matrix`의 크기가 커질수록 용량 차이는 많이 나며, N이 10000일 때, 약 28배 정도의 차이가 나는군요. 메모리에 올릴 때도 아마 비슷할 겁니다.

```python
import numpy as np
from scipy import sparse

N = 10000

np_arr = np.eye(N)
sparse_mat = sparse.csr_matrix(np.eye(N))
# save them as compressed file
if True:
    np.savez_compressed('np_arr.npz', np_arr)
    sparse.save_npz('sparse_mat.npx', sparse_mat, compressed=True)
```

## wrap-up

- 기본적으로 `scipy.sparse.csr_matrix`는 `numpy.array`와 거의 문제없이 돌아갑니다. 대부분의 method가 유효하므로 이 부분은 설명하지 않고 넘어갔습니다. 다만, 그래도, operation의 결과로 반환되는 타입이 변할 수 있으므로 가능하면 형변환에 문제가 없도록 관리하면서 진행하는 것이 필요하죠.


## reference 

- [Scipy sparse matrix handling](https://lovit.github.io/nlp/machine%20learning/2018/04/09/sparse_mtarix_handling/)
- [scipy.sparse.csr_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html)
- [scipy.sparse.dok_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.dok_matrix.html)
