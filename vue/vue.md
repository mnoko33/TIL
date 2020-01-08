[TOC]

# computed와 watch

**computed** 

자바스크립트 표현식을 mustache 태그 내에 넣으면 다양한 것을 표현할 수 있다. 하지만 연산이 복잡해질 경우 코드가 비대해진다. 따라서 복잡한 로직일 경우 computed를 사용하자

**computed vs method** 

computed 속성 대신 메소드와 같은 함수를 사용할 수 있다. 그리고 결과는 동일하다. 하지만 차이점이라면 computed는 종속 대상(피연산자?)을 따라 저장(캐싱)된다. computed 속성을 아무리 요청해도 변하지 않다가 종속 대상이 변할 경우 함수가 실행된다.

> computed는 종속 대상이 변해야 함수가 실행되므로 Data.now() 처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않는다.

**computed vs watch**

watch는 감시할 데이터를 지정하고 그 데이터가 바뀌면 어떠한 함수를 실행하라는 명령형 프로그래밍 방식이고 computed의 경우 계산해야 하는 목표 데이터를 정의하는 선언형 프로그래밍 방식이다.

**computed의 setter와 getter**

**watch**

