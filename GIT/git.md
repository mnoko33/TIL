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



