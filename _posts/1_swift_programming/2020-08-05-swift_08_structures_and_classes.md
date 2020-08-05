---
title: swift - chapter 8 - Structures and Classes
category: swift
tags: swift tutorial structure class
---

## swift - chapter 8 - Structures and Classes

- Structure, Class는 모두 대상을 보다 효과적으로 관리하기 위한 '묶음'이라고 생각하시면 됩니다. 가령, 우리가 '사람'을 코드에 녹여 넣어야 한다고 할 때, 지금까지는 '사람에 대한 데이터'는 따로, '이 사람이 수행하는 동작(function)'도 따로 관리를 했어야 했습니다. 그런데, 코딩하려는 대상이 복잡해지면 이렇게 따로 관리하는 데 문제가 발생하게 되죠.
- 따라서, 이 둘을 효과적으로 통합하기 위해서 struct, class와 같은 개념들이 나오게 됩니다.
- 다만, class는 프로그래밍에서 핵심적인 개념이고 간단하게 읽어서는 이해할 수 없는 부분들이 많습니다. 본 챕터에서는 매우 간단하게 몇몇 내용들을 설명하고 있는데, 만약 이해가 되지 않더라도, 일단은 넘어가시는 게 좋습니다. 이후에 더 자세하게 설명된 내용을 보시면 이해하실 수 있을 거에요.

## Struct, Class in swift

- struct와 class는 기본적으로 조금 다른데, swift에서는 다른 언어들에 비해서 공통점이 많다고 합니다. 따라서 본문에서도 보통 'class instance'를 칭할 때 object라고 하지만, swift에서는 struct와 class 간에 차이가 거의 없기 때문에, 전반적으로 그냥 instance라는 말을 주로 사용하겠다고 합니다.
- swift 책에 나온 개념을 가져와서 아래의 내용을 정리하였지만, 이 내용들은 단지 몇 문장만으로는 이해하기 어려운 것이 사실입니다. 일단은 '대략 그렇구나'라고 이해하시고, 추후 챕터를 공부하시면 더 정확하게 알 수 있을 거에요.

### Both Struct and Class can do

- struct와 class는 모두 다음의 것들을 수행할 수 있습니다. C에서 배웠던 struct에 비해서 swift에서의 struct는 좀 더 넓은 기능을 수행할 수 있는 것처럼 보입니다. 가령, C에서는 struct가 생성자를 가지지 못했던 것 같아요.
- swift에서 struct와 class는 모두 다음의 특성을 가집니다.
  - **Define properties to store values and methods to provide functionality**: 값을 저장하기 위해 property, 기능을 수행하는 method를 정의할 수 있다.
  - **Define subscripts to provide access to their values using subscript syntax**: subscript, `[]`를 사용하여 값에 접근할 수 있도록 정의할 수 있다.
  - Define initializers to set up their initial state: 초기상태를 설정할 수 있는 initializer(생성자)를 정의할 수 있다.
  - **Be extended to expand their functionality beyond a default implementation**: 초기에 구현된 상태(default implementation)을 넘어 기능을 확장할 수 있다. Class의 경우 상속(inheritance)을 사용해서 이 부분이 가능할텐데, struct의 경우는 어떠한 방식으로 이를 가능하게 한다는 이야기인지 조금 궁금하네요.
  - **Conform to protocols to provide standard functionality of a certain kind**: 특정한 종류의 표준적인 기능을 공급하기 위해서, protocol에 순응할 수 있다. 

### Only Class can do

- 또한, struct는 할 수 없지만, class만 할 수 있는 것으로는 다음의 것들이 있습니다.
- **Inheritance enables one class to inherit the characteristics of another**: 상속을 사용해서 한 class의 기능을 다른 class에서도 사용할 수 있도록 할 수 있다.
- **Type casting enables you to check and interpret the type of a class instance at runtime**: type casting(형변환)이 runtime시에 class들간의 관계를 체크하고 변환해준다. 이건 class들에 대해서만 가능하다는 이야기죠.
- **Deinitializers enable an instance of a class to free up any resources it has assigned**: deinitizlier는 C++에서의 destuctor처럼 보이는데, 음 뭐, 할당된 instance를 해제해준다는 말로 보이네요.
- **Reference counting allows more than one reference to a class instance.**: Reference Counting은 간단히 말하자면, "메모리를 효과적으로 관리하기 위하여 현재 참조하고 있는 개체들의 수를 계속 관리하는 것"을 말합니다. 만약, 참조되고 있지 않은 개체가 있다면 이 아이를 해제함으로써, 메모리를 효율적으로 관리하는 것이죠. 아무튼, 이 때 여기서 하나의 class instance에 대해서 여러 개의 reference가 가능하도록 지원한다는 말인데, 이건 당연한 말로 보이기도 해서 나중에 다른 챕터에서 정확히 무엇을 말하는지 꼼꼼하게 봐야 할 것 같아요.

