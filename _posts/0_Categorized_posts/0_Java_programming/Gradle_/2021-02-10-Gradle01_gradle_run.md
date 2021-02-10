---
title: Gradle - Basic 
category: others
tags: build gradle java maven programming
---

## Gradle - basic

- [spring initializer](https://start.spring.io/)에서 config을 설정하고 다운받습니다. 
- 압축을 풀고 나서 해당 경로에서 다음 명령어를 실행해 주면 해당 경로에 필요한 plungin을 모두 설치해주고 build를 해줍니다.
- intelliJ의 경우는 그냥 해당 프로젝트의 폴더를 열면 알아서 다 처리해줍니다.

```plaintext
gradle build
```

- 폴더 내 `build.gradle` 파일을 확인해 보면, 대량 뭔지 보입니다.

```groovy
plugins {
    id 'org.springframework.boot' version '2.4.2'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'
    id 'java'
}

group = 'com.example'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

test {
    useJUnitPlatform()
}
```

- 아무튼 그냥 `gradle tasks --all`을 사용하면, 다음처럼 사용가능한 command들을 알 수 있습니다.

```plaintext
$ gradle tasks --all

> Task :tasks

------------------------------------------------------------
Tasks runnable from root project
------------------------------------------------------------

Application tasks
-----------------
bootRun - Runs this project as a Spring Boot application.

Build tasks
-----------
assemble - Assembles the outputs of this project.
bootBuildImage - Builds an OCI image of the application using the output of the bootJar task
bootJar - Assembles an executable jar archive containing the main classes and their dependencies.
bootJarMainClassName - Resolves the name of the application's main class for the bootJar task.
bootRunMainClassName - Resolves the name of the application's main class for the bootRun task.
build - Assembles and tests this project.
buildDependents - Assembles and tests this project and all projects that depend on it.
buildNeeded - Assembles and tests this project and all projects it depends on.
classes - Assembles main classes.
clean - Deletes the build directory.
jar - Assembles a jar archive containing the main classes.
testClasses - Assembles test classes.

Build Setup tasks
-----------------
init - Initializes a new Gradle build.
wrapper - Generates Gradle wrapper files.

Documentation tasks
-------------------
javadoc - Generates Javadoc API documentation for the main source code.

Help tasks
----------
buildEnvironment - Displays all buildscript dependencies declared in root project 'demo'.
components - Displays the components produced by root project 'demo'. [incubating]
dependencies - Displays all dependencies declared in root project 'demo'.
dependencyInsight - Displays the insight into a specific dependency in root project 'demo'.
dependencyManagement - Displays the dependency management declared in root project 'demo'.
dependentComponents - Displays the dependent components of components in root project 'demo'. [incubating]
help - Displays a help message.
model - Displays the configuration model of root project 'demo'. [incubating]
outgoingVariants - Displays the outgoing variants of root project 'demo'.
projects - Displays the sub-projects of root project 'demo'.
properties - Displays the properties of root project 'demo'.
tasks - Displays the tasks runnable from root project 'demo'.

Verification tasks
------------------
check - Runs all checks.
test - Runs the unit tests.

Other tasks
-----------
compileJava - Compiles main Java source.
compileTestJava - Compiles test Java source.
prepareKotlinBuildScriptModel
processResources - Processes main resources.
processTestResources - Processes test resources.
```

- `gradle bootrun`을 사용해보면 다음처럼 Application이 돌아가는 것을 알 수 있죠 호호.

```plaintext
$ gradle bootrun

> Task :bootRun

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v2.4.2)

2021-02-10 20:59:51.912  INFO 94004 --- [           main] com.example.demo.DemoApplication         : Starting DemoApplication using Java 15.0.1 on seunghoonui-MacBookAir.local with PID 94004 (/Users/seunghoonlee/JavaProject_Gradle/Proj1/build/classes/java/main started by seunghoonlee in /Users/seunghoonlee/JavaProject_Gradle/Proj1)
2021-02-10 20:59:51.914  INFO 94004 --- [           main] com.example.demo.DemoApplication         : No active profile set, falling back to default profiles: default
2021-02-10 20:59:52.307  INFO 94004 --- [           main] com.example.demo.DemoApplication         : Started DemoApplication in 0.747 seconds (JVM running for 1.071)
== frhyme

BUILD SUCCESSFUL in 1s
4 actionable tasks: 2 executed, 2 up-to-date
```
