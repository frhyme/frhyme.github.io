---
title: git pull 을 생활화합시다. 
category: others
tags: git 
---

- 그동안 commit을 한동안 안하다가, 오랜만에 커밋을 했더니 이상한 오류가 뜨면서 안됩니다. 

```
To https://github.com/frhyme/frhyme.github.io.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/frhyme/frhyme.github.io.git'
```

- 아마도 저는 기억이 잘 안나는데, 제가 깃헙 홈페이지에서 제 깃헙을 뭐 좀 건드렸다거나 그런것을 했었나봐요. 언제 했지. 
- 아무튼 그래서 지금 제 로컬에 있는 폴더와 깃헙에 있는 폴더에 싱크가 안 맞는거죠. 그래서 위와 같은 오류가 발생했습니다. 

- 깊게 고민하지 마시고 아래 커맨드를 실행하시면 됩니다. 로컬파일들을 그대로 덮어씌우는 것이 아니라, 보통은 그대로 두고 업데이트된 파일들만 가져옵니다. 

```
git pull origin master 
```

- 그리고 가능하면 깃헙 웹에서 바로 파일을 수정하시는 것은 지양하는 게 좋습니다. 

## GPG 

- 웹에서 깃헙 커밋 기록을 쭉 보면 `README.md`파일에만 verifed가 되어 있는 것을 볼 수 있습니다. 대략 아래 그림처럼 올라오죠(귀찮아서 아무 그림이나 퍼왔습니다).

![](https://www.google.co.kr/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi77bTv3vrcAhVC2LwKHcrUC_EQjRx6BAgBEAU&url=https%3A%2F%2Fwww.ahmadnassri.com%2Fblog%2Fgithub-gpg-keybase-pgp%2F&psig=AOvVaw29yEcQLj6qy75qooK5jS6U&ust=1534823937527377)

- 제 맥북에서 하면 `verified` 표시가 안되는데, 웹에서는 저렇게 표시가 되는게 약간 부럽다고 할까요??? 그래서 제가 맥에서 뭘 올리면 모두 `verifed`가 되도록 처리해보기로 했습니다. 

- [자세한 내용은 여기서](https://blog.outsider.ne.kr/1209) 보시는게 훨씬 좋구요 하하핫. 

- 막상 하려고 보니 귀찮아서 안하기로 했습니다 하하하하핫 제가 그렇져 뭐 


 ## reference 

 - <https://stackoverflow.com/questions/28429819/rejected-master-master-fetch-first>