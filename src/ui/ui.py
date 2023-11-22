import json
import requests
import streamlit as st

_CONFIG = json.load(open("src/config.json"))


def send_authorize_request(
    backend_host: str,
    backend_port: str,
    action: str,
    username_message: str = "",
    password_message: str = "",
):
    request_json = {"action": action,
                    "username": username_message,
                    "password": password_message}
    request_url = backend_host + ":" + backend_port + "/authorize"
    response = requests.post(url=request_url, json=request_json)
    return response


def ui():
    _ = st.header("Authorization")
    input_username_value = st.text_input('Username')
    input_password_value = st.text_input('Password')
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        if st.button("Sign up"):
            sign_up_response = send_authorize_request(backend_host=_CONFIG["backend_host"],
                                            backend_port=str(_CONFIG["backend_port"]),
                                            action="sign up",
                                            username_message=input_username_value,
                                            password_message=input_password_value)
    with col1_2:
        if st.button("Sign in"):
            sign_in_response = send_authorize_request(backend_host=_CONFIG["backend_host"],
                                            backend_port=str(_CONFIG["backend_port"]),
                                            action="sign in",
                                            username_message=input_username_value,
                                            password_message=input_password_value)
        

if __name__=="__main__":
    ui()
