from fastapi import FastAPI
from model import TravelRequest

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Travel recommendation API"}

@app.post("/recommend")
def recommend(data: TravelRequest):
    if data.location == "국내":
        if data.purpose == "휴식":
            destination = "제주도"
        elif data.purpose == "관광":
            destination = "경주"
        elif data.purpose == "맛집":
            destination = "전주"
        else:
            destination = "부산"
    else:
        if data.purpose == "휴식":
            destination = "괌"
        elif data.purpose == "관광":
            destination = "일본 도쿄"
        elif data.purpose == "맛집":
            destination = "일본 오사카"
        else:
            destination = "프랑스 파리"

    return {
        "recommended_destination": destination,
        "reason": f"{data.location} 여행 중 {data.purpose} 목적에 어울리는 여행지입니다.",
        "style": data.style,
        "duration": data.duration
    }
