# backend/app/core/config.py

class Settings:
    PROJECT_NAME: str = "HABITS API"
    
    # 1. DB 주소
    # DATABASE_URL = "postgresql://user:password@localhost/habits_db" 
    DATABASE_URL = "sqlite:///./habits.db"

    # 2. API 키들 (여기에 실제 키를 입력해서 올릴 예정)
    OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxxxxxxxxx" 
    HF_API_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxx"
    
    # 3. 기타 설정
    SECRET_KEY = "grading-test-secret-key"
    ALGORITHM = "HS256"

settings = Settings()
