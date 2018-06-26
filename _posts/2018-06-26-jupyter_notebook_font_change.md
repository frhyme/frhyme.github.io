---
title: jupyter notebook 커스토마이징하기. 
category: python-lib
tags: python python-lib css jupyter-notebook customizing conda font-family
---

## 나는 갑자기 왜 jupyter notebook 설정을 바꾸었나 

- 최근에 뭘 코딩하다 보니까, 아나콘다를 새롭게 업데이트해야 되더라구요. 몇 가지 라이브러리만 하나씩 업데이트하면 좋았을 것을, 저는 개념없이, 통째로 코딩해버렸습니다....하하하 그 결과로, 이유는 모르겠지만, `jupyter notebook`의 폰트와 설정이 모두 바뀌어버렸더라구요. 
- 처음에는 당연히, 아나콘다의 문제라고만 생각하고, 몇번 갈아 엎었는데 그대로였습니다. 그 말인즉슨, 아나콘다의 문제가 아니고, jupyter notebook의 문제였다는 것이죠. 그래서 쥬피터 노트북의 설정을 바꾸기 시작했습니다. 

## conda is different with pip 

- 찾아보면, 대부분의 사람들이 `conda`가 아닌 `pip`를 사용해서 jupyter notebook을 설치했습니다. 어쩌면 사소한 차이인데, `pip`를 이용해서 설치한 사람들은 `~/.jupyter/` 경로가 존재합니다. 홈폴더 아래에 `.jupyter`폴더가 있다는 것이죠. 
- 하지만, 저는 없습니다... 그래서 와 이거 어떻게 해야 하나 싶었는데, [이 포스트](http://marinerism.blogspot.com)를 보니, 비교적 간단하게 처리할 수 있더군요. 콘다로 설치하신 분은 터미널에서 아래 명령어를 사용합시다. 
- 그럼 이제 `~/.jupyter`경로가 있습니다. 할렐루야. 

```bash 
jupyter notebook --generate-config
```

## customizing

- 커스토마이징하는 방법은 이제 간단합니다. 
- `~/.jupyter/` 아래에, `custom`이라는 폴더를 새로 만들고, 그 아래에 `custom.css`라는 파일을 만들어줍니다.
- `custom.css` 파일 내에 아래 설정을 넣어주면 됩니다. 
    - 적용된 건지, 안된건지 헷갈리니까 그냥 막 `font-size`를 34 뭐 이런식으로 세팅해서 보시는게 편합니다. 
    - 저는 쥬피터 노트북 가로폭을 넓게 보기 위해서 다음처럼 바꾸었습니다. 
    - 의미는 몰라요. 저는 css를 잘 모릅니다. 일단 필요한거만 세팅하고 나머지는 안 건드릴래요ㅎㅎㅎㅎㅎㅎㅎㅎ
        - [여기](https://gist.github.com/pmlandwehr/6bd26d0aabab5963a34dcaba1d6a18d4) 보면 jupyter notebook에서 사용하는 class들이 있는지, 왠지 이거인가? 싶은것을 보면서 고쳤습니다.
- 왠지 네이버 d2 폰트가 더 좋지 않을까? 싶어서 봤는데, 제가 설정한 `Consolas`도 충분히 좋습니다. 안 하기로 했어요 헤헤헤

```css
.CodeMirror pre {font-family: Consolas; font-size: 12pt; line-height: 140%;}
.container { width:100% !important; }
div.output pre{
    font-family: Consolas;
    font-size: 12pt;
}
```

## 테마 바꾸기. 

- 이렇게 일일이 바꾸는 것도 방법이지만, 더 예쁘게 만드는 방법도 있습니다. css를 잘아는 사람들은 알아서 뚝딱뚝딱 하겠지만, 잘 모르는 사람들은, 왠지 잘 되어 있는 무엇인가를 그대로 가져오는 것도 방법이니까요. 
- 그런 사람들은 위해서 `jupyterthemes`라는 것이 있습니다(pip 로 설치하셔야 합니다)
- 이걸 사용하면, 위의 `custom.css`등이 알아서 변경됩니다. 간혹 쥬피터 노트북의 하얀색 화면이 눈부시다는 분들도 계시는데 이 테마 중에서는 괜찮은 것들이 있으니 변경하시면 좋아요. 

### 라이브러리 설치 

```bash
pip install jupyterthemes
```

### 적용할 수 있는 테마 리스트업

```bash
jt -l 
```

### 테마 적용 

- 테마 적용(`themename`)내에 원하는 테마 이름을 넣어서 사용하시면 됩니다(위의 `jt -l`을 치면 테마 이름이 죽 나와요. 

```bash
jt -t themename
```

### 결과 확인 

- 그다음에 jupyter notebook을 실행해 보면(경우에 따라 다시 jupyter notebook을 실행해야 하는 경우도 있습니다), 테마에 맞춰서 달라져 있는 것을 알 수 있습니다. 동시에, `.jupyter/custom/`폴더에 들어가시면, `custom.css` 파일도 바뀌어 있고, `custom.js`파일도 바뀌어 있는 것을 볼 수 있습니다. 
- 결국, 테마를 적용한다는 것은, `custom` 폴더 내에 있는 파일들을 알아서 바꾸어준다는 것이죠. 

- 원래대로 돌아가고 싶으시면, 일단 `pip uninstall jupyterthemes`를 하시고, `custom.css`를 제외한 모든 파일은 없애주시면 될 것 같습니다. 

## wrap-up

- 사소하게 시작했는데, 꽤 먼길을 돌아왔습니다. 블로그에 써야 하는 것들이 많아졌네요. 
- jupyter notebook을 바꾸는 것도 방법이지만, 저는 그냥 이대로가 좋은 것 같아요. `matplotlib`로 그림을 많이 그리는데, 화면을 어둡게 하면 저 그림에서 손 봐야 할 부분들이 많이 늘어나는 것 같구요. 
- 상황에 맞춰서 몇 가지만 변경하면서 진행하면 좋을 것 같습니다. 저는. 


## reference

- <http://marinerism.blogspot.com>
- <http://pinkwink.kr/1039>
- <http://pythonanalysis.tistory.com/6>
- [쥬피터 테마 설정](https://www.opentutorials.org/module/2957/17787)