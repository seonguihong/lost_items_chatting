import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수에서 값 가져오기
def get_env_var(key: str, default: str = None):
    """환경변수 값을 가져옵니다"""
    return os.getenv(key, default)