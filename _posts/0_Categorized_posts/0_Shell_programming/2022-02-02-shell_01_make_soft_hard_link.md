---
title: Shell01 - Make Symbolic Link (ln)
category: shell
tags: shell link
--- 

## Shell01 - Make Symbolic Link (ln)

- unix terminal에서 자주 접근하는 folder path가 길어서, 빠르게 접근할 수 있는 link를 만들어주려고 합니다.
- 이렇게 만들어주고 나면, cd를 여러번 칠 필요 없이 바로 움직일 수 있습니다.
- `ls -l`을 사용해서 확인해 보면, link가 잘 만들어진 것을 확인할 수 있습니다.

```bash
$ ln -s ~/frhyme.github.io/_posts/ frhyme_posts
$ ls -l
```

## soft link vs. hard link

- link는 기본적으로 hard link와 soft link로 구분됩니다. 앞서 만든 link는 soft link죠.
- 두 link 모두 원본 파일을 가리키는 일종의 shortcut, 바로가기 다, 라는 개념은 같지만, 세부적으로는 조금씩 다른 부분들이 있습니다. 
- 이해를 돕기 위해서 간단하게 만들어보면서 설명해보도록 할게요.
- soft_link, hard_link를 각각 만들고, 각 file의 inode 값을 확인 해보면, `raw_file.md`, `raw_file_hard_link`의 inode 값은 동일하고, soft_link의 inode값은 다른 것을 확인할 수 있습니다. "hard link의 경우 inode값이 원본과 동일하고, soft link의 경우 inode 값이 원본과 다르다"라는 것이, 중요합니다. 

```bash
$ vi raw_file.md
$ ln -s raw_file.md raw_soft_link
$ ln raw_file.md raw_hard_link
$ ls -il
total 16
59689582 -rw-r--r--  2 seunghoonlee  staff  17  2  2 14:35 raw_file.md
59689582 -rw-r--r--  2 seunghoonlee  staff  17  2  2 14:35 raw_file_hard_link
59689591 lrwxr-xr-x  1 seunghoonlee  staff  11  2  2 14:36 raw_file_soft_link -> raw_file.md
```

- soft link의 경우 원본 파일의 내용이 변경되면 동일하게 soft link에서도 변경되나, 원본 파일의 이름이 변경되거나, 원본 파일이 삭제되면 할 수 있는 것이 아무것도 없습니다. 가리키는 원본 파일이 삭제되었으므로 쓸모없는 파일이 되죠.
- 반면, hard link의 경우 원본 파일의 내용이 변경되면 동일하게 반영됨은 물론, 파일의 이름이 변경되거나, 원본 파일이 다른 폴더로 움직여도 여전히 원본 파일과 연결되어 있습니다. 또한, 원본 파일이 삭제되어도 여전히 원본파일에 접근할 수 있음은 물론, 본인이 원본인척 하게 됩니다.
- 이 차이점은 보이는 원인이 바로 inode가 동일하기 때문이죠. 

### inode

- inode는 Index Node의 약자로, Unix에서 사용하는 file 등에 대한 정보를 저장하기 위한 자료구조입니다. 기본적으로 서로 다른 개체를 가리키는 경우에는 inode number가 달라야 하죠.
- Unix에서 사용자가 file에 접근하기 위해서는 filename에 mapping된 inode number를 확인 -> inode number에 해당하는 inode를 확인하여 해당 개체의 실제 물리적 위치를 확인 하는 순서로 진행됩니다.
- 만약 접근하는 대상이 soft link라면, soft link에 mapping된 inode number를 확인 -> inode number에 해당하는 inode를 확인 -> soft link이므로 inode 에서 raw file inode를 확인 -> 실제 물리적 위치를 확인 하는 순서로 진행되죠.
- 반면, hard link의 경우, hard link에 mapping된 inode number를 확인 -> (raw file 과 동일한) inode number에 해당하는 inode를 확인 -> 실제 물리적 위치를 확인 하는 순서로 진행됩니다.
- 즉, 정리하면 soft link는 파일의 경로를 저장해서, 파일의 경로에 접근하는 바로가기를 만든다, 라고 생각하시면 됩니다. hard link는 원본 파일과 동일한 inode에 접근하여, 원본과 동일한 물리적 위치에 직접 접근한다, 정도로 이해하면 됩니다.
- 종종 hard link에서 원본 파일을 그대로 복사한다, 라는 식으로 설명되어 있는 글들이 있는데요, 복사하지 않습니다. 가리키는 inode값이 같고 파일 크기도 같아서 복사해왔다, 라고 생각할 수 있지만, 좀 더 깊은 레벨에서 동일한 파일을 가리키는 셈이죠.

### Hard link not allowed for directories

- hard link는 soft link와 다르게 directories에 대해서 만들어질 수 없습니다. 이는 다른 inode를 공유하는 soft link와 다르게 hard link의 경우 동일한 inode를 공유하기 때문이죠.
- file 탐색은 기본적으로 대상이 acyclic(loop가 없는)이라는 것을 가정하고 돌아갑니다. folder를 뒤져가면서 file을 찾아야 할때, 대상 폴더 구조에 loop가 있다면, 탐색에 무한 loop가 발생하여 탐색이 종료될 수 없습니다.
- 만약 hard link가 folder를 대상으로 만들어질 수 있다면, hard link의 경우 동일한 inode값을 가지므로, hard link에서 parent folder를 가리키는 다음과 같은 경우에, 무한 루프가 발생할 수 있습니다. folder를 순회하는 기능을 실행하게 되면 b -> hard_link -> b -> hard_link의 순서로 folder를 뒤지게 될 테고, 무한 루프가 되는 것이죠.

```bash
$ mkdir -p a/b/
$ ln a/ b/hard_link
```


## Wrap-up

- 대충 hard_link, soft_link의 차이점에 대해서 정리해 봤습니다. "왜 hard link는 directory에 적용할 수 없지?"라는 간단한 호기심 때문에, 이걸 해결하기 위해 inode가 대충 무슨 개념인지 확인했고, 사실은 hard link가 대상을 복사(deep copy)하는 것이 아니라, 대상을 가리키는 방법 자체가 달라서 복사한 것처럼 보인다, 라는 사실도 알게 되었습니다. 처음보다 더 자세한 내용을 알게 된 것 같아서 기분이 좋네요 호호호.


## Reference

- [askubuntu - why are hard links not allowed for directories](https://askubuntu.com/questions/210741/why-are-hard-links-not-allowed-for-directories)
- [왜 Directory에 hard link를 만들 수 없나요](https://notes.harues.com/posts/why-hard-link-not-allowed-for-directory/)
- [[Linux] 리눅스 시스템의 아이노드(inode), 심볼릭 링크(Symbolic Link), 하드 링크(Hard Link)에 대해서.](https://i5i5.tistory.com/341)
