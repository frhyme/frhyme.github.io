---
title: Java - 메모리를 어떻게 구분하고, 어떻게 관리하는가?
category: java
tags: java programming JVM stack heap static GarbageCollection
---

## Java - 메모리 관리

- 컴퓨터 구조를 나누면, 연산은 CPU가 하고 CPU에서 연산을 처리하기 위해 값을 기억해두는 놈은 Memory라는 놈이 하죠. 일단은 그냥 그렇게 되어 있다, 라고만 해석해도 상관이 없기는 합니다. 하지만, 프로그래밍 언어에 따라 메모리를 어떻게 세부적으로 구분해서 관리하는지는 조금씩 다릅니다.
- C에서는 OS에서 메모리를 직접 관리하도록 합니다. `malloc()`과 `free()`를 사용하여 메모리를 할당하고, 해제하죠.
- 반면 Java의 경우는 OS 위에 JVM이라는 가상 머신을 올리고, 이 가상머신에서 코드가 돌아가도록 합니다. OS로부터 허락을 받아서 JVM은 메모리를 사용하고, 그 메모리를 사용해서 프로그램을 돌리는 것이죠. 이 경우에는 OS 레벨에서의 메모리 누수는 발생하지 않습니다.
- 오늘은 Java가 메모리를 어떻게 세부적으로 구분하는지 등에 대해서 정리해보려고 합니다. 아래 JVM Architecture 기준으로 보면, Runtime Data Area 부분을 자세히 보려고 해요.

![JVM_Architecture](https://i2.wp.com/blogitwithsatyam.com/wp-content/uploads/2018/06/jvm-architecture.png?resize=720%2C471&ssl=1)

## Method Area 

- Class의 field, method code 등이 모두 Method Area에 담겨 있다고 보시면 됩니다. Static으로 표현되는 클래스 변수들도 모두 이 부분에 담겨져 있죠.
- 새로운 Class를 만들 때, 그리고 각 Instance에서 사용하는 Method들이 모두 담겨져 있는 부분이기 때문에, Instance들에 의해서 접근이 가능합니다. 따라서, 새로운 Instance를 만들 때는 Method Area에 있는 Class에 관한 정보를 읽고, 이를 통해 새로운 Object를 만들게 됩니다.
- 다만, 이렇게 쓰고 보면, 마치 Method Area를 담는 공간이 Heap이나, Stack이 아닌 독립적인 메모리처럼 느껴지지만, 그렇지만은 않았습니다.

### Java 1.7 이하에서의 Method Area

- 일반적으로 Method Area에는 "Class MetaData", "Method Metadata" 그리고 "static object"들이 저장됩니다. static하다는 것은, class instance에 종속되는 것이 아니라, class 자체에 종속되는 것을 말하죠. 
  - Class, Method method 정보
  - Static Object
  - String Object
- 이 때 Method Area는 Heap Memory 내의 PermGen(Permanent Generation Heap)이라는 영역에 저장되어 있었습니다. Heap은 GC를 통해 메모리를 관리하는데, Permanent Generation은 "시간이 지나도 GC되지 않는 영속적인 놈들"이라고 해석하면 되겠죠. 즉, 절대로 메모리를 해제하지 않는 영역, 이라고 해석하면 됩니다.
- 다만, PermGen은 메모리의 크기가 작았을 뿐만 아니라, 프로그램 내에서 메모리의 공간을 탄력적으로 조정할 수 없었습니다. 가령, 프로그램이 시작되고, PermGen의 용량이 부족하다면(가령, Static object가 너무 많아서) 다음의 에러와 함께 프로그램이 뻗는 것이죠.

```plaintext
java.lang.OutOfMemoryError: PermGen space
```

- 이 경우는 두 가지로 구분됩니다. 1) 개발자가 Static object를 아주 많이 만들어서, PermGen이 넘치는 경우, 2) Class, Method의 Metadata가 증가하는 경우. 어쨌든 PermGen의 메모리가 부족하여 반복적으로 문제가 발생하게 되니까, Java 1.8에서는 PermGen을 없애버리는 극단적인 결정을 내리게 됩니다.

### Java 1.8 이상에서의 Method Area 

- 하지만, Java 1.8부터는 PermGen영역이 사라지고 MetaSpace라는 영역이 생겨났습니다. 또한, MetaSpace는 Heap 내에 존재하는 영역이 아니라, off-heap, 즉 OS가 직접 관리하는 Native Memory에 속하게 됩니다. 이전에 비해 탄력적으로 메모리를 사용할 수 있다는 강점이 있죠.
- 다만, Class, Method의 Metadata는 MetaSpace로 넘어갔지만, **Static Object는 MetaSpace에 포함되지 않고, 여전히 Heap영역에서 관리됩니다.**
- 다만, PermGen이 없어졌으므로, 이 말대로면 static object 또한 Garbage Collection의 영역에 포함될 수 있다, 는 것처럼 보이는데 흠...이건 좀 더 알아볼 필요성이 있을 것 같아요.

### Not Too much Static Object

