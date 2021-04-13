---
title: Google Apps Script - Gmail - Send Mail
category: google
tags: google javascript macro GoogleAppsScript Gmail
---

## Google Apps Script - Gmail - Send Mail

- Google Apps Script에서 Gmail API를 사용하여 메일을 보내는 코드를 정리하였습니다.

```js
function send_mail_to_me() {
  var email = "aaa@gmail.com"
  var subject = "subject"
  var body = "body"

  GmailApp.sendEmail(email, subject, body);
}
```

- 코드를 실행하니까 저한테 메일이 뚝 와 있네요 호호호.

## Wrap-up

- 여러 명에게 조금씩 다른 내용으로 메일을 보내야 하는 경우, 과거에는 Outlook을 사용했었는데요. 이제 Google Apps Script를 사용해서 처리하면 될것 같습니다.
- 또한, 트리거를 통해 다양한 이벤트 상황에서 스스로에게 알람을 전달해줄 수 있는 형태로 코드를 짜면 좋을 것 같습니다 하하.
