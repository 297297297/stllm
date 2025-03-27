import streamlit as st
from zhipuai import ZhipuAI  # 替换为智谱AI的库

st.title("🦜🔗 Quickstart App")

zhipuai_api_key = st.sidebar.text_input("ZhipuAI API Key", type="password")  # 修改为智谱AI的API Key输入


def generate_response(input_text):
    client = ZhipuAI(api_key=zhipuai_api_key)  # 使用智谱AI的客户端
    response = client.chat.completions.create(
        model="glm-4",  # 使用智谱AI的GLM-4模型
        messages=[{"role": "user", "content": input_text}],
        temperature=0.7
    )
    st.info(response.choices[0].message.content)  # 获取并显示响应内容


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not zhipuai_api_key:  # 修改为检查智谱AI的API Key
        st.warning("Please enter your ZhipuAI API key!", icon="⚠")
    if submitted and zhipuai_api_key:
        generate_response(text)