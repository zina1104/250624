import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# 여행한 지역
visited_places = ['강릉시', '제주시', '순천시']

# 지도 중심
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 행정구역 GeoJSON 파일 로드 (시군구)
with open('skorea_municipalities_geo_simple.json', encoding='utf-8') as f:
    geo_data = json.load(f)

# 색칠
for feature in geo_data['features']:
    name = feature['properties']['name']
    color = 'red' if name in visited_places else 'gray'
    
    folium.GeoJson(
        feature,
        style_function=lambda x, color=color: {
            'fillColor': color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.5 if color == 'red' else 0.1
        },
        tooltip=name
    ).add_to(m)

# Streamlit에 표시
st.title("성룡이와 함께한 국내 여행지 지도")
st_data = st_folium(m, width=700, height=500)
