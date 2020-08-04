---
title: python) Contour 플롯을 그려봅시다. 
category: python-lib
tags: python python-lib matplotlib
---

## 등고선이란 말입니다

- 그냥 contour라고 말하면 헷갈리는데, 지도에서 등고선이랑 같은 개념이라고 보시면 됩니다. 대충 아래 그림처럼, 비슷한 높이에 있는 놈들기리 묶어줍니다. 이런걸 contour라고 하죠. 

![contour_Img_web](https://i.stack.imgur.com/tjOQZ.png)

- 사실 원래는 `contour`를 정리하려고 했던 것이 아닌데, `decision boundary`를 그리다 보니, `contourf`를 사용해서 그리더라고요. 그래서 이걸 이참에 한번 정리하는게 좋을 것 같았습니다. 

## 우선, meshgrid 

- `plt.contour(X, Y, Z)`의 `X`, `Y`, `Z`는 모두 2차원의 `np.array`여야 합니다. 특히, `X`, `Y`의 경우는 `np.meshgrid`로 생성을 하는데, 음, 이를 조금 더 설명하자면, 
- '메쉬그리드'란, 한국말로는 그물망이고, 원하는 지역의 좌표를 X, Y로 구분하여 서로 다른 매트릭스로 리턴해주는 함수입니다....말로 하니 이상한데, 아무튼 코드로 보면, 
- matrix a는 [1,2,3]이 행별로 반복되고, matrix b는 열별로 반복되죠. 이런 형태를 meshgrid라고 하는 것 같아요....사실 잘 모르겠습니다, 반드시 이렇게 넘겨줘야 하는 이유는. 

```python
a, b = np.meshgrid([1,2,3], [1,2])
print(a)
print(b)
```

```plaintext
[[1 2 3]
 [1 2 3]]
[[1 1 1]
 [2 2 2]]
```

- 결과적으로, x, y 좌표 리스트만 각각 가지고 있으면 아무 문제가 없는 건데, 그걸 꼭 2차원 어레이 형태로 가지고 있어야 하고, `plt.contour`에도 2차원 어레이로 넘겨줘야 하는 건가요? 흐음. 
  - 똑같은 내용을 `reshape(-1, 1)`로 해서 넘겨주면 컨투어가 그려지지 않습니다, 뭐, 아무튼 그냥 하라는 대로 하죠 뭐. 

## contour 를 그립시다

- 자 아래처럼 그릴 수 있습니다. 참 쉽죠?

```python
Xmesh, Ymesh = np.meshgrid(np.linspace(-3.0, 3.0, 1000),
                     np.linspace(-3.0, 3.0, 1000)
                    )
print("XX.shape: {}".format(Xmesh.shape))
print("YY.shape: {}".format(Ymesh.shape))
Z = np.sqrt(Xmesh**2 + Ymesh**2 )

plt.figure(figsize=(12, 5))
"""levels에 구간을 넣어줘서 등고선 표시 위치를 정할 수 있습니다. 
"""
cp = plt.contourf(Xmesh, Ymesh, Z, 
                 levels = np.linspace(Z.reshape(-1, 1).min(), Z.reshape(-1, 1).max(), 50)
                )
plt.colorbar(cp)
plt.savefig('../../assets/images/markdown_img/draw_contour_20180529_1727.svg')
plt.show()
```

![contour_img](/assets/images/markdown_img/draw_contour_20180529_1727.svg)

## wrap-up

- contour 플롯을 그려본 이유는, decision boundary를 그려 보기 위함입니다. 이후에 decision boundary를 그리는 포스트에서 contour를 이용하겠습니다. 

## reference 

- [Matplotlib Tutorial: Contour Plots](https://www.python-course.eu/matplotlib_contour_plot.php)