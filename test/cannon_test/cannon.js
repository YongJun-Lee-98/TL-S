const autocannon = require('autocannon');

let token = ''; // 로그인 후 받은 JWT 토큰을 저장할 변수

const instance = autocannon({
  url: 'https://moongcle.xyz', // 테스트할 서버 주소 (실제 주소로 변경)
  connections: 10, // 동시 연결 수 (필요에 따라 조절)
  duration: 10, // 테스트 지속 시간 (초) (필요에 따라 조절)
  requests: [
    {
      method: 'POST',
      path: '/login', // 로그인 API 엔드포인트 (실제 경로로 변경)
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id: 'TEST2', // 실제 ID 입력
        password: '5625' // 실제 비밀번호 입력
      }),
      onResponse: (status, body) => {
        console.log('로그인 응답:', status, body);
        if (status === 200) {
          // 로그인 성공 시 응답에서 토큰 추출 (실제 응답 형식에 맞게 수정)
          const responseData = JSON.parse(body);
          token = responseData.token || responseData.accessToken; // 토큰 필드 이름 확인 필요
          console.log('로그인 성공:', token);
        } else {
          // 로그인 실패 시 오류 처리
          console.error('로그인 실패:', status, body);
        }
      }
    },
    {
      method: 'GET',
      path: '/ItemManagement', // 로그인 후 접근 가능한 URL (실제 경로로 변경)
      headers: {
        'Authorization': `Bearer ${token}` // JWT 토큰 추가
      }
    },
    // {
    //   method: 'GET',
    //   path: '/ExamReport', // 로그인 후 접근 가능한 URL (실제 경로로 변경)
    //   headers: {
    //     'Authorization': `Bearer ${token}` // JWT 토큰 추가
    //   }
    // },
    // {
    //   method: 'GET',
    //   path: '/ClassManagement', // 로그인 후 접근 가능한 URL (실제 경로로 변경)
    //   headers: {
    //     'Authorization': `Bearer ${token}` // JWT 토큰 추가
    //   }
    // },
    // {
    //   method: 'GET',
    //   path: '/TestCreation', // 로그인 후 접근 가능한 URL (실제 경로로 변경)
    //   headers: {
    //     'Authorization': `Bearer ${token}` // JWT 토큰 추가
    //   }
    // },
    
    // ... 추가 URL에 대한 요청 설정 가능 (필요에 따라 추가)
  ]
}, (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
});