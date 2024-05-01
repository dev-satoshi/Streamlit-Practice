import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader

# 設定ファイルの読み込み
with open("./config.yml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# 認証オブジェクトを作成
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# ログインフォームの表示
if st.session_state["authentication_status"] is None:
    authenticator.login()

# ログイン成功時の処理
if st.session_state["authentication_status"]:
    st.write(f'ようこそ *{st.session_state["name"]}* さん！')
    st.success("ログインに成功しました。")
    authenticator.logout()
    # st.switch_page("pages/garbage_list.py") リダイレクトではない
elif st.session_state["authentication_status"] is None:
    st.info("ユーザー名とパスワードを入力してください。")
elif st.session_state["authentication_status"] is False:
    st.error("ユーザー名・パスワードが間違っています。")
