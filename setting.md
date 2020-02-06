[TOC]

# Node.js

### 1. nodemon

파일을 관찰하고 있다가 변경점이 발생하면 자동으로 애플리케이션을 재시작해주는 도구

```
npm install nodemon --save-dev
```



### 2. babel

`babel` : ES6/ES7 코드를 ECMAScript5 코드로 transpiling해주는 도구.

* `@babel/core` : 바벨의 핵심 파일로 바벨의 다른 모듈들이 종속성을 가진다.
* `@babel/node` : 바벨의 CLI
* `@babel/preset-env` : 바벨의 preset 중 하나로 es6+ 이상의 js를 각 브라우저/노드 환경에 맞는 코드로 변환



위의 모듈 세가지를 설치한 후, 폴더의 최상단에 `.babelrc` 파일을 만들고 다음과 같이 설정한다

```
{
	"presets": ["@babel/preset-env"]
}
```



그리고 다서 `package.json` 의 실행 스크립트를 수정한다

```
"start": "nodemon ./bin/www --exec babel-node"
```

