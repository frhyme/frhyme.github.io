---
title: python에서 이미지 비디오로 변환하기. 
category: python-lib
tags: python python-lib jupyter-notebook 

---

## jupyter notebook에서 HTML등 보여주기 

- 최근에 강화학습을 공부하고 있습니다. 강화학습은 사실 게임 AI를 만드는 것과 비슷합니다. 즉 계속 화면에 게임 화면처럼 계속 바뀌는, 애니메이션을 그려주는 것이 필요하죠. 제가 계속 확인하면서 하면 좋으니까요. 
- 그런데, jupyter notebook은 이걸 원활하게 지원하지 못해요. 계속 어떤 라이브러리가 없다, 어떤 문제가 있다, 하면서 뭐라뭐라 하는데, 이걸 어떻게 해결할 수 있을지 고민하고 있습니다. 
- 그래서, 처음에는 `matplotlib.animation`에서 뭔가를 할 수 있을 것 같아서 계속 했는데, 잘 안되는것 같아요 
    - ㅇㅇ
    - ㅇㅇ

- 그래서 아예 그냥 비디오로 만들어버리는 것이 나을 것 같더라구요. 



https://docs.opencv.org/master/d9/df8/tutorial_root.html

- **우선, jupyter lab에서는 javascript가 지원되지 않습니다. 그래서 저는 jupyter notebook에서 진행했습니다**


http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

http://blog.extramaster.net/2015/07/python-pil-to-mp4.html

https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python