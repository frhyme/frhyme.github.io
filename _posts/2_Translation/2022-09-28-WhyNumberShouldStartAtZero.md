---
title: (발번역) Why Number Should Start at Zero
category: translation
tags: Dijkstra zero
---

## Dijkstar - Why Number Should Start at Zero

- [(Original) Why Number Should Start at Zero](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)을 번역하여 아래에 작성하였습니다만, 번역이라고 하기에는 좀 너무 대충 중요한 부분만 선택해서 번역한 느낌이 있습니다. 원문을 그대로 보시면 아주 고급적으로 비꼬는 기술을 확인하실 수 있습니다.

## 번역 - 왜 번호 붙이기(numbering)은 0부터 시작해야만 하는가

### closed - open is better

- 2 ~ 12 의 연속된 자연수를 표현(의미)하기 위해서는 다음 과 같은 4가지의 표현 방법이 가능합니다.

```
1. 2 <= i < 13
2. 1 < i <= 12
3. 2 <= i <= 12
4. 1 < i < 13
```

- 1, 2번 방법들의 경우 두 bound(경계)간의 차이(difference)와 해당 구간 내에 존재하는 수의 개수가 같습니다. 예를 들어 1번의 경우 13 - 2는 11이고, 구간 내에 11개의 수가 존재합니다. 따라서 효율적이므로 우월합니다.
- 그리고 두 subsequence 가 연달아 존재할 때, 가령 `1 <= i < 3`, `3 <= i < 5`가 존재할 때, 한 쪽의 upper bound와 다른 한 쪽의 lower bound가 같아집니다. 따라서, 인접한 두 subsequence를 연결하기에도 효과적이죠.
- 2번과 4번의 경우 인위적으로 lower bound를 제외합니다. 만약 가장 작은 자연수(natural number)를 포함시키기 위해서는 2번과 4번에서 unnatural number를 가져와야 합니다. 이는 구리죠(ugly). 따라서, 우선, 1번과 3번이 우월합니다.

```
1. 0 <= i < 1
2. -1 < i <= 0
3. 0 <= i <= 0
4. -1 < i < 1
```

- 3번의 경우 가장 작은 자연수(smallest natural number)에서 출발하는 empty set를 표현할 경우 unnatural number를 사용해야 하는 경우가 발생할 수 있습니다. 이것도 구리죠(ugly). 따라서, 1번 방법이 가장 선호되는 것으로 결론을 내립니다.

```
1. 0 <= i < 0
2. 0 < i <= 0
3. 0 <= i <= -1
4. 0 < i < 0
```

- Xerox PARC에서 만들어진 programming language Mesa 에서는 1 ~ 4번을 표현할 수 있는 4가지 표기법이 모두 존재하였습니다. 1번을 제외한 다른 방법들은 모두 오류를 발생시킬 수 있다는 것이 해당 프로그래밍 언어의 사용 경험들에서 증명되었습니다.

### 0 based is better than 1 based

- 그럼 이제 2번째 질문으로, N 개의 길이를 가진 sequence를 처리해야 하는 경우 어떤 값이 Start number 로 선택되어야 하는지에 대해서 논의하자. 앞서 논의한 1번 방법이 우수하다는 결론 하에서, 10개의 sequence를 표현할 수 있는 방법은 다음 두가지가 존재한다. 다만, 1번 방법보다는 2번 방법이 더 깔끔하게 느껴집니다.

```
1. 1 <= i < N + 1
2. 0 <= i < N
```

## Conclusion

- 발번역을 한 다음 찾아보니, [shoark7 - why numberin should start at zero](https://shoark7.github.io/programming/knowledge/why-numbering-should-start-at-zero-kr)에 더 잘 정리된 번역글이 있습니다. 이해가 안되시면 이곳으로 가시면 더 좋을겁니다 호호.
- 또한 원문에는 좀 더 해당 글을 쓰게 된 이유와, 비꼬는 문장들이 꽤 보이는데요, 해당 내용은 제외해도 상관없다고 판단하여 제외하였습니다.

## Reference

- [(Original) Why Number Should Start at Zero](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)
- [shoark7 - why numberin should start at zero](https://shoark7.github.io/programming/knowledge/why-numbering-should-start-at-zero-kr)