- Static Object들은 "전역변수"의 개념과 유사하고, Encapsulization이 되어 있지 않죠. 즉, 유효 범위(특정 변수가 유효한 범위)를 고려하지 않는, C와 같은 "절차지향적 프로그래밍"에서는 매우 유용할지도 모릅니다. 다만, Java는 객체지향 언어이며, 유효 범위가 존재하지 않는, Static을 함부로 사용할 경우, 예기치 못한 에러를 발생시킬 수 있다는 이야기죠. 
- 또한, Static Memory는 다른 메모리, 가령 Heap과 같은 메모리에 비해서 그 크기가 작습니다. 그리고 Static Memory는 JVM이 실행되면 종료될 때까지, 한번 할당된 메모리가 제거되지 않습니다. 물론, 이제는 PermGen이 없어져서 문제가 없는 것처럼 보이기는 한데요.
- 여타 다양한 이유로, 가능하면 Static 을 자주 사용하지 말라는 말이 있는데요, 자세한 내용은 [Stackoverflow - Why are static variables considered evil?](https://stackoverflow.com/questions/7026507/why-are-static-variables-considered-evil%22)를 보면 도움이 되실 겁니다. 이 안에는 좀 더 다양한 이슈들이 정리되어 있는데, 나머지 내용들은 추가로 다음에 더 정리하도록 하겠습니다.

---

## Stack Memory

- Stack Memory에는 Heap 영역에 저장되는 Object들의 데이터들의 "메모리 주소 값"이 저장됩니다. Class Instance를 만든다면, 이 Class Instance의 내부 field의 데이터는 Heap Memory에 저장되고, Class Instance의 주소는 Stack에 저장된다는 이야기죠.
- 또한, Class Instance가 아닌 Primitive type들(int, double 등) 또한, Stack에 저장됩니다. 그리고, 이미 아시겠지만, Primitive type의 경우는 메모리에 값을 그대로 저장하기 때문에, 주소를 저장하는 것이 아니라, stack에 메모리 값을 그대로 저장하게 되죠. 아래 그림으로 보면 이해가 빠를 수 있어요.

![stack_and_heap](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2458A349592E1C420F)

- 또한, Thread 별로 Stack은 구분되어 각각의 Thread를 가집니다. Heap의 경우는 Thread 구분 없이 공유되는 하나의 Heap이 존재하죠. 

---

## Heap Memory

- Heap 영역은 일반적으로 "동적 메모리 할당(Dynamic Memory Allocation)"되는 변수의 값들이 적재됩니다. 따라서 보통 Class Instance(객체)에 대한 데이터가 적재되죠.
- Heap 영역은 앞서 말한 것처럼, Dynamically Allocated되는 부분이므로, GC(Garbage Collector)에 의해 관리되며 특정 변수가 참조되지 않는다면 Heap 영역에서 메모리가 삭제됩니다.
- 다시, Heap은 "Young Generation", "Old Generation"으로 크게 구분되며, 세부적으로는 더 구분됩니다. 완벽하게 이해하려면 어렵고 간단하게 설명하자면 JVM은 Young Generation에 대해서는 Minor GC를 수행하고, Old Generation에 대해서는 Major GC를 수행하는데, Minor GC를 반복하는 동안 살아남은 Young Generation의 객체들은 Old Generation으로 옮겨 준다. 이렇게 쓰고 보니, 그냥 Genetic Algorithm처럼 GC를 해주는 걸로 보이기도 하네요.
- 각각을 개략적으로 설명하면 다음과 같습니다.
  - **Minor GC**: 만들어진지 얼마 안된 객체들의 메모리를 제거해줌으로써, 메모리 공간 확보
  - **Major GC**: 만들어진지 오래된(Minor GC에서 살아남은) 객체들의 메모리를 제거해줌으로써, 메모리 공간 확보. 물론, Major GC외에도 Full GC도 있지만, 이 글에서는 그 부분까지는 커버하지 않고 일단은 '같다'라고 생각하고 넘어가겠습니다.

![Heap_memory](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdOYH4N%2Fbtqwn8TENCZ%2F4A8uclI4KEyKYBbIdki9Tk%2Fimg.png)

--- 

## Wrap-up

- 가능하다면, 다른 언어들과 비교하여, 'python에서는 memory 관리를 방식 A로 하는데, Java에서는 방식 B로 하며 그로 인해 a, b, c 의 차이가 발생한다' 와 같은 부분까지 말했다면 좋았겠지만, 아무래도 능력 부족입니다.
- 그래도, Java에서 대략적으로 어떻게 memory를 구분하고 관리하는지에 대해서는 알게 된 것 같습니다.
- 다만 여전히 조금 더 공부를 하거나, 알아야할 것 같다고 느껴지는 부분들은 대략 다음과 같겠네요.
  - Stack이 변수를 할당하고 해제하는 방식을 예제와 함께 알아둘 것
  - Garbage Collection은 어떠한 방식으로 수행되는지.

---

## Reference

- [자바(JVM)의 메모리 사용 방식 (T 메모리 구조)](https://siyoon210.tistory.com/124)
- [Java 의 GC는 어떻게 동작하나?](https://mirinae312.github.io/develop/2018/06/04/jvm_gc.html)
- [Java PermGen의 역사](https://blog.voidmainvoid.net/315)
- [johngrib - java8 why permgen removed](https://johngrib.github.io/wiki/java8-why-permgen-removed/)
- [Yaboong - 자바 메모리 관리 - 가비지 컬렉션](https://yaboong.github.io/java/2018/06/09/java-garbage-collection/)
- [Yaboong - 자바 메모리 관리 - 스택 & 힙](https://yaboong.github.io/java/2018/05/26/java-memory-management/)
