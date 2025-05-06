from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

# Use Streamlit secrets to load your OpenAI API key
from openai import OpenAIError

openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the model with API key
model = ChatOpenAI(openai_api_key=openai_api_key)

# App UI
st.header("AI Chatbot")
messages = [SystemMessage(content="You are any chat assistant.")]

if "messages" not in st.session_state:
    st.session_state.messages = messages

# Function to handle input and response
def handle_input():
    user_message = st.session_state.user_input
    st.session_state.messages.append(HumanMessage(content=user_message))
    try:
        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
    except OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
    st.session_state.user_input = ""

# Show chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.write("You:", msg.content)
    else:
        st.write("AI:", msg.content)

# Text input with callback
st.text_input("You:", key="user_input", on_change=handle_input)
