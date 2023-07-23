---
title: markdown에서 image 파일 사이즈 변경하기
category: other
tags: markdown blog image

---

## intro

- 간단하게 이미지를 업로드하는 방법은 다음과 같습니다. 

```markdown
![google](https://goo.gl/qwGmse)
```

![google](https://goo.gl/qwGmse)

- 픽셀 사이즈를 조절하려면 뒤에 딕셔너리 같은걸 붙여주면 되요. 

```markdown
![google](https://goo.gl/qwGmse){: width="10" height="10"}
```

![google](https://goo.gl/qwGmse){: width="100" height="100"}

- 퍼센트로 조절하려면 `%`를 넣어주면 되요. 

```markdown
![google](https://goo.gl/qwGmse){: width="50%" height="50%"}
```

![google](https://goo.gl/qwGmse){: width="50%" height="50%"}
