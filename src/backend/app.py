import os, json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()
_CONFIG = json.load(open("src/config.json"))


class PredictionRequest(BaseModel):
    caller: str
    url: str
    login: str
    password: str
    lab: str


@app.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the LabsChecker API"})


@app.post("/process")
async def get_results(request: PredictionRequest):
    caller = request.caller
    url = request.url
    login = request.login
    password = request.password
    lab = request.lab
    print(url, '\n', login, '\n', password)
    
    if caller == "button_examine":
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
    
    if caller == "button_sign_up":
        if login and password:
            return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                }, status_code=210)
        elif login and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                }, status_code=410)
        elif not login and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty login",
                }, status_code=411)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty login and password",
                }, status_code=413)
    
    if caller == "button_sign_in":
        if login and password:
            return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                }, status_code=220)
        elif login and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                }, status_code=421)
        elif not login and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty login",
                }, status_code=422)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty login and password",
                }, status_code=423)
        

if __name__ == "__main__":
    uvicorn.run(app, port=_CONFIG["backend_port"])