## Initializer

- C++의 경우 class 정의 시에 내부에 생성자를 따로 정의해주었어야 했습니다. 하지만, swift에서는 생성자를 따로 method처럼 정의할 필요 없고, 자동으로 만들어지죠. 또한 swift의 경우 모든 변수에 초기 값을 설정하는 것이 기본이기 때문에, 아래와 같이, 그냥 값을 선언/정의하고 생성자를 바로 콜하면 되는 식이죠.

```swift
struct Student{
    var name = "Lee"
    var id = 2000
}
class School{
    var students:[Student] = []
}

var student1 = Student()
print(student1) // Student(name: "Lee", id: 2000)

var school = School()
school.students.append((student1))
print(school.students[0]) // Student(name: "Lee", id: 2000)
```

### Member-wise Initializer for struct 

- struct에 대해서는 다음처럼, property를 변경하여 initializer를 통해 instance를 생성하는 것이 가능합니다.

```swift
struct Student{
    var name = "Lee"
    var id = 2000
}

var student1 = Student(name:"Kim")
print(student1) // Student(name: "Kim", id: 2000)
```

- 하지만, class에 대해서는 적용되지 않는 것처럼 보여요. 이 부분이 지금은 명확하지 않은데, 이후에 왜 안되는지 정리해보도록 하겠습니다.

```swift
class Student{
    var name = "Lee"
    var id = 2000
}

var student1 = Student(name:"Kim") // Error: Argument passed to call that takes no argument
print(student1) // 
```

## Structures  are Value type

- 'value type'이라는 것은 간단히 말해, `=` 연산자를 이용해서 다른 변수로 지정해주면, 그 값이 그대로 복사된다는 것을 말합니다. 즉, 기본적으로 deep copy를 지원한다, 라고 이해하셔도 상관없습니다.
- 우리가 흔히 알고 있는 int, float 등과 같은 기본적인 primitive type은 모두 value type이죠. 즉, `=`를 사용하면 그대로 값이 복사되지, 같은 메모리 공간을 가르키는 것이 아닙니다.

```swift
struct Student{
    var name = "Lee"
    var id = 2000
}

// student1을 만듭니다.
var student1 = Student()
// Struct는 value type이므로 이렇게 assign해주면 알아서 deep copy됩니다.
var student2 = student1
// deep copy이므로, student1의 name이 바뀐다고, student2의 name이 바뀌면 안됨.
student1.name = "Kim"

print(student1.name) // Kim
print(student2.name) // Lee
```

## Classess are reference type

- 반면, class의 경우는 reference type입니다. 즉, 정의된 `.copy` 메소드를 사용하지 않는다면, shallow copy가 발생한다는 이야기죠. 값이 복사되어 새로운 메모리 공간을 차지하는 것이 아니라, 기존의 메모리 공간을 그대로 가리키게 된다는 말입니다.
- 이전의 코드의 `struct`를 `class`로 바꾼 다음 코드를 보시면, shallow copy가 발생하는 것을 알 수 있습니다.

```swift
class Student{
    var name = "Lee"
    var id = 2000
}

// student1을 만듭니다.
var student1 = Student()
// Class는 reference type이므로, assign해주면 shallow copy가 됩니다.
var student2 = student1
// shallow copy이므로, student1의 name이 바뀌면, student2의 name도 바뀝니다.
student1.name = "Kim"

print(student1.name) // Kim
print(student2.name) // KIM
```

### Identity operator

- class는 reference type이기 때문에, 하나의 개체에 대해서, 여러 reference를 가지는 것이 가능합니다. 앞서 본 것처럼 여러 개체가 동시에 참조할 수 있죠. 반대로, struct나 다른 기본적인 타입들의 경우는 이것이 불가능하죠.
- 여기서, 두 개체가 같은 개체를 참조하고 있는지 확인하기 위해서는 `===`를 사용합니다. identity operator라고 하죠. 반대로는 `!==`를 사용합니다.

```swift
class Student{
    var name = "Lee"
    var id = 2000
}

var student1 = Student()
var student2 = Student()
var student3 = student1

print(student1===student2) // false
print(student1===student3) // true
```

- 다만 헷갈리지 않아야 하는 것은 지금 "값이 같은지를 확인하는 것이 아니라는 것"이죠. equality operator가 아니라, 같은 개체를 참조하고 있는지를 파악하기 위한 Identity operator를 의미합니다.

## wrap-up

- 아주 간단하게 struct와 class를 정의하였습니다. struct는 value type, class는 reference type이라는 것도 다시 알게 되었고, identity operator도 다시 봤습니다. python에서는 identity operator 가 `is`죠.
- 새로운 언어를 배우다 보니, 프로그래밍의 기본 개념들에 대해서 다시 정리되는 기분이 듭니다. 새로운 언어를 배운다는 것은 역시 아주 좋은 취미생활입니다 호호호.