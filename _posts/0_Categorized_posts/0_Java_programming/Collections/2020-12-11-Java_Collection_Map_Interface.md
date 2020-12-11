---
title: Java - Map Interface
category: java
tags: java programming interface collection Map
---

## Java - Map

- Map은 `(key, value)`로 구성하는 자료구조입니다. python의 dictionary와 비슷하죠. Map Interface의 구현체로는, `HashMap`, `TreeMap`, `LinkedHashMap`이 있죠.
- `HashMap`의 경우 HashTable에 의해서 관리되기 때문에, `get`, `put` 메소드를 사용할 때, constant time이 사용됩니다.
- `LinkedHashMap`의 경우는 "들어온 순서"를 기억합니다. 그 순선에 맞게 값을 저장해두죠.
- `TreeMap`은 key의 기본 비교 우위에 맞춰서 기억해둡니다. 그냥 SortedDicationary라고 생각해도 된다는 이야기죠.

## Java - Map Implmentation

- 실제로 Java에서 Map을 사용해보겠습니다.

```java
// Map
// Map은 Key, Value로 값을 기억하므로 각각 어떤 Type이 되어야 하는지 선언해주어야 합니다.
Map<String, String> id_to_name = new HashMap<>();
// put(key, value): (key, value)를 넣어줍니다.
// get(key): key가 가진 value 값을 리턴합니다.
// getOrDefault(key, defaultValue): key가 map에 없으면 defaultValue를 리턴합니다.
id_to_name.put("id1", "v1");
id_to_name.put("id2", "v2");
id_to_name.put("id3", "v3");
System.out.println( id_to_name.get("id1") ); // "id1"
System.out.println( id_to_name.getOrDefault("id9", "null") ); // "null"
// boolean containKey(key): key가 Map에 있는지 확인
// boolean containValue(value): value가 Map에 있는지 확인
System.out.println( id_to_name.containsKey("id1") ); // true
System.out.println( id_to_name.containsKey("id9") ); // false
System.out.println( id_to_name.containsValue("v1") ); // true
System.out.println( id_to_name.containsValue("v9") ); // false
// Set<K> keySet(): Map의 Key Set를 리턴합니다.
// Collection<V> values(): Map의 Value Collection를 리턴합니다.
// Set는 중복이 안되고, Collection은 중복이 허용되죠.
for (String k: id_to_name.keySet()) {
System.out.printf("Key: %s, Value: %s\n", k, id_to_name.get(k));
}
// Map Equality
// Map은 key, value가 완벽하게 똑같아야 equality가 성립됩니다.
Map<String, String> map1 = new HashMap<>();
Map<String, String> map2 = new HashMap<>();
map1.put("1", "1");
map2.put("1", "1");
System.out.println( map1.equals(map2) ); // true
map2.put("1", "3");
System.out.println( map1.equals(map2) ); // false
map2.put("2", "2");
System.out.println( map1.equals(map2) ); // false
```
