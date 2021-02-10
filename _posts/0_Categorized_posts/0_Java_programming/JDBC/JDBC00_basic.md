---
title: Java - JDBC
category: java
tags: java JDBC database sqlite
---

- 일단 `build.gradle`에 아래를 sqlite를 등록해줍니다.

```groovy
dependencies {
    // ...
    // 20210210 ADD sqlite
    compile group:'org.xerial', name:'sqlite-jdbc', version:'3.30.1'
}
```