import streamlit as st

# ファイルアップロード
uploaded_file = st.file_uploader("ファイル選択")

# アップロードされたファイルがある場合
if uploaded_file is not None:
    # ファイルを読み込んで表示する
    file_contents = uploaded_file.read()
