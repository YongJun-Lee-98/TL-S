/*
tts = text to speech
본 코드는 OpenAI의 Dall-E API를 이용해서 그림을 그리는 코드입니다.
직접 fetch로 API의 Endpoint로 접속해서 API를 사용하고 결과를 얻는 코드입니다

사용방법은 다음과 같습니다
1. 폴더를 만들고 본 코드를 index.js라는 이름으로 담습니다 (다른이름이여도 괜찮습니다)
2. 터미널에서 해당 폴더로 cd명령어로 이동 후, npm init -y es6 라고 입력해서 실행해줍니다
3. 이어서 npm i node-fetch 를 입력해서 실행해줍니다
4. node index.js 를 입력해서 본 소스코드를 실행합니다
5. 그러면 만들어진 이미지에 해당하는 URL을 담은 JSON을 출력합니다.
6. URL을 클립보드에 복사해서 웹브라우저에 복사해서 넣으면 이미지를 확인할 수 있습니다.
*/
import fetch from 'node-fetch';
for (let i = 0; i < 3; i++) {
  fetch("https://api.openai.com/v1/images/generations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer 여기에에이피아이키를담아주세요"
    },
    body: JSON.stringify({
      "prompt": "A cute baby sea otter",
      "n": 1,
      "size": "1024x1024"
    })
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response data here
      console.log(data);
    })
    .catch(error => {
      // Handle any errors here
      console.error(error);
    });
}