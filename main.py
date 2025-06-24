import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(layout="wide")
st.title("📸 성룡이와 함께한 여행지 감성 지도")
st.caption("여행했던 지역은 컬러풀하게 강조되며, 클릭하면 사진과 에피소드가 나와요.")

# 🌈 감성 팔레트 (다채로운 색상)
color_palette = [
    "#E63946",  # 빨강
    "#F4A261",  # 오렌지
    "#2A9D8F",  # 청록
    "#A8DADC",  # 민트
    "#457B9D",  # 파랑
    "#B5838D",  # 장미빛
    "#6D6875",  # 톤다운 보라
]

# ✅ 지역별 사진 및 에피소드 정보
places_info = {
    "경주시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Bulguksa_temple.jpg",
        "story": "약혼함"
    },
    "제주시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Jeju_Island.jpg",
        "story": "스노쿨링&올레길"
    },
    "여수시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Yeosu_night.jpg",
        "story": "금오도 트레킹"
    },
    "철원군": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/bf/CheorwonDMZ.jpg",
        "story": "DMZ 뮤직 페스티벌 & 노동당사"
    },
    "부산광역시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/Busan_night.jpg",
        "story": "광안리 불꽃축제"
    },
    "제천시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Cheongpung_Lake.jpg",
        "story": "온천"
    },
    "양평군": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Dumulmeori.jpg",
        "story": "두물머리에서 핫도그"
    }
}

visited_places = list(places_info.keys())

# 지도 생성 (고급 스타일)
m = folium.Map(location=[36.5, 127.8], zoom_start=7, tiles="CartoDB positron")

# GeoJSON 파일 열기
with open("skorea_municipalities_geo_simple.json", encoding='utf-8') as f:
    geo_data = json.load(f)

# 각 지역 그리기
for idx, feature in enumerate(geo_data["features"]):
    name = feature["properties"]["name"]
    is_visited = name in visited_places

    if is_visited:
        color = color_palette[idx % len(color_palette)]
        opacity = 0.85
        border = "black"
        weight = 2.5

        # 팝업 HTML
        info = places_info[name]
        popup_html = f"""
        <div style="width:230px;">
            <h4 style="margin-bottom:4px;">{name}</h4>
            <img src="{info['image']}" width="210" style="border-radius:6px;"><br>
            <p style="margin-top:4px;">{info['story']}</p>
        </div>
        """
        popup = folium.Popup(popup_html, max_width=250)

    else:
        color = "#f0f0f0"
        opacity = 0.03
        border = "#cccccc"
        weight = 0.5
        popup = None

    folium.GeoJson(
        feature,
        style_function=lambda x, color=color, opacity=opacity, border=border, weight=weight: {
            "fillColor": color,
            "color": border,
            "weight": weight,
            "fillOpacity": opacity,
        },
        tooltip=name,
        popup=popup
    ).add_to(m)

# Streamlit 출력
st_folium(m, width=1000, height=650)
