# DATA Finder

1. `findOrCreate` : 조건을 만족하는 인스턴스가 존재하는지 확인하고 없을 경우 생성하여 반환한다. 리턴값의 경우 `[instance, isCreated]` 이다.

   ```js
   const result = Model.findOrCreate({
       where: { key: value }
   })
   
   // result = [instance, isCreated]
   ```

2. `findAll` : 조건을 만족하는 모든 인스턴스를 리스트로 반환하는 것으로 조건에 맞는 여러 가지의 value를 정할 수 있다.

   ```js
   const result = Model.findAll({
       where: {key: [value1, value2, value3]}
   })
   
   // result = [instance1, instance2, instance3]
   ```

   



