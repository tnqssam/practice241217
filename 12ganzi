import streamlit as st

def get_zodiac(year):
    # 12간지 띠와 이모티콘 매핑
    zodiac_animals = [
        ("원숭이", "🐵"),  # 0
        ("닭", "🐓"),  # 1
        ("개", "🐕"),  # 2
        ("돼지", "🐷"),  # 3
        ("쥐", "🐀"),  # 4
        ("소", "🐂"),  # 5
        ("호랑이", "🐅"),  # 6
        ("토끼", "🐇"),  # 7
        ("용", "🐉"),  # 8
        ("뱀", "🐍"),  # 9
        ("말", "🐎"),  # 10
        ("양", "🐑")   # 11
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
