from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    mbti_type = Column(String)  # 성격 유형 (예: "용감한 모험가")
    
    # 기획 핵심: 이상적 자아 해시태그 (예: ["#대담함", "#도전"])
    ideal_hashtags = Column(JSON) 
    
    # 기획 핵심: 사용자 스케줄 (예: {"commute": "08:00-09:00", "bedtime": "23:00"})
    schedule_context = Column(JSON)

    habits = relationship("Habit", back_populates="owner")

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # 예: "출근길 팟캐스트 듣기"
    category = Column(String)         # 'AUDIO', 'VISUAL', 'ACTIVITY' 등
    frequency = Column(String)        # "DAILY", "WEEKLY"
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="habits")
    logs = relationship("HabitLog", back_populates="habit")

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)
    
    # 기획 핵심: 감정 분석 결과 저장
    emotion_score = Column(JSON) # 예: {"sadness": 0.8, "joy": 0.1}
    diary_content = Column(String, nullable=True) # 사용자가 쓴 일기 내용
    ai_feedback = Column(String, nullable=True)   # LLM이 해준 피드백
    
    habit_id = Column(Integer, ForeignKey("habits.id"))
    habit = relationship("Habit", back_populates="logs")
