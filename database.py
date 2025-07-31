import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import os
from typing import Optional

class DatabaseConnection:
    def __init__(self):
        # 환경변수에서 데이터베이스 설정을 가져옵니다
        self.db_config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432'),
            'database': os.getenv('DB_NAME', 'your_database_name'),
            'user': os.getenv('DB_USER', 'your_username'),
            'password': os.getenv('DB_PASSWORD', 'your_password')
        }
        
    def get_connection_string(self):
        """SQLAlchemy 연결 문자열을 생성합니다"""
        return f"postgresql://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}"
    
    def get_engine(self):
        """SQLAlchemy 엔진을 생성합니다"""
        return create_engine(self.get_connection_string())
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """SQL 쿼리를 실행하고 pandas DataFrame으로 반환합니다"""
        try:
            engine = self.get_engine()
            df = pd.read_sql_query(query, engine)
            return df
        except Exception as e:
            print(f"데이터베이스 쿼리 실행 중 오류 발생: {e}")
            return pd.DataFrame()
    
    def get_products_data(self, limit: Optional[int] = None) -> pd.DataFrame:
        """제품 데이터를 조회합니다"""
        # 여기서 테이블명과 컬럼명을 실제 데이터베이스에 맞게 수정하세요
        query = """
        SELECT 
            product_id,
            product_name,
            price,
            image_url as "대표이미지URL",
            category,
            description
        FROM products
        """
        
        if limit:
            query += f" LIMIT {limit}"
            
        return self.execute_query(query)

# 전역 데이터베이스 연결 인스턴스
db = DatabaseConnection()