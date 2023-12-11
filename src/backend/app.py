import re
import os, json
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db_utils.process import LabsCheckerDB
from src.backend.utils import inference
import time


app = FastAPI()
_CONFIG = json.load(open("src/config.json"))
db = LabsCheckerDB(dbname=_CONFIG["db_name"],
                    user=_CONFIG["db_user"],
                    password=_CONFIG["db_password"],
                    table_name=_CONFIG["db_table_name"],
                    host=_CONFIG["db_host"])

class AuthorizeRequest(BaseModel):
    action: str
    username: str
    password: str

class LabRequest(BaseModel):
    username: str
    lab_file: bytes

def is_injected(string) -> bool:
    if re.search(r"[^A-Za-z0-9]+", string):
        return True
    else:
        return False

@app.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the LabsChecker API"})


@app.post("/authorize")
async def authorize(request: AuthorizeRequest):
    action = request.action
    username = request.username
    password = request.password
    if is_injected(username) or is_injected(password):
        return JSONResponse(content={
            "status": "unsuccess",
            "message": "Bad Request",
            "result": "unauthorized"
            }, status_code=400)
    
    if action == "sign up":
        if username and password:
            if not db.check_user(username):
                db.register_user(username, password)
                print("Registered!")
                return JSONResponse(content={
                    "status": "success",
                    "message": "Processed",
                    "result": "authorized"
                    }, status_code=214)
            return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                "result": "unauthorized"
                }, status_code=210)
        elif username and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                "result": "unauthorized"
                }, status_code=410)
        elif not username and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username",
                "result": "unauthorized"
                }, status_code=411)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username and password",
                "result": "unauthorized"
                }, status_code=413)
    
    if action == "sign in":
        if username and password:
            if db.check_user(username) and db.check_password(username, password):
                print("Signed in!")
                return JSONResponse(content={
                "status": "success",
                "message": "Processed",
                "result": "authorized"
                }, status_code=220)
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "wrong data",
                "result": "unauthorized"
                }, status_code=424)
        elif username and not password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty password",
                "result": "unauthorized"
                }, status_code=421)
        elif not username and password:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username",
                "result": "unauthorized"
                }, status_code=422)
        else:
            return JSONResponse(content={
                "status": "unsuccess",
                "message": "empty username and password",
                "result": "unauthorized"
                }, status_code=423)


@app.post("/check")
async def check(request: LabRequest):
    username = request.username
    lab_file = request.lab_file
    inference(lab_file=lab_file)
    return JSONResponse(content={})

if __name__ == "__main__":
    uvicorn.run(app, port=_CONFIG["backend_port"])
