import os, json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()
_CONFIG = json.load(open("src/config.json"))


class PredictionRequest(BaseModel):
    url: str


@app.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the LabsChecker API"})


@app.post("/process")
async def get_results(request: PredictionRequest):
    url = request.url
    print(url)
    if url:
        return JSONResponse(content={
            "status": "success",
            "message": "Processed",
            }, status_code=200)
    else:
        return JSONResponse(content={
            "status": "unsuccess",
            "message": "empty url"
        }, status_code=400)


if __name__ == "__main__":
    uvicorn.run(app, port=_CONFIG["backend_port"])