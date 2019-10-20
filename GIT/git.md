[TOC]

## credential.helper

`git pull` 또는 `git push` 할 때, 이메일과 비밀번호를 입력하는 것을 생략하기 위한 방법으로 --global을 붙일 경우 모든 git 활동에 대해 이를 적용한다

```
#> git config credential.helper store
```

임시적으로 이를 사용하기 위해선 cache를 통해 만료기간을 설정할 수 있다 (15분)

```
#> git config credential.helper cache 
```

만료시간을 timeout 옵션으로 지정할 수 있다 (초 단위)

```
#> git config credential.helper 'cache --timeout=3600)
```



## git add/commit/push 취소

1. git add 취소하기 (파일을 unstage로 변경)

   `git reset HEAD [filename]` : 특정 파일을 unstaged 상태로 바꾼다. 파일명이 없을 경우 staged된 모든 파일을 되돌린다.

2. git commit 취소하기

   `git reset HEAD^`: commit을 취소하고 해당 파일들을 unstaged 상태로 되돌린다. (add 전)

   `git reset --soft HEAD^` : commit을 취소하고 해당 파일들을 staged 상태로 되돌린다. (add 후)

   `git reset --hard HEAD^` : commit을 취소하고 해당 파일들을 삭제.

3. commit message 변경

   `git commit --ammend` : git commit message를 변경

4. 현재 작업 중인 디렉토리를 원격 저장소의 마지막 commit 상태로 되돌리기

   `git reset --hard HEAD`

5. 원격 저장소의 파일을 삭제하기

   `git rm --cached [fimename]` : 원격 저장소에 push된 해당 파일을 삭제한다