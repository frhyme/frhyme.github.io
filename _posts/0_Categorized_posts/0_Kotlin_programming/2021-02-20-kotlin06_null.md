
- kotlin에서는 기본적으로는 변수에 `null`을 넣어줄 수 없습니다. 만약 null이 가능하도록 하려면 자료형 뒤에 `?`를 붙이면 됩니다.

```kotlin
var nullable:Int? = null;
println(nullable) // null
println(10) // 10
```