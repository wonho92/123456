import streamlit as st

# 페이지 구성
st.set_page_config(page_title="Q&A 앱", page_icon="💬", layout="wide")

# 사용자 정의 스타일
st.markdown("""
<style>
/* 전체 배경 */
body {
    background-color: #f9f9f9;
}

/* 앱 제목 */
h1 {
    color: #2c3e50;
}

/* Expander 스타일 */
.streamlit-expanderHeader {
    font-weight: bold;
    font-size: 18px;
    color: #34495e !important;
}

.streamlit-expander:hover {
    border: 1px solid #3498db !important;
    box-shadow: 0 0 6px #3498db50;
    background-color: #ecf6fc;
}

/* 사이드바 배경과 텍스트 */
section[data-testid="stSidebar"] {
    background-color: #eaf2f8;
}

.css-1d391kg {  /* 일반 텍스트 스타일 */
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# 사이드바 메뉴
st.sidebar.title("📁 메뉴")
menu = st.sidebar.radio("카테고리 선택", ["회사 일반", "조직문화", "인사제도", "복리후생"])

# 데이터
qa_data = [
    {"category": "회사 일반", "question": "회사의 주요 사업 분야는 무엇인가요?", "answer": "보안 솔루션 개발 및 시스템 구축, 모바일 커머스 서비스를 주력으로 하고 있습니다."},
    {"category": "회사 일반", "question": "조직 규모는 어떻게 되나요?", "answer": "약 250명의 임직원이 재직 중이며, 절반 이상이 R&D 및 기술영업 인력입니다."},
    {"category": "조직문화", "question": "사내 커뮤니케이션 방식은 어떤 편인가요?", "answer": "슬랙과 노션을 사용하며 수평적인 분위기에서 자유롭게 의견을 주고받습니다."},
    {"category": "조직문화", "question": "회식이나 사내 행사는 어떤가요?", "answer": "자율참여 중심이며 분기마다 리프레시 프로그램을 진행합니다."},
    {"category": "인사제도", "question": "평가 제도는 어떻게 운영되나요?", "answer": "분기별 OKR 및 직무/역량 평가를 포함하며, 상사와의 면담도 포함됩니다."},
    {"category": "인사제도", "question": "승진 기준은 무엇인가요?", "answer": "직무성과와 리더십 역량을 기반으로 연 1회 심사합니다."},
    {"category": "복리후생", "question": "식대나 교통비는 지원되나요?", "answer": "구내식당 제공 및 월 10만원까지 외부 식대 지원, 교통비는 미지원입니다."},
    {"category": "복리후생", "question": "건강검진은 제공되나요?", "answer": "전 임직원 대상 건강검진과 심리상담, 헬스케어 앱 서비스도 지원됩니다."}
]

# 본문 출력
st.title("💬 질문을 선택하고 답변을 확인하세요")

# 선택된 카테고리의 질문만 필터링
filtered = [q for q in qa_data if q["category"] == menu]

for qa in filtered:
    with st.expander(qa["question"]):
        st.write(qa["answer"])
