import json
import requests
import streamlit as st

_CONFIG = json.load(open("src/config.json"))


def send_request(backend_host: str, backend_port: str, url_message: str):
    request_json = {"url": url_message}
    request_url = backend_host + ":" + backend_port + "/process"
    response = requests.post(url=request_url, json=request_json)
    return response


def ui():
    input_url_value = st.text_input('URL')
    if input_url_value:
        response = send_request(backend_host=_CONFIG["backend_host"],
                    backend_port=str(_CONFIG["backend_port"]),
                    url_message=input_url_value)
        print(response.status_code)
    

if __name__=="__main__":
    ui()
