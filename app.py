import pip
import streamlit as st
pip install langchain==0.3.0 openai==1.47.0 langchain-community==0.3.0 langchain-openai==0.2.2 httpx==0.27.2
pip install python-dotenv

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = []

st.title("提出課題: LLMを用いたWebアプリ")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["地理に関する質問", "健康に関する質問"]
)

st.divider()

if selected_item == "地理に関する質問":
    SystemMessage(content="あなたは、世界の地理に関する専門家です。"),
    human_message = st.text_input(label="世界の地理に関する質問を入力してください。")

else:
    SystemMessage(content="あなたは、健康に関する専門家です。"),
    human_message = st.text_input(label="健康に関する質問を入力してください。")

if st.button("実行"):
    st.divider()

result = llm(messages)
st.write(f"回答: **{result.content}**")