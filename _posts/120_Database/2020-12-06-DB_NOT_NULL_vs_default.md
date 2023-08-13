---
title: DB) NOT NULL과 DEFAULT를 동시에 쓸 필요가 있는가?
category: others
tags: database constraint NULL
---

## DB constraint에서 NOT NULL과 DEFAULT를 동시에 쓸 필요가 있나요?

- `name` 칼럼만 있는 테이블을 다음과 같이 만들었습니다. 그리고 다음의 두 가지 Constraint을 설정해줬죠.
  - `NOT NULL`: 해당 칼럼이 NULL 값이 되면 안된다.
  - `DEFAULT "person"`: explicit하게 값이 입력되지 않으면 `"person"`을 값으로 정해준다.

```SQL
CREATE TABLE simple_table (
    name VARCHAR(30) NOT NULL DEFAULT "person"
); 
```

- 이제 우리는 테이블에 값을 입력할 때 발생할지도 모르는 실수들을 조금은 방지할 수 있게 되었습니다. 
- 그럼 이제 값을 직접 넣어보도록 하죠. Query를 다음과 같이 작성했다고 해봅시다. 그 결과는 어떻게 되어야 할까요?

```SQL
INSERT INTO simple_table (name) VALUES ();
```

- 이 쿼리에서 우리는 아무 값도 넣어주지 않았습니다. 그럼 NULL 값을 넣어준게 아닐까요? 만약 그렇다면 NOT NULL CONSTRAINT에 의해서 오류가 발생해야 하는걸까요? 그런데 동시에 우리는 값이 정해지지 않은 경우에 대해서 DEFAULT VALUE가 정해지도록 처리하였습니다. 만약 아무 값도 정해지지 않는다면 자동으로 "person"이 들어가야하는게 아닐까요?

## If we don't have NOT NULL

- `NOT NULL`과 `default`의 역할을 서로 다른데, 어떻게 다른지 확실하게 알 기 위해서는 `NOT NULL` Constraint가 없다고 생각하고 쿼리를 돌려 보겠습니다. 쿼리는 다음과 같죠. 
- 우리는 "어차피 DEFAULT가 NULL값이면 알아서 'person'으로 바꿔주겠지?"라고 생각하고 있다고 할게요.

```SQL
CREATE TABLE simple_table (
    name VARCHAR(30) DEFAULT "person"
); 
```

- 그리고 다음의 INSERTION 쿼리문을 실행한다고 해보겠습니다. 어떤 일이 발생할까요?
- Query 1의 경우 null 값을 explicitly 넣어주었죠. 따라서, NULL인 값을 입력받았다고 생각하기 때문에, 아무 일도 일어나지 않습니다. 이를 막아주려면 `NOT NULL` constraintRk dlTdjdi gkwy.
- Query 2의 경우, 아무 것도 입력받지 않았죠. `DEFAULT`는 이 때 작동하게 되죠.

```SQL
/* QUERY 1 */
INSERT INTO simple_table (name) VALUES (NULL)
/* QUERY 2 */
INSERT INTO simple_table (name) VALUES ()
```

## Wrap-up

- 즉, `NOT NULL`과 `DEFAULT` constraint는 서로 중복되는 것이 아닙니다.
- **NOT NULL만 있는 경우**: NULL을 직접 입력하든, 아무 것도 입력하지 않아서 NULL 값이 넘어가든 두 경우에 대해서 모두 오류를 생성한다.
- **DEFAULT만 있는 경우**: 사용자가 값을 입력하지 않는 경우에 알아서 해당 칼럼에 값을 부여한다. 만약 사용자가 NULL을 입력한다고 해도, 값을 입력한 것으로 보기 때문에, DEFAULT는 활성화되지 않는다.
- **NOT NULL, DEFAULT 모두 있는 경우**: 둘다 있는 경우에는 사용자가 값을 입력하지 않는 경우에는 알아서 DEFAULT가 활성화되고, NULL을 입력하는 경우 NOT NULL이 활성화되어 오류가 발생하게 됩니다. 

## Reference

- [Stakcoverflow - SQL column definition default value and not null redundant](https://stackoverflow.com/questions/11862188/sql-column-definition-default-value-and-not-null-redundant)
