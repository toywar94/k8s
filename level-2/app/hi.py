from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 origin 허용 (보안 상 필요에 따라 수정)
    allow_methods=["GET", "POST", "OPTIONS"],  # 허용할 메서드 목록에 OPTIONS 추가
    allow_headers=["*"],  # 모든 헤더 허용 (보안 상 필요에 따라 수정)
)

@app.get("/api/hi")
def return_hi():
    return {"message": "Hi"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)