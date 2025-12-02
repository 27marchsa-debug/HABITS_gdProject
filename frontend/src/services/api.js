import axios from 'axios';
import { Platform } from 'react-native';

// 분기 처리
const API_URL = Platform.select({
  ios: 'http://localhost:8000', // iOS 에뮬레이터 전용 주소
  android: 'http://10.0.2.2:8000', // 안드로이드 에뮬레이터 전용 주소
});

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
