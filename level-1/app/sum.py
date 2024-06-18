from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/sum")
def calculate_sum(numbers: Numbers):
    result = numbers.a + numbers.b
    return {"sum": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)