import streamlit as st

def get_zodiac(year):
    # 12간지 띠와 이모티콘 매핑
    zodiac_animals = [
        ("쥐", "🐀"),  # 0
        ("소", "🐂"),  # 1
        ("호랑이", "🐅"),  # 2
        ("토끼", "🐇"),  # 3
        ("용", "🐉"),  # 4
        ("뱀", "🐍"),  # 5
        ("말", "🐎"),  # 6
        ("양", "🐑"),  # 7
        ("원숭이", "🐵"),  # 8
        ("닭", "🐓"),  # 9
        ("개", "🐕"),  # 10
        ("돼지", "🐷")   # 11
    ]

    zodiac_index = (year - 4) % 12
    return zodiac_animals[zodiac_index]

# Streamlit UI
st.title("12간지 띠 알아보기")

# 사용자로부터 출생년도 입력받기
year = st.number_input("출생년도를 입력하세요:", min_value=0, step=1)

if year:
    animal, emoji = get_zodiac(year)
    st.subheader(f"당신의 띠는 {animal}띠 {emoji} 입니다!")
