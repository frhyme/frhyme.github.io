---
title: Javascript - Object
category: javascript
tags: javascript object programming 
---

## Javascript - Object

- javascript의 Object를 간단히 정리하였습니다.

```javascript
// Object를 선언하는 데는 다음 두 가지 방법이 있다.
// 타 언어에서 Map, Dictionary로 표현되어 있는 자료구조가
// JS에서는 Object라는 이름으로 있다, 라고 생각해도 일단은 문제가 없다.
aObj = {
  name: "LSH",
  GPA: 4.3
};
bObj = new Object();
bObj.name = "HSL"
bObj.GPA = 2.0
// Object의 property를 지우고 싶으면
delete bObj.GPA


console.log(aObj); // {name: "LSH", GPA: 4.3}
console.log(bObj); // {name: "HSL"}
console.log(typeof aObj) // object
console.log(typeof bObj) // object
```

- 메소드는 다음처럼 만들죠. 

```javascript
person = {
  name: "LSH",
  age: 20,
  // 내부에서 다음처럼 정의해도 되고.
  printName() {
    console.log(this.name)
  }
}
// 외부에서 이렇게 정의할 수도 있습니다.
person.printAge = function() {
  console.log(this.age)
}

person.printName() // LSH
person.printAge() // 20
```