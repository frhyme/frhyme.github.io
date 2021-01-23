---
title: scala - Collection
category: scala
tags: scala programming collection
---

## Scala - Collection 

- scala의 collection, Array, List, Set, Map에 대해서 간단하게 정리하였습니다.

```scala
// S
object HelloWorld {
  def main(args: Array[String]) {
    val arr1:Array[Int] = Array(2, 4, 6, 8);
    val lst1:List[Int] = List(1, 2, 3, 4)
    System.out.println(lst1.length); // 4
    System.out.println(arr1.length); // 4

    val set1:Set[Int] = Set(1, 2, 3, 5);
    System.out.println(set1.size); // 4
    System.out.println(set1.contains(4)); // false

    val map1:Map[Int, Char] = Map(1 -> 'A', 2 -> 'B');
    System.out.println(map1); // Map(1 -> A, 2 -> B)
    System.out.println(map1.keys); // Set(1, 2)
    System.out.println(map1.values); // Iterable(A, B)   
  }
}
```
