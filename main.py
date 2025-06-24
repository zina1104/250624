import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(layout="wide")
st.title("📸 성룡이와 함께한 여행지 지도")
st.caption("붉은 지역은 여행지이며, 클릭하면 사진과 에피소드가 나옵니다.")

# ✅ 지역별 사진 및 에피소드 정보
places_info = {
    "경주시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Bulguksa_temple.jpg",
        "story": "불국사에서 단풍을 배경으로 사진 찍음"
    },
    "제주시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Jeju_Island.jpg",
        "story": "바람 부는 해변에서 같이 커피 마심"
    },
    "여수시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Yeosu_night.jpg",
        "story": "돌산대교 야경을 보며 드라이브"
    },
    "철원군": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/bf/CheorwonDMZ.jpg",
        "story": "DMZ 근처 평화전망대에서 감상"
    },
    "부산광역시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/Busan_night.jpg",
        "story": "광안리에서 밤바다 산책"
    },
    "제천시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Cheongpung_Lake.jpg",
        "story": "청풍호반길에서 드라이브"
    },
    "양평군": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Dumulmeori.jpg",
        "story": "두물머리에서 해돋이 감상"
    }
}

# 여행지 목록
visited_places = list(places_info.keys())

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# GeoJSON 불러오기
with open("skorea_municipalities_geo_simple.json", encoding='utf-8') as f:
    geo_data = json.load(f)

# 지도에 지역 표시
for feature in geo_data['features']:
    name = feature['properties']['name']
    is_visited = name in visited_places
    color = 'crimson' if is_visited else 'lightgray'

    popup_html = ""
    if is_visited:
        info = places_info[name]
        popup_html = f"""
        <div style="width:220px">
            <strong>{name}</strong><br>
            <img src="{info['image']}" width="200"><br>
            <p>{info['story']}</p>
        </div>
        """

    folium.GeoJson(
        feature,
        style_function=lambda x, color=color: {
            'fillColor': color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6 if is_visited else 0.1,
        },
        tooltip=name,
        popup=folium.Popup(popup_html, max_width=250) if is_visited else None
    ).add_to(m)

# Streamlit에 출력
st_data = st_folium(m, width=900, height=600)
