
申し訳ありません。少し手順に誤りがあったかもしれません。

app.py を手動で作成する必要があります。以下の手順に従って app.py を作成してください。


---

手順：app.py の作成

1. GitHubでの手順

dogdog1122/nana-papa-baken のリポジトリを開いてください。

「Add file」 → 「Create new file」 をクリックします。



2. ファイル名を入力

ファイル名欄に app.py と入力します。



3. コードを貼り付け
下記のコードをそのままコピーし、作成した app.py に貼り付けます：



import streamlit as st
import pandas as pd

st.title("奈々パパの配置馬券術 ツール")

st.markdown("---")

# ファイルアップロード
shobyo_file = st.file_uploader("出馬表CSVをアップロード", type=["csv", "txt"])
odds_file = st.file_uploader("オッズCSVをアップロード", type=["csv", "txt"])

if shobyo_file and odds_file:
    try:
        df_shobyo = pd.read_csv(shobyo_file)
        df_odds = pd.read_csv(odds_file)

        st.subheader("出馬表プレビュー")
        st.dataframe(df_shobyo.head())

        st.subheader("オッズ表プレビュー")
        st.dataframe(df_odds.head())

        # フィルター条件の適用
        st.markdown("### 条件に一致する馬を抽出：")

        # 人気と単勝オッズを条件にフィルター
        filtered = df_odds[(df_odds['人気'] <= 9) & (df_odds['単勝'] >= 10.0) & (df_odds['単勝'] <= 50.0)]

        if not filtered.empty:
            merged = pd.merge(df_shobyo, filtered, on='馬番')
            st.success(f"{len(merged)} 件ヒットしました！")
            st.dataframe(merged)
        else:
            st.warning("条件に一致する馬が見つかりませんでした。")

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

else:
    st.info("出馬表とオッズのCSVファイルをアップロードしてください。")

4. ファイルを保存

画面下部の「Commit new file」をクリックしてファイルを保存します。





---

これで app.py が作成され、GitHubリポジトリにアップロードされます。
その後、Streamlitでアプリをデプロイできますので、手順が完了したらお知らせください。


手順：app.py の作成

1. GitHubでの手順

dogdog1122/nana-papa-baken のリポジトリを開いてください。

「Add file」 → 「Create new file」 をクリックします。



2. ファイル名を入力

ファイル名欄に app.py と入力します。



3. コードを貼り付け
下記のコードをそのままコピーし、作成した app.py に貼り付けます：



import streamlit as st
import pandas as pd

st.title("奈々パパの配置馬券術 ツール")

st.markdown("---")

# ファイルアップロード
shobyo_file = st.file_uploader("出馬表CSVをアップロード", type=["csv", "txt"])
odds_file = st.file_uploader("オッズCSVをアップロード", type=["csv", "txt"])

if shobyo_file and odds_file:
    try:
        df_shobyo = pd.read_csv(shobyo_file)
        df_odds = pd.read_csv(odds_file)

        st.subheader("出馬表プレビュー")
        st.dataframe(df_shobyo.head())

        st.subheader("オッズ表プレビュー")
        st.dataframe(df_odds.head())

        # フィルター条件の適用
        st.markdown("### 条件に一致する馬を抽出：")

        # 人気と単勝オッズを条件にフィルター
        filtered = df_odds[(df_odds['人気'] <= 9) & (df_odds['単勝'] >= 10.0) & (df_odds['単勝'] <= 50.0)]

        if not filtered.empty:
            merged = pd.merge(df_shobyo, filtered, on='馬番')
            st.success(f"{len(merged)} 件ヒットしました！")
            st.dataframe(merged)
        else:
            st.warning("条件に一致する馬が見つかりませんでした。")

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

else:
    st.info("出馬表とオッズのCSVファイルをアップロードしてください。")

4. ファイルを保存

画面下部の「Commit new file」をクリックしてファイルを保存します。





---

これで app.py が作成され、GitHubリポジトリにアップロードされます。
その後、Streamlitでアプリをデプロイできますので、手順が完了したらお知らせください。

