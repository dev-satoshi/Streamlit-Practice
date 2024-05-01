import pandas as pd
import streamlit as st
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right

st.chat_input("What is up?")
