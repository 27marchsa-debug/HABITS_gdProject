import axios from 'axios';

// 안드로이드 에뮬레이터에서는 localhost 대신 10.0.2.2를 씁니다.
// 실기기 테스트 시에는 내 PC의 IP 주소를 넣으세요 (예: http://192.168.0.5:8000)
const API_URL = 'http://10.0.2.2:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 예시: 일기 데이터 서버로 전송하기
export const submitDiary = async (userId, content, emotion) => {
  try {
    const response = await api.post('/logs', {
      user_id: userId,
      content: content,
      emotion_tag: emotion
    });
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};

export default api;
