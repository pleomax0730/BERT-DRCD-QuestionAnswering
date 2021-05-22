import streamlit as st
import requests


st.title("BERT DRCD QuestionAnswering")


# backend_pred_url = "http://fastapi:8000/predict/"
backend_pred_url = "http://127.0.0.1:8000/predict/"

with st.form("input_area"):

    # setting default value
    text_area_value = "鴻海科技集團是由臺灣企業家郭台銘創辦的跨國企業，總部位於臺灣新北市土城區，主要生產地則在中國大陸，以富士康做為商標名稱。其專注於電子產品的代工服務，研發生產精密電氣元件、機殼、準系統、系統組裝、光通訊元件、液晶顯示件等3C產品上、下游產品及服務。"
    text_input_value = "鴻海集團總部位於哪裡？"

    text = st.text_area(
        "Paragraph: ",
        value=text_area_value,
        help="BERT model can only process 512 tokens, the rest tokens will be truncated.",
    )
    query = st.text_input("Question: ", value=text_input_value)

    submitted = st.form_submit_button("Submit")
    if submitted:
        if not text or not query:
            st.warning("Paragraph and Question should not be empty.")
        else:
            payload = {"text": text, "query": query}
            with st.spinner("It'll take a while to run for the first time. Please wait."):
                result = requests.post(backend_pred_url, json=payload)
                st.write(result.json())
