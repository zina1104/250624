import streamlit as st
import pandas as pd

# CSV 파일 읽기
@st.cache_data
def load_data():
    df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding="euc-kr")
    df['행정구역'] = df['행정구역'].str.replace(r"\s*\(.*\)", "", regex=True)
    df['총인구수'] = df['2025년05월_계_총인구수'].str.replace(",", "").astype(int)

    age_columns = [col for col in df.columns if col.startswith("2025년05월_계_") and '세' in col]
    new_age_columns = [col.replace("2025년05월_계_", "").replace("세", "").replace(" ", "") for col in age_columns]

    age_df = df[['행정구역', '총인구수'] + age_columns].copy()
    age_df.columns = ['행정구역', '총인구수'] + new_age_columns
    top5_df = age_df.sort_values(by='총인구수', ascending=False).head(5)
    return top5_df, new_age_columns

st.title("2025년 5월 기준 상위 5개 지역 연령별 인구 현황")

# 데이터 불러오기
data, age_cols = load_data()

st.subheader("📊 원본 데이터 (상위 5개 지역)")
st.dataframe(data)

# 연령별 인구 시각화
st.subheader("📈 연령별 인구 선 그래프")
chart_data = data.set_index('행정구역')[age_cols].T
chart_data.index.name = "연령"

st.line_chart(chart_data)
