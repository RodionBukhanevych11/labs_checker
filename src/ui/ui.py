import json
import requests
import streamlit as st
import tempfile
import os

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

def send_upload_request(
    backend_host: str,
    backend_port: str,
    username: str,
    file: bytes
):
    request_json = {"usename": username,
                    "lab_file": file}
    request_url = backend_host + ":" + backend_port + "/check"
    response = requests.post(url=request_url, json=request_json)
    return response

def create_folder(username: str):
    print("create_folder: ", st.session_state["username"])
    path = os.path.join("data", username)
    os.makedirs(path, exist_ok = True)
    return path

def save_file(lab_bytes: bytes,
              folder: str,
              lab: str):
    str_data = lab_bytes.decode('utf-8')
    path = os.path.join(folder,
                        f"""{lab} {st.session_state["username"]}.py""")
    with open(path, 'w') as file:
            file.write(str_data)
    return path

st.set_page_config(
    page_title="Labs Checker"
)

if "result" not in st.session_state:
    st.session_state["result"] = "unauthorized"
if "username" not in st.session_state:
    st.session_state["username"] = None

_ = st.title("Labs Checker")

def ui_authorized():
    options = ("Lab 1 Main",
               "Lab 1 Additional")
    selectbox_labs_value = st.selectbox("Choose Lab", options=options)
    file_uploader_lab_value = st.file_uploader("Upload file")
    button_examine =  st.button("Examine")

    if button_examine:
        if file_uploader_lab_value:
            lab_bytes = file_uploader_lab_value.read()
            # request_lab = send_upload_request(backend_host=_CONFIG["backend_host"],
            #                                 backend_port=str(_CONFIG["backend_port"]),
            #                                 username=st.session_state["username"],
            #                                 file=lab_bytes)
            save_path = create_folder(username=st.session_state["username"])
            save_file(lab_bytes=lab_bytes,
                      folder=save_path,
                      lab=selectbox_labs_value)

def ui_unauthorized():
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
            st.session_state["result"] = sign_up_response.json()["result"]
            if st.session_state["result"] == "authorized":
                st.session_state["username"] = input_username_value
    with col1_2:
        if st.button("Sign in"):
            sign_in_response = send_authorize_request(backend_host=_CONFIG["backend_host"],
                                            backend_port=str(_CONFIG["backend_port"]),
                                            action="sign in",
                                            username_message=input_username_value,
                                            password_message=input_password_value)
            if sign_in_response:
                st.session_state["result"] = sign_in_response.json()["result"] 
                if st.session_state["result"] == "authorized":
                    st.session_state["username"] = input_username_value
                print(st.session_state["username"])
        

if __name__=="__main__":
    if st.session_state["result"] == "authorized":
        ui_authorized()
    elif st.session_state["result"] == "unauthorized":
        ui_unauthorized()
