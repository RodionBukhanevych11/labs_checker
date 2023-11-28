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

def get_auth_request(
    backend_host: str,
    backend_port: str,
    action: str = "",
    username_message: str = "",
    password_message: str = ""):    
    request_json = {"action": action,
                    "username": username_message,
                    "password": password_message}
    request_url = backend_host + ":" + backend_port + "/result"
    res = requests.get(url=request_url, json=request_json)
    print(res.json())
    return res.json()


st.set_page_config(
    page_title="Labs Checker"
)

if "result" not in st.session_state:
    st.session_state["result"] = "unauthorized"

_ = st.title("Labs Checker")

def ui_authorized():
    options = ("Lab 1 Main",
               "Lab 1 Additional")
    selectbox_labs_value = st.selectbox("Choose Lab", options=options)
    input_url_value = st.text_input("Url")
    button_examine =  st.button("Examine")

def ui_unauthorized():
    print(st.session_state["result"])
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
            print(sign_up_response.json())
            st.session_state["result"] = sign_up_response.json()["result"]
    with col1_2:
        if st.button("Sign in"):
            sign_in_response = send_authorize_request(backend_host=_CONFIG["backend_host"],
                                            backend_port=str(_CONFIG["backend_port"]),
                                            action="sign in",
                                            username_message=input_username_value,
                                            password_message=input_password_value)
            print(sign_in_response.json())
            st.session_state["result"] = sign_in_response.json()["result"]

            print(st.session_state["result"] == "unauthorized") 
        

if __name__=="__main__":
    if st.session_state["result"] == "authorized":
        ui_authorized()
    elif st.session_state["result"] == "unauthorized":
        ui_unauthorized()
