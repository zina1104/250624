import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.title("📍 성룡이와 함께한 국내 여행지 지도")
st.markdown("붉게 칠해진 곳이 우리가 다녀온 여행지입니다.")

# 여행한 지역 리스트
visited_places = ['경주시', '제주시', '여수시', '철원군', '부산광역시', '제천시', '양평군']

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# GeoJSON 파일 로드
with open("skorea_municipalities_geo_simple.json", encoding="utf-8") as f:
    geo_data = json.load(f)

# 색칠 로직
for feature in geo_data["features"]:
    name = feature["properties"]["name"]
    color = "crimson" if name in visited_places else "lightgray"

    folium.GeoJson(
        feature,
        style_function=lambda x, color=color: {
            "fillColor": color,
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6 if color == "crimson" else 0.1,
        },
        tooltip=name,
    ).add_to(m)

# Streamlit에 출력
st_folium(m, width=700, height=500)
