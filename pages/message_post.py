import requests
import streamlit as st

user_input = st.text_input("入力:")
submit_button = st.button("送信")

# バックエンドAPIのエンドポイント
API_ENDPOINT = "http://example.com/api"

# 送信ボタンがクリックされたときの処理
if submit_button:
    # ユーザーからの入力を取得
    input_data = {"input": user_input}

    # APIにPOSTリクエストを送信
    response = requests.post(API_ENDPOINT, json=input_data)

    # レスポンスを処理
    if response.status_code == 200:
        st.success("APIへのリクエストが成功しました")
        result = response.json()
        st.write("APIからのレスポンス:", result)
    else:
        st.error("APIへのリクエストが失敗しました")
