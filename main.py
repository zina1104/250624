import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os
from PIL import Image
import uuid

# 폴더 준비
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 세션 초기화
if "records" not in st.session_state:
    st.session_state.records = []

# 🔽 사용자 입력 영역
st.title("📸 나만의 여행기록 지도")
st.markdown("성룡이와 함께한 여행지를 직접 기록해보세요. 사진과 이야기가 지도에 나타납니다.")

with st.form("travel_form"):
    place_name = st.selectbox("여행한 지역을 선택하세요", [
        "경주시", "제주시", "여수시", "철원군", "부산광역시", "제천시", "양평군"
    ])
    story = st.text_area("여행 에피소드를 적어주세요", max_chars=200)
    image_file = st.file_uploader("여행 사진을 업로드하세요 (JPG/PNG)", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("📍 지도에 추가하기")

    if submitted:
        if not story:
            st.warning("에피소드를 입력해주세요.")
        elif not image_file:
            st.warning("사진을 업로드해주세요.")
        else:
            file_id = str(uuid.uuid4())[:8]
            file_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.jpg")
            img = Image.open(image_file)
            img.save(file_path)

            st.session_state.records.append({
                "place": place_name,
                "story": story,
                "image_path": file_path
            })
            st.success(f"✅ {place_name}이(가) 지도에 추가되었습니다.")

# 🔽 지도 만들기
m = folium.Map(location=[36.5, 127.8], zoom_start=7, tiles="CartoDB positron")

# GeoJSON 로딩
with open("skorea_municipalities_geo_simple.json", encoding="utf-8") as f:
    geo_data = json.load(f)

# 🌈 컬러 팔레트
color_palette = ["#E63946", "#2A9D8F", "#F4A261", "#457B9D", "#B5838D", "#6D6875", "#A8DADC"]

# 🔽 지도에 기록 반영
for idx, feature in enumerate(geo_data["features"]):
    name = feature["properties"]["name"]
    matched = [r for r in st.session_state.records if r["place"] == name]

    if matched:
        record = matched[-1]  # 가장 최근 기록
        color = color_palette[idx % len(color_palette)]
        opacity = 0.85
        border = "black"
        weight = 2

        popup_html = f"""
        <div style="width:220px;">
            <h4>{name}</h4>
            <img src="data:image/jpeg;base64,{(open(record['image_path'], 'rb').read()).encode('base64').decode()}" width="200" style="border-radius:6px;"><br>
            <p>{record['story']}</p>
        </div>
        """
        popup = folium.Popup(popup_html, max_width=250)
    else:
        color = "#f0f0f0"
        opacity = 0.03
        border = "#ccc"
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

# 🔽 지도 표시
st.subheader("🗺️ 나의 여행지 지도")
st_folium(m, width=1000, height=650)