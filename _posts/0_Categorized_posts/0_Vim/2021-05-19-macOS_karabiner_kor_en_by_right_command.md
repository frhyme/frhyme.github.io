---
title: macOS - 카라비너를 사용하여, 오른쪽 커맨드로 한영전환하기 
category: macOS
tags: macOS karabiner
---

## macOS - 카라비너를 사용하여, 오른쪽 커맨드로 한영전환하기 

- 맥북에서는 기본적으로 한영전환을 `ctrl + space` 혹은 `caps lock`을 사용해서 합니다. 저는 두 키 를 사용해서 한영전환을 하는 것 보다는, 키 하나를 사용하는 것이 더 효율적이기 때문에, 캡츠락을 사용해서 한영전환을 해줍니다.
- 그동안은 맥북 키보드를 그대로 사용했기 때문에, 문제가 없었습니다. 하지만 최근에 해피해킹 키보드를 사용하면서부터는 문제가 발생합니다. 우선, 해피해킹 키보드에는 캡츠락 키보드 자리에 control 키가 와 있기 때문이죠. 그리고 해피해킹 키보드에서 컨트롤 키는 단 하나 있습니다. 따라서, 해피해킹에서의 컨트롤 키를 한영 전환으로 변환하는 것을 불가능합니다.
- 따라서, 저는 [karabiner - elements](https://karabiner-elements.pqrs.org/)를 사용해보기로 합니다.

## 카라비너?

- [karabiner - elements](https://karabiner-elements.pqrs.org/)는 키 맵핑 도구라고 생각하시면 됩니다. 가령 맥OS에서 키를 가상으로 매핑하고 싶을 때 사용하는 도구죠. 아마도 맥북에서 캡츠락 자체를 아예 한영 전환 전용 키로 사용하고 싶을 때(대소문자 변환을 하지 않고)에도 유용하게 사용할 수 있죠.
- 일단 카라비너를 설치해주고, "Complex modification"에 들어갑니다. 
- 그리고, "Add Rule"을 눌러줍니다.
- 그 다음 "Import more rule from the internet(open a web browser)"를 눌러줍니다.
- 그럼 웹 브라우저가 뜨는데요, 거기서 "Change input-source directly for korean"를 검색해 주고 import 해 줍니다. 이렇게 하면 외부에서 해당 키 매핑에 대한 정보를 로컬로 가져오는 것을 말하죠.

### 좀 더 자세히 설명 해 보면

- 이 작업을 자세히 설명해 보겠습니다.
- 아쉽게도 카라비너 앱을 사용해서 직접 제가 원하는 방식으로 키 맵핑을 하는 것은 어렵구요, 남들이 정의해 놓은 방식을 가져와서 사용할 수만 있습니다.
- 아무튼, 그럼 가져온 내용이 어디에 저장되느냐? 다음 경로에 저장됩니다. 

```plaintext
~/.config/karabiner
```

- 해당 경로에 들어가서 `karabiner.json` 문서를 열어 보면 대략 다음과 같이 구성되어 있습니다. 만약, 아직 어떤 complex modification rule도 가져오지 않았다면요. 
- 아래 부분에서 profiles > complex_modifications > rules 에 import된 complex modification rule이 저장됩니다.
- 즉, 카라비너는 키 맵핑에 대한 정보를 json을 사용해서 관리한다는 이야기죠.

```json
{
    "global": {
        "check_for_updates_on_startup": true,
        "show_in_menu_bar": true,
        "show_profile_name_in_menu_bar": false
    },
    "profiles": [
        {
            "complex_modifications": {
                "parameters": {
                },
                "rules": [
                ]
            },
            "devices": [
            ],
            "fn_function_keys": [
            ],
            "name": "Default profile",
            "parameters": {
                "delay_milliseconds_before_open_device": 1000
            },
            "selected": true,
            "simple_modifications": [],
            "virtual_hid_keyboard": {
            } 
        }
    ]
}
```

- 앞서 말한 대로 "Change input-source directly for korean"를 가져온 상태라면 profiles > complex_modifications > rule 부분이 아래와 같이 변경됩니다.
- 자세히 읽어보면 **"아 대강 이런 방식으로 정의하는 구나"**라는 느낌이 오기는 합니다. 그냥 `condition`에 키 맵핑이 발동될 수 있는 조건을 정의하고, `from`에는 눌려지는 키, `to`에는 `from`에 정의된 키가 눌렸을 때, 실행되는 키 등을 정의해야 하는 것이죠. 

```json
"rules": [
    {
        "description": "Right_command to korean <-> english",
        "manipulators": [
            {
                "conditions": [
                    {
                        "input_sources": [
                            {
                                "input_source_id": "^com\\.apple\\.keylayout\\.ABC$"
                            }
                        ],
                        "type": "input_source_if"
                    }
                ],
                "from": {
                    "key_code": "right_command",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "select_input_source": {
                            "input_source_id": "^com\\.apple\\.inputmethod\\.Korean\\.2SetKorean$"
                        }
                    }
                ],
                "type": "basic"
            },
            {
                "conditions": [
                    {
                        "input_sources": [
                            {
                                "input_source_id": "^com\\.apple\\.inputmethod\\.Korean\\.2SetKorean$"
                            }
                        ],
                        "type": "input_source_if"
                    }
                ],
                "from": {
                    "key_code": "right_command",
                    "modifiers": {
                        "optional": [
                            "any"
                        ]
                    }
                },
                "to": [
                    {
                        "select_input_source": {
                            "input_source_id": "^com\\.apple\\.keylayout\\.ABC$"
                        }
                    }
                ],
                "type": "basic"
            }
        ]
    }
]                
```

## wrap-up 

- 일단은 그냥 간단하게 알아봤습니다만, 기정의되어 있는 것을 가져오는 것 뿐만 아니라 `karabiner.json`에 직접 문법에 맞춰서 정의하여 다양한 키맵핑을 사용할 수 있을 것 같습니다.
- 저의 이상적인 목표는 ctrl 이 단독으로 눌렸을 경우 한영전환이 적용되도록 하고 싶어요. 어설프게나마 정의해봤는데, 한영전환은 되는데 `ctrl + a`와 같은 복합 키가 적용되지 않더라고요.
- 다음에 좀 더 공부해서 만들 수 있으면 다시 글을 포스팅 해보도록 하겠씁니다.
