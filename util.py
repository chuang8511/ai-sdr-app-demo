import streamlit as st

def append_session(key, val):
    st.session_state[key].append(val)
    
def set_session(key, val):
    st.session_state[key] = val

def get_session(key):
    return st.session_state[key] if key in st.session_state else None

def is_status(stage):
    return get_session("stage") == stage