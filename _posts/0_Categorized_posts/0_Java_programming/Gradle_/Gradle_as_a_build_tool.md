---
title: Gradle - Build Tool
category: others
tags: build gradle java maven programming
---

## Build Tool

- 일반적으로 build tool은 "소스코드들을 실행가능한 어플리케이션으로 자동으로 변환해주는 도구"라고 생각하시면 됩니다. 원래의 소스 코드들을 모두 텍스트로 되어 있는데, 이를 컴파일하고, 다른 코드들에 흩어져 있는 패키지들과 연결하여 하나의 완성된 프로그램으로 변환하는 것이죠.
- 혼자 프로그래밍을 할 때는 굳이 build tool을 사용해야 할 필요성을 별로 느끼지 못합니다. 일단 build하는데 걸리는 시간 자체도 작으니까 그냥 하면 되니까요. 하지만, 프로젝트의 규모가 커지고, 여러 라이브러리들을 사용하게 되고(따라서 버전이 달라진다거나 하는 일이 발생할 수 있고) 여러 이유로 빌드 툴을 사용해서 이를 효과적으로 관리해야 할 필요성들이 생기죠. 

### Build Tool이 하는 일

- 프로젝트가 여러 라이브러리들과 연결되어 있는 경우에, 해당 버전에 해당하는 라이브러리를 다운받고, 해당 라이브러리가 참조하는 다른 라이브러리들과 버전도 함께 다운 받아 줍니다.
- Build Tool이 compiler를 통해 프로젝트 내의 모든 소스 코드를 bytecode로 변환(Compile)해줍니다. 
- 컴파일된 code를 `JAR`, `APK`와 같은 어플리케이션 으로 패키지화해줍니다.
- 정상적인 어플리케이션이라면 통과해야 하는 Test들을 실행하고 해당 어플리케이션이 통과하는지를 확인해줍니다. 만약 테스트 과정에서 bug가 발생한다면, 프로그래머에게 알려주고, 고치도록 하죠.

### Java의 Build Tool

- Java에는 1) Apache Ant를 사용해서 build하고 Apache Ivy를 사용하여 의존성을 관리하거나 2) Apache Maven을 사용해서 서버 쪽에서 의존성을 관리하고, build하거나, 3) 안드로인드 어플리케이션에서 표준적으로 사용하는 툴인 Gradle을 사용하거나 하는 방법들이 있습니다.

--- 

## Gradle - Build Tool for JVM-based language

- Gradle은 JVM 기반의 언어들인 Java, Kotlin, Scala로 작성되는 프로젝트들을 관리하고 빌드해주는 자동화도구입니다. Ant, Ivy, Maven들도 있지만, 최근에는 안드로이드 쪽에서 Gradle을 표준으로 사용하기 때문에 최근에 아주 많이 사용되고 있죠.
- 프로젝트에서 사용하는 많은 라이브러리들의 버전과 라이브러리들간의 의존관계를 효과적으로 관리해줄 뿐 아니라, 다양한 플러그인들을 가지고 있어서 필요한 기능을 이어 붙여서 확장할 수 있도록 해주죠. 
- 또한, Groovy 기반의 DSL(Domain-Specific Language)를 작성하여 빌드 스크립트를 작성할 수 있도록 해줍니다.

### Install Gradle

- Gradle을 설치해보겠습니다.
- 저는 맥 유저이고 `brew`를 사용해서 설치하려고 합니다. [brew는 다음 명령어를 통해 설치할 수 있습니다](https://brew.sh/index_ko).

```plaintext
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

- 그 다음에는 brew를 통해서 gradle을 설치합니다.

```plaintext
brew install gradle
```

- 그리고 설치된 gradle의 버전을 확인해 봅니다. 저는 6.7.1 버전을 설치했습니다.

```plaintext
gradle -v
```

```plaintext
------------------------------------------------------------
Gradle 6.7.1
------------------------------------------------------------
```

### Spring Boot로 개발환경 설정

- Gradle
- [Spring Initializer](https://start.spring.io/)에서 Gradle Project를 설정하여 다운받습니다.

```plaintext
gradlew build
```

- 아래와 같이 우리가 설정한 것에 맞춰서 Build되죠.

```plaintext
(base) seunghoonlee@seunghoonui-MacBookAir demo % ./gradlew build
Downloading https://services.gradle.org/distributions/gradle-6.6.1-bin.zip
.........10%..........20%..........30%..........40%.........50%..........60%..........70%..........80%..........90%.........100%

Welcome to Gradle 6.6.1!

Here are the highlights of this release:
 - Experimental build configuration caching
 - Built-in conventions for handling credentials
 - Java compilation supports --release flag

For more details see https://docs.gradle.org/6.6.1/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)

BUILD SUCCESSFUL in 1m 9s
6 actionable tasks: 6 executed
```

- 그럼 내부에 `build` 라는 폴더가 생기죠. 여기서 아래 명령어를 통해 Spring 프로그램을 실행합니다.

```plaintext
java -jar build/libs/*.jar
```

```plaintext
(base) seunghoonlee@seunghoonui-MacBookAir demo % 

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v2.4.0)

2020-11-22 21:35:49.431  INFO 16640 --- [           main] com.example.demo.DemoApplication         : Starting DemoApplication using Java 15 on seunghoonui-MacBookAir.local with PID 16640 (/Users/seunghoonlee/demo/build/libs/demo-0.0.1-SNAPSHOT.jar started by seunghoonlee in /Users/seunghoonlee/demo)
2020-11-22 21:35:49.433  INFO 16640 --- [           main] com.example.demo.DemoApplication         : No active profile set, falling back to default profiles: default
2020-11-22 21:35:49.945  INFO 16640 --- [           main] com.example.demo.DemoApplication         : Started DemoApplication in 0.959 seconds (JVM running for 1.463)
```