---
title: Javascript - Object Constructor
category: javascript 
tags: javascript programming object constructor function
---

## Javascript - Object Constructor

- javascript에서는 `function`을 사용해서 Object Constructor를 만들어 줍니다.

```javascript
/*
- object constructor
*/
function Student(name, studentID) {
    this.name = name;
    this.studentID = studentID;
    // method를 정의할 때도 function을 사용합니다.
    this.printName = function() {
        console.log(`Student - name: ${this.name}, ID: ${this.studentID}`)
    }
}
// new를 넣는 것을 잊어버리지 마세요.
s1 = new Student("LSH", 11);
s2 = new Student("LHS", 12);

s1.printName()
// Student - name: LSH, ID: 11
s2.printName()
// Student - name: LHS, ID: 12
```
