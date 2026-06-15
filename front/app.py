import streamlit as st
import requests

st.title("여행지 추천 프로그램")

location = st.selectbox("위치", ["국내", "해외"])
purpose = st.selectbox("목적", ["휴식", "관광", "맛집", "쇼핑"])
style = st.selectbox("선호 여행 스타일", ["자연", "도시", "역사/문화", "휴양"])
duration = st.number_input("여행 기간", min_value=1, max_value=30, value=3)

if st.button("추천받기"):
    data = {
        "location": location,
        "purpose": purpose,
        "style": style,
        "duration": duration
    }

    response = requests.post(
        "http://localhost:8000/recommend",
        json=data
    )

    if response.status_code == 200:
        result = response.json()
        st.subheader("추천 여행지")
        st.write(result["recommended_destination"])
