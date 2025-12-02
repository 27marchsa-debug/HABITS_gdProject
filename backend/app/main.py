from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user

# DB 테이블 자동 생성 (서버 시작 시)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HABITS API", description="AI Habit Coaching Backend")

# 헬스 체크용 (서버 살아있는지 확인)
@app.get("/")
def read_root():
    return {"message": "HABITS Server is Running! 🚀"}

# TODO: 여기에 @app.post("/diary") 등 API 라우터 추가 예정
