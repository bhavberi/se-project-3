import streamlit as st
from streamlit_cookies_controller import CookieController
import requests
import json

def get_all_cookies():
    controller = CookieController()
    
    all_cookies = controller.getAll()
    for cookie in all_cookies:
        if type(all_cookies[cookie]) == type({'a': 1}):
            all_cookies[cookie] = json.dumps(all_cookies[cookie])
    
    return all_cookies

st.title("Report")
my_cookies = get_all_cookies()
if "access_token_se_p3" in my_cookies:
    url = "http://localhost/api/users/current"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers, cookies=my_cookies)

    username = json.loads(response.content)["username"]
    role = json.loads(response.content)["role"]

    st.session_state["logged_in_user"] = username
    st.session_state["logged_in_role"] = role

if st.session_state["logged_in_user"] is None:
    st.warning("You need to login first.")
    st.stop()
    
# add verification for type of user
if st.session_state["logged_in_role"] not in ["recruiter"]:
    st.warning("You need to be a recruiter to view a report.")
    st.stop()


st.write(f"{st.session_state['application_report']}")
    
