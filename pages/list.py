import pandas as pd
import requests
import streamlit as st

st.write("# 一覧ページ")

# モックAPI
API_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"

# モックAPIからデータを取得
response = requests.get(API_ENDPOINT)

# レスポンスが成功した場合
if response.status_code == 200:
    data = response.json()  # JSON形式のレスポンスをデコード
    df = pd.DataFrame(data)  # 辞書を含むリストに変換してDataFrameに変換
    aa = df["id"].unique()
    st.write(df)  # DataFrameを表示
    s = st.selectbox("ゴミの出し方を選択", aa, key="df")
    ss = df[df["id"] == s]
    st.table(ss)
else:
    st.error("Failed to fetch data from backend API")
