# 비구조화 할당

ES6의 비구조화 할당을 사용하면 쉽게 나타낼 수 있다.

```react
import React from 'react';

const myComponent = props => {
    const {name, age} = props;
    return (
    	<div>
        	제 이름은 {name} 이고 나이는 {age} 입니다.
        </div>
    );
};
```

함수의 파라미터 부분에서도 사용 가능하다

```react
import React from 'react';
const myComponent = ({name, age}) => {
    return (
    	<div>
        	제 이름은 {name} 이고 나이는 {age} 입니다.
        </div>
    );
};
```

