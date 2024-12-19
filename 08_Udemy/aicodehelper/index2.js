/*
본 코드는 Google Cloud의 TTS API를 사용하는데 있어서 구글클라우드 모듈을 이용해서 API를 사용하고 결과를 얻는 코드입니다

사용방법은 다음과 같습니다
1. 폴더를 만들고 본 코드를 index2.js라는 이름으로 담습니다 (다른이름이여도 괜찮습니다)
2. 터미널에서 해당 폴더로 cd명령어로 이동 후, npm init -y 라고 입력해서 실행해줍니다
3. 이어서 npm i @google-cloud/text-to-speech 를 입력해서 실행해줍니다
4. node index2.js 를 입력해서 본 소스코드를 실행합니다
5. 그러면 해당 폴더에 output.mp3 파일이 생겼는지 확인합니다. 본 파일은 '안녕하세요' 를 TTS로 읽어서 만든 음원입니다.
*/

const textToSpeech = require('@google-cloud/text-to-speech');
const fs = require('fs');
const client = new textToSpeech.TextToSpeechClient({
    keyFilename: './인증키파일.json' // 발급방법은 강의를 참고해주세요
});
async function tts(text) {
    const request = {
        input: { text: text },
        voice: { languageCode: 'ko-KR', name: `ko-KR-Wavenet-A`, ssmlGender: 'NEUTRAL' },
        audioConfig: { audioEncoding: 'MP3' },
    };
    const [response] = await client.synthesizeSpeech(request);
    const { audioContent } = response
    const buffer = Buffer.from(audioContent, 'base64');
    fs.writeFileSync('output.mp3', buffer);
}
tts('안녕하세요');
