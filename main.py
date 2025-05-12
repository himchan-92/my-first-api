from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "루피니티 서버 연결 성공!"}