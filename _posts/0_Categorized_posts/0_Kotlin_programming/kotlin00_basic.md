
## Install extension for syntax highting for VScode

- ddd

## Varaible - val, var

- `val`: immutable variable, Constatn
- `var`: mutable variable

```kotlin
// 다음처럼, type을 지정할 수 있으며, 
// 타입을 지정할 경우 값을 지정하지 않고도 변수를 선언할 수 있음.
var x:Int
x = 10
```

## Char and String

- 'a': char
- "a": string

## convention

- 4 space indentation instead of tab

### Comment

```kotlin
// one line comment
/*
multi line comment
*/
/**
 * The `main` function accepts string arguments from outside.
 * @param args arguments from the command line.
 * @return
 */
fun main(args: Array<String>) {
    // do nothing
}
```