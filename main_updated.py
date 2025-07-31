from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import random
from database import db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_clothing_data():
    """PostgreSQL에서 의류 데이터를 가져옵니다"""
    try:
        # 데이터베이스에서 데이터 조회
        df = db.get_products_data()
        
        # 이미지 URL 처리 (필요한 경우)
        if "대표이미지URL" in df.columns:
            # URL이 "//"로 시작하는 경우 "https:" 추가
            df.loc[df["대표이미지URL"].str.startswith("//"), "대표이미지URL"] = "https:" + df["대표이미지URL"]
        
        # 데이터프레임을 딕셔너리 리스트로 변환
        return df.to_dict("records")
    
    except Exception as e:
        print(f"데이터베이스에서 데이터를 가져오는 중 오류 발생: {e}")
        return []

@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    # PostgreSQL에서 데이터 가져오기
    clothing_data = get_clothing_data()
    
    if not clothing_data:
        # 데이터베이스 연결에 실패한 경우 빈 데이터로 처리
        return templates.TemplateResponse(
            "home.html", 
            {
                "request": request,
                "section1_items": [],
                "section2_items": [],
                "section3_items": [],
                "section4_items": [],
                "error_message": "데이터베이스에서 데이터를 가져올 수 없습니다."
            }
        )
    
    # 데이터셋에서 100개의 아이템을 무작위로 선택
    if len(clothing_data) > 100:
        sampled_data = random.sample(clothing_data, 100)
    else:
        sampled_data = clothing_data

    # 데이터를 4개의 섹션으로 나눕니다.
    section1_data = sampled_data[0:25] if len(sampled_data) > 0 else []
    section2_data = sampled_data[25:50] if len(sampled_data) > 25 else []
    section3_data = sampled_data[50:75] if len(sampled_data) > 50 else []
    section4_data = sampled_data[75:100] if len(sampled_data) > 75 else []

    return templates.TemplateResponse(
        "home.html", 
        {
            "request": request,
            "section1_items": section1_data,
            "section2_items": section2_data,
            "section3_items": section3_data,
            "section4_items": section4_data
        }
    )