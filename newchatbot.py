from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model=ChatOpenAI()
st.header("Ai Chatbot")
messages=[SystemMessage(content="YOU ARE ANY CHAT ASSISTANT")
]
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to handle input and response
def handle_input():
    user_message = st.session_state.user_input
    st.session_state.messages.append(HumanMessage(content=user_message))
    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    st.session_state.user_input = ""  # This works now because it's in the callback

# Show chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.write("You:", msg.content)
    else:
        st.write("A.I:", msg.content)

# Text input with callback
st.text_input("You:", key="user_input", on_change=handle_input)
