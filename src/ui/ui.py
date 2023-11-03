import json
import requests
import streamlit as st

_CONFIG = json.load(open("src/config.json"))


def send_request(backend_host: str, backend_port: str, caller: str, url_message: str = "", login_message: str = "", password_message: str = "", labs_value: str = ""):
    request_json = {"url": url_message,
                    "login": login_message,
                    "password": password_message,
                    "caller": caller}
    request_url = backend_host + ":" + backend_port + "/process"
    response = requests.post(url=request_url, json=request_json)
    return response


def ui():
    col1, col2 = st.columns(2)

    list_labs = [
        "Lab 1 Main",
        "Lab 1 Additional",
        "Lab 2 Main",
        "Lab 2 Additional"
    ]

    with col1:
        header_authorization = st.header("Authorization")
        input_login_value = st.text_input('Login')
        input_password_value = st.text_input('Password')
        col1_1, col1_2 = st.columns(2)
        
        with col1_1:
            button_sign_in = st.button("Sign up")
        
        with col1_2:
            button_sign_up = st.button("Sign in")
    with col2:
        header_examination = st.header("Examination")
        selectbox_labs = st.selectbox("Labs", list_labs)
        input_url_value = st.text_input('URL')
        button_examine = st.button("Examine")

    if button_examine:
        response = send_request(backend_host=_CONFIG["backend_host"],
                    backend_port=str(_CONFIG["backend_port"]),
                    caller="button_examine",
                    url_message=input_url_value)
        print(response.status_code)

    if button_sign_up:
        response = send_request(backend_host=_CONFIG["backend_host"],
                    backend_port=str(_CONFIG["backend_port"]),
                    caller="button_sign_up",
                    login_message=input_login_value,
                    password_message=input_password_value)
        print(response.status_code)
    
    if button_sign_in:
        response = send_request(backend_host=_CONFIG["backend_host"],
                    backend_port=str(_CONFIG["backend_port"]),
                    caller="button_sign_in",
                    login_message=input_login_value,
                    password_message=input_password_value)
        print(response.status_code)

if __name__=="__main__":
    ui()

