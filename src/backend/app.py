import os, json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db_utils.process import LabsCheckerDB


app = FastAPI()
_CONFIG = json.load(open("src/config.json"))


class AuthorizeRequest(BaseModel):
    action: str
    username: str
    password: str


@app.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the LabsChecker API"})



@app.post("/authorize")
async def authorize(request: AuthorizeRequest):
    action = request.action
    username = request.username
    password = request.password
    print(username, password)
    db = LabsCheckerDB(dbname=_CONFIG["dbname"],
                    user=_CONFIG["user"],
                    password='12345678',
                    host=_CONFIG["dbhost"])
    if action == "sign up":
        if username and password:
            if not db.check_user(username):
                db.register_user(username=username, password=password)
            return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                }, status_code=210)
        elif username and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                }, status_code=410)
        elif not username and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username",
                }, status_code=411)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username and password",
                }, status_code=413)
    
    if action == "sign in":
        if username and password:
            return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                }, status_code=220)
        elif username and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                }, status_code=421)
        elif not username and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username",
                }, status_code=422)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username and password",
                }, status_code=423)


if __name__ == "__main__":
    uvicorn.run(app, port=_CONFIG["backend_port"])