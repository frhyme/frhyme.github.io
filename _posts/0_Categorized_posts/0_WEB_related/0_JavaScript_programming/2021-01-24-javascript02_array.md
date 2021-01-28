---
title: Javascript - Array
category: javascript
tags: javascript programming array
---

## Javascript - Array

- Javascrip의 Array를 간단히 정리하였습니다.

```javascript
// Array는 다음 두 가지 방식을 사용해서 정의할 수 있다.
arr1 = [1, 2, 3];
arr2 = new Array();
// .push를 사용해서 뒤에서부터 집어넣는다.
arr2.push('A');
arr2.push('B');
arr2.push('C');
console.log("Popped Item: " + arr2.pop());
// Popped Item: C
console.log(arr2); // ["A", "B"]
arr2.shift();
console.log(arr2); // ["B"]
arr2.shift();
console.log(arr2); // []

for(x in arr1) {
  console.log(x);
}
```

- Array는 `.forEach()` 메소드로 다음처럼 실행할 수도 있죠. 

```javascript
arr = ["A", "B", "C"]
arr.forEach((x) => console.log("X: " + x))
/*
X: A
X: B
X: C
*/
// element: Array의 각 요소
// index: 각 요소의 index
// array: array
arr = ["A", "B", "C", "D"]
arr.forEach(function(element, index, array){
    console.log(`Array: ${array} - ${index}th element : ${element}`);
});
/*
Array: A,B,C,D - 0th element : A
Array: A,B,C,D - 1th element : B
Array: A,B,C,D - 2th element : C
Array: A,B,C,D - 3th element : D
*/
```

- `.slice()`를 사용해서 subArray를 만들 수도 있죠.

```javascript
arr = ["A", "B", "C", "D"]
console.log(arr.slice(0, 2)) // ["A", "B"]
```
