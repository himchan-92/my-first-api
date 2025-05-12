from fastapi import FastAPI, Request
import json

app = FastAPI()

# 시스템 JSON 불러오기
with open("config/루피니티_시스템.json", "r", encoding="utf-8") as f:
    루피니티 = json.load(f)

@app.get("/")
def root():
    return {"message": "루피티니 서버 정상 작동 중!"}

@app.post("/dispatch-command")
async def dispatch_command(request: Request):
    data = await request.json()
    message = data.get("message", "").lower()

    if "인포그래픽" in message or "디자인" in message:
        return {"mode": "디온", "action": "디자인 생성"}
    elif "기획" in message or "아이디어" in message:
        return {"mode": "핀", "action": "아이디어 제안"}
    elif "사주" in message:
        return {"mode": "노트", "action": "성향 분석"}
    elif "궁합" in message:
        return {"mode": "노바", "action": "궁합 판단"}
    else:
        return {"mode": "루피트", "action": "추가 판단 필요"}
