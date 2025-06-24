import streamlit as st

# MBTI별 추천 직업 사전 정의
mbti_jobs = {
    "ISTJ": ["📊 회계사", "⚖️ 변호사", "🗂️ 행정직 공무원"],
    "ISFJ": ["👩‍🏫 교사", "🩺 간호사", "🤝 사회복지사"],
    "INFJ": ["🧠 상담가", "✍️ 작가", "🧘 심리학자"],
    "INTJ": ["📈 전략기획가", "🔬 과학자", "💻 엔지니어"],
    "ISTP": ["🔧 기술자", "✈️ 파일럿", "👮 경찰관"],
    "ISFP": ["🎨 디자이너", "🎭 예술가", "🧑‍⚕️ 물리치료사"],
    "INFP": ["📜 시인", "🧘‍♀️ 심리상담사", "🌍 인류학자"],
    "INTP": ["🧪 이론물리학자", "🧑‍💻 프로그래머", "📚 철학자"],
    "ESTP": ["💼 세일즈 매니저", "🚑 응급 구조사", "🚀 기업가"],
    "ESFP": ["🎤 연예인", "🎉 이벤트 플래너", "📣 마케터"],
    "ENFP": ["🧠 카피라이터", "📢 홍보 전문가", "✊ 인권 운동가"],
    "ENTP": ["📊 기획자", "🏗️ 스타트업 창업가", "⚖️ 변호사"],
    "ESTJ": ["🏢 경영 관리자", "🪖 군인", "🎯 감독관"],
    "ESFJ": ["🏥 의료보조원", "👨‍🏫 교사", "🍽️ 서비스 매니저"],
    "ENFJ": ["🎤 강사", "🗳️ 정치가", "👥 인사 관리자"],
    "ENTJ": ["🧑‍💼 CEO", "🧑‍⚖️ 변호사", "📂 프로젝트 매니저"]
}

# Streamlit 인터페이스
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼")

st.title("💡 MBTI 기반 직업 추천기")

st.markdown("""
🎯 **당신의 MBTI 유형을 선택하면, 그에 어울리는 직업을 추천해드립니다!**

성격에 맞는 진로를 찾는 첫걸음이 될 거예요.  
각 직업 옆의 이모지도 함께 확인해보세요 😉
""")

mbti_types = list(mbti_jobs.keys())
selected_mbti = st.selectbox("🧬 당신의 MBTI는 무엇인가요?", mbti_types)

if selected_mbti:
    st.balloons()  # 풍선 효과
    st.subheader(f"🌟 {selected_mbti} 유형에 어울리는 추천 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
