import streamlit as st
import plotly.express as px
import pandas as pd

st.title("서울 주요 관광지 지도")

# 데이터프레임
df = pd.DataFrame({
    '장소': ['경복궁', '남산타워'],
    '위도': [37.5702, 37.5512],
    '경도': [126.992, 126.9882]
})

# Plotly 지도 생성
fig = px.scatter_mapbox(df, lat='위도', lon='경도', text='장소',
                        zoom=11, height=600)

# 무료 지도 스타일 사용
fig.update_layout(mapbox_style="open-street-map")

# ✅ Streamlit에서 출력
st.plotly_chart(fig)
