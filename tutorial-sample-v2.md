## API 사용 방법

요청 데이터는 아래와 같은 형식으로 구성되어야 합니다.

*   **<span style="color:#3498db">{source-style}</span>|<span style="color:#3498db">{target-style}</span>|<span style="color:#3498db">{source-sentence}</span>**

    *   **source-style**: 전달할&nbsp;텍스트의 스타일 원형 (표준어/충청도/강원도/전라도/경상도/제주도 중 택 1)
    *   **target-style**: 변환하고자 하는 스타일 유형&nbsp;(표준어/충청도/강원도/전라도/경상도/제주도 중 택 1)
    *   **source-sentence**: 변환하고자 하는 텍스트 문장 (1~512 자)
*  예시

    *   <span style="font-size:14px"><span style="color:#4e5f70">표준어|충청도|안녕하세요?</span></span>
    *   <span style="font-size:14px"><span style="color:#4e5f70">표준어|경상도|요즘 날씨가 너무 추워서 어떤 옷을 입을지 고민이 많아진 것 같아요. 어떤 옷이 좋을지 추천해줄 수 있어요?</span></span>


## Sample

### Request

*   curl 명령어

```bash
curl -k --header 'x-client-key: {client-key}'--header 'x-client-signature: {signature}'--header 'x-auth-timestamp: {timestamp}' 
--header 'Content-Type: application/json'--header 'charset: utf-8' -d '{"data" : "표준어|충청도|안녕하세요?"}'https://aiapi.genielabs.ai/kt/nlp/dialect
```


*   python
```python
import json
import requests
url = "https://aiapi.genielabs.ai/kt/nlp/dialect"
headers = {
     "x-client-key":"f{client-key}",
     "x-client-signature":"f{signature}",
     "x-auth-timestamp": "f{timestamp}",
     "Content-Type": "application/json",
     "charset": "utf-8",
 } 
body = json.dumps({"data" : "표준어|충청도|안녕하세요?"}) 
response = requests.post(url, data=body, headers=headers, verify=False)
if response.status_code == 200:
    try:
        print(response.json())
    except json.decoder.JSONDecodeError:
        print(f'json.decoder.JSONDecodeError occured.\nresponse.text: "{response.text}"')
else:
    print(f"response.status_code: {response.status_code}\nresponse.text: {response.text}")
```

### Response

```bash
{
  "code": 200,
  "message": "Success",
  "text": "안녕하세요?",
  "prediction": "안녕하세유",
  "input_token_count": 5,
  "completion_token_count": 5,
  "total_token_count": 10
}
```

*Request Header 값은&nbsp;<u>[<span style="color:#3498db">GenieLabs AI API 인증 방법</span>](https://github.com/ktgenielabs/guide/wiki/AI-API-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)</u>을&nbsp;참고하세요.
