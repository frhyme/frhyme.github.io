---
title: Gradle - build.gradle 살펴보기
category: others
tags: build gradle java maven programming
---

## Gradle - build.gradle 살펴보기

- `build.gradle` 파일을 매우 간단하게 설명합니다.

```groovy
// plugin이 작성됩니다.
plugins {
    id 'org.springframework.boot' version '2.4.2'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'
    id 'java'
}

/*
- gradle에서 정의하는 다른 라이브러리들을 어디에서 가져올지 작성하게 되고요.
- 기본적으로는 다음 4가지들이 있습니다.
    - mavenCentral()
    - jcenter()
    - mavenLocal()
    - google()
*/
repositories {
    mavenCentral()
}

// 의존관계들을 설정합니다.
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```
