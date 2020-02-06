[TOC]

# credential.helper

`git pull` 또는 `git push` 할 때, 이메일과 비밀번호를 입력하는 것을 생략하기 위한 방법으로 --global을 붙일 경우 모든 git 활동에 대해 이를 적용한다

`#> git config credential.helper store`

임시적으로 이를 사용하기 위해선 cache를 통해 만료기간을 설정할 수 있다 (15분)

`#> git config credential.helper cache `

만료시간을 timeout 옵션으로 지정할 수 있다 (초 단위)

`#> git config credential.helper 'cache --timeout=3600)`



# git add/commit/push 취소

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



# git flow

## 1. branch CRUD

### 1. Create

* `git branch [branch name]` : 브랜치 생성
* 👋 `git checkout -b [branch name]` : 브랜치 생성 후 해당 브랜치로 이동
* 👍 `git checkout -b [branch name] [remote branch name]` : 원격 브랜치에서 새로운 브랜치를 만들어내고 연동 
* 👍 `git checkout -t [remote branch name]` : remote 브랜치를 그대로 복사해오고 연동
* `git push origin [branch name]` : remote에 브랜치 생성
* `git checkout -tb [new local branch name] origin/[new local branch name]`  로컬 브랜치를 생성하고 remote 브랜치와 연동

### 2. Read

* `git branch`: local
* `git branch -r` : remote
* `git branch -a ` : remote + local

### 3. Update

* `git pull` : 모든 사항 업데이트
* `git remote prune origin` : remote에서 삭제한 브랜치 업데이트

* `git branch -u origin HEAD` : local에서 만든 branch를 remote에 적용
* `git push origin [branch name]` : local 브랜치를 remote로 push
* 

### 4. Delete

* `git branch -delete [branch name]` : local 브랜치 삭제
* `git branch -D [branch name]` : commit 이력을 무시하고 삭제
* `git push origin :[branch name]` : local에서 삭제한 브랜치를 remote에서도 삭제

