# 02-Parameter

클라이언트(프론트엔드)로부터 변수를 전송받는 방법

| 전송 방법 | 의미 | 동작 | 관련 SQL | HTML 전송 가능 여부 |
| ---- | --- | --- | --- | --- |
| GET | URL에 `?`이후 `key=value`&`key=value` 형식으로 전송. | READ | SELECT | O |
| POST | HTTP Header에 데이터를 포함시켜 전송 | CREATE | INSERT | O |
| PUT | HTTP Header에 데이터를 포함시켜 전송 | UPDATE | UPDATE | X |
| DELETE | HTTP Header에 데이터를 포함시켜 전송 | DELETE | DELETE | X |

