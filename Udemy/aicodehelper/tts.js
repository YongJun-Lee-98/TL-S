
const textToSpeech = require('@google-cloud/text-to-speech');
const fs = require('fs');
const path = require('path');

const client = new textToSpeech.TextToSpeechClient({
    keyFilename: './aimovie-394513-482c61930bdf.json'
});

async function synthesizeSpeech(text, languageCode, voiceName, audioEncoding, filename) {
    const request = {
        input: { text },
        voice: { languageCode, name: voiceName, ssmlGender: 'MALE' },
        audioConfig: { audioEncoding, effectsProfileId: ['telephony-class-application'], pitch: -2.0, speakingRate: 1.5, naturalSampleRateHertz: 10000 },
    };

    try {
        const [response] = await client.synthesizeSpeech(request);
        const filepath = path.join(__dirname, `${filename}.mp3`);
        fs.writeFileSync(filepath, response.audioContent, 'binary');
        console.log('음성 파일이 성공적으로 저장되었습니다.');
        console.log('파일 경로:', filepath);
        return filepath;
    } catch (err) {
        console.error('TTS 요청 중 오류가 발생했습니다:', err);
        throw err; 
    }
}

(async () => {
    try {
        const filepath = await synthesizeSpeech('안녕하세요. 반갑습니다. 한국인은 게임을 잘합니다.', 'ko-KR', 'ko-KR-Wavenet-A', 'MP3', 'voice2');
        console.log('filepath:', filepath);
    } catch (err) {
        console.error('함수 실행 중 오류가 발생했습니다:', err);
    }
})();