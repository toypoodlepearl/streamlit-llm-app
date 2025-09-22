##  from dotenv import load_dotenv

##  load_dotenv()

from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


st.title("提出課題: LLMを用いたWebアプリ")

st.write("##### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

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
st.write(f"回答: **{human_message}**")