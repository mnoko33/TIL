[TOC]

# computed와 watch

**1. computed** 

자바스크립트 표현식을 mustache 태그 내에 넣으면 다양한 것을 표현할 수 있다. 하지만 연산이 복잡해질 경우 코드가 비대해진다. 따라서 복잡한 로직일 경우 computed를 사용하자

**2. computed vs method** 

computed 속성 대신 메소드와 같은 함수를 사용할 수 있다. 그리고 결과는 동일하다. 하지만 차이점이라면 computed는 종속 대상(피연산자?)을 따라 저장(캐싱)된다. computed 속성을 아무리 요청해도 변하지 않다가 종속 대상이 변할 경우 함수가 실행된다.

> computed는 종속 대상이 변해야 함수가 실행되므로 Data.now() 처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않는다.

**3. computed vs watch**

watch는 감시할 데이터를 지정하고 그 데이터가 바뀌면 어떠한 함수를 실행하라는 명령형 프로그래밍 방식이고 computed의 경우 계산해야 하는 목표 데이터를 정의하는 선언형 프로그래밍 방식이다.

**4. computed의 setter와 getter**

computed는 기본적으로 getter 함수만 가지고 있는데 필요한 경우 setter 함수를 만들어 쓸 수 있다. (쓸 일이 있을지는 모르겠다..)

```js
computed: {
	fullName: {
		// getter
        get: () => {
        	return this.firstName + ' ' + this.lastName    
        },
        // setter
        set: (newValue) => {
            const names = newValue.split(' ');
            this.firstName = names[0];
            this.lastName = names[names.length - 1]
        }
	}
}
```

**5. watch**

데이터 변경에 대한 응답으로 비동기식 or 시간이 많이 소요되는 **조작**을 수행하려는 경우 유용한 기능. 즉, 데이터 변경에 따라 어떠한 행위 즉 함수를 시행하기 위한 것

 

# Vue가 감지하지 못하는 변형

**1. 배열 변경**

javascript의 제한으로 인해 Vue는 배열에 대해 다음과 같은 방법으로 적용하는 변경 사항을 감지하지 못한다

(1) 인덱스로 배열에 있는 항목을 **직접** 설정하는 경우

(2) 배열 길이를 수정하는 경우

```js
const vm = new Vue({
    data: {
        items: ['a', 'b', 'c']
    }
})

vm.items[1] = 'x' // not reactive
vm.items.length = 2 // not reactive
```

따라서 배열의 인덱스를 직접 설정하는 것이 아닌 다음과 같이 해야한다.

```js
// Vue.set
Vue.set(vm.items, idxOfItem, newValue)
```

```js
// Array.prototype.splice
vm.items.splce(indexOfItem, 1, newValue)
```



**2. 객체 변경**

```js
var vm = new Vue({
    data: {
        a: 1
    }
})

vm.b = 2 // vm.b는 반응형이 아니다
```



-이벤트 핸들링부터