---
title: Java - Logging - Logger
category: java
tags: java programming logging logger
---

## Java - Logging

- Logger는 일반적으로 시스템 상에서 발생하는 상황을 확인하기 위한 도구죠. 
- 사실 그냥 `System.out.println()`을 사용해서 처리하는 일이 많기는 한데, 이렇게 할 경우 나중에 한번에 해제한다거나 하는 일이 어려워집니다. 가령, 여러 함수에 `System.out.println()`이 분산되어 있다면 얘네를 일일이 확인해서 어디에서 오는건지 봐야하거든요.
- 따라서, 개발을 진행할수록 점차 logging을 사용하게 되는 일이 많죠.
- `java.util.logging` 패키지에는 보통 Logger, Handler, Filter, Formatter, output 등이 있습니다. 하나씩 알아볼거에요.

<div class="mermaid"> 
  graph LR; 
    Logger --> Handler;
    Logger --> Filter;
    Handler --> Filter;
    Handler --> Formatter;
    Handler --> Output;
</div>

## Logger 

- 가장 근-본이 되는 놈으로 말 그대로 발생하는 문제를 log(기록)해주는 놈이죠.
- 다음처럼 상황의 심각성과 message를 함께 기록하도록 할 수 있습니다.

```java
package com.company;

import java.util.logging.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // logger의 name을 등록합니다.
        Logger logger = Logger.getLogger("Main class");
        logger.log(Level.SEVERE, "Message ::" + logger.getName());
        logger.log(Level.WARNING, "Message ::" + logger.getName());
        logger.log(Level.INFO, "Message ::" + logger.getName());
        logger.log(Level.CONFIG, "Message ::" + logger.getName());
    }
}
```

- 위 코드를 실행해 보면, `CONFIG`에 해당하는 log는 표시되지 않는 것을 알 수 있습니다. default는 info죠.
- 이는 Logger에서 지정된 '위험 레벨'보다 높은 경우만 출력해주기 때문이죠.

```plaintext
2월 10, 2021 5:36:57 오후 com.company.Main main
SEVERE: Message ::Main class
2월 10, 2021 5:36:57 오후 com.company.Main main
WARNING: Message ::Main class
2월 10, 2021 5:36:57 오후 com.company.Main main
INFO: Message ::Main class
```

## Handler, Formatter 

- `Handler`는 결과를 console 창에 출력하게 할 것인지, File에 출력하도록 할 것인지를 정하는 놈이고. `Formatter`는 어떤 출력형식(XML 등)으로 출력할 것인지를 정해주는 놈을 말합니다.
- 따라서 보통 이 두놈은 같이 쓰일 때가 많죠.
- 코드는 다음과 같습니다.

```java
package com.company;

import java.util.logging.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // logger의 name을 등록합니다.
        Logger logger = Logger.getLogger("Main class");
        // FilerHandler를 만들고, 파일명인 "test.log"를 넘겨줍니다.
        Handler fileHandler = new FileHandler("test.log");
        // fileHandler의 format형식을 정해주기 위해서 XMLFormatter를 등록해줍니다.
        fileHandler.setFormatter(new XMLFormatter());
        // 그리고 logg에도 Handler를 등록해줍니다.
        logger.addHandler(fileHandler);

        // logging start
        logger.log(Level.SEVERE, "Message ::" + logger.getName());
        logger.log(Level.WARNING, "Message ::" + logger.getName());
        logger.log(Level.INFO, "Message ::" + logger.getName());
        logger.log(Level.CONFIG, "Message ::" + logger.getName());
    }
}
```

- 그리고, `test.log`를 열어 보면 다음과 같습니다.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE log SYSTEM "logger.dtd">
<log>
    <record>
        <date>2021-02-10T08:43:49.074499Z</date>
        <millis>1612946629074</millis>
        <nanos>499000</nanos>
        <sequence>0</sequence>
        <logger>Main class</logger>
        <level>SEVERE</level>
        <class>com.company.Main</class>
        <method>main</method>
        <thread>1</thread>
        <message>Message ::Main class</message>
    </record>
    <record>
        <date>2021-02-10T08:43:49.133306Z</date>
        <millis>1612946629133</millis>
        <nanos>306000</nanos>
        <sequence>1</sequence>
        <logger>Main class</logger>
        <level>WARNING</level>
        <class>com.company.Main</class>
        <method>main</method>
        <thread>1</thread>
        <message>Message ::Main class</message>
    </record>
    <record>
        <date>2021-02-10T08:43:49.134279Z</date>
        <millis>1612946629134</millis>
        <nanos>279000</nanos>
        <sequence>2</sequence>
        <logger>Main class</logger>
        <level>INFO</level>
        <class>com.company.Main</class>
        <method>main</method>
        <thread>1</thread>
        <message>Message ::Main class</message>
    </record>
</log>
```
