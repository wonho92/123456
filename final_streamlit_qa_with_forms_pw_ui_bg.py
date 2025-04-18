import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title='Tscientific Q&A', page_icon='💬', layout='wide')

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("photo_2024-03-27_12-49-56.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# 방문자 수 추적 기능
def update_visitor_count():
    file_path = "visitors.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visit_data = {"timestamp": now, "user": "anonymous"}
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([visit_data])], ignore_index=True)
    else:
        df = pd.DataFrame([visit_data])
    df.to_csv(file_path, index=False)
    return len(df)


if "visited" not in st.session_state:
    visitor_count = update_visitor_count()
    st.session_state["visited"] = True
else:
    visitor_count = pd.read_csv("visitors.csv").shape[0]

st.sidebar.markdown(f"👀 방문자 수: **{visitor_count}**명")

# 회사 로고
st.image("티사이언티픽로고(1538x582)_가로로 길게.png", use_container_width=False, width=300)

# 색상 테마
st.markdown("""<style>
.streamlit-expanderHeader {
    font-weight: bold;
    font-size: 18px;
    color: #003366 !important;
}
.streamlit-expander:hover {
    border: 1px solid #009fe3 !important;
    box-shadow: 0 0 6px #009fe380;
    background-color: #f1f9fd;
}
section[data-testid="stSidebar"] {
    background-color: #e6f4fb;
}
</style>""", unsafe_allow_html=True)

# 사이드바
st.sidebar.title("📁 카테고리 선택")

categories = ["Q&A", "커피챗", "방문 통계"]
menu = st.sidebar.radio("선택해주세요", ["Q&A", "커피챗"])


# Q&A 데이터
qa_data = [
    {"category": "회사 일반", "question": "회사의 주요 사업 분야는 무엇인가요?", "answer": "보안 솔루션 개발 및 시스템 구축, 그리고 모바일 커머스 서비스를 주력으로 하고 있습니다."},
    {"category": "회사 일반", "question": "조직 규모는 어떻게 되나요?", "answer": "현재 약 250명 정도의 임직원이 재직 중이며, R&D와 기술영업 인력이 절반 이상을 차지하고 있습니다."},
    {"category": "회사 일반", "question": "회사의 비전이나 중장기 전략이 있다면 알려주세요.", "answer": "기술 기반의 지속가능한 보안 생태계 구축을 목표로 하며, 글로벌 보안 시장 진출도 계획 중입니다."},
    {"category": "회사 일반", "question": "최근 1~2년간 주요 성과가 있다면 무엇인가요?", "answer": "국내 대형 공공기관 대상 보안 솔루션 수주와 T사 파트너십을 통해 연 매출 400억 원을 돌파했습니다."},
    {"category": "회사 일반", "question": "회사의 근무지는 본사 외에도 다른 지역에 있나요?", "answer": "현재는 서울 본사 한 곳에서만 운영되며, 재택/하이브리드 근무는 부서별로 다르게 적용됩니다."},

    {"category": "조직문화", "question": "사내 커뮤니케이션 방식은 어떤 편인가요?", "answer": "협업툴로 슬랙과 노션을 활용하며, 수평적인 분위기에서 의견 교환이 활발합니다."},
    {"category": "조직문화", "question": "상사나 동료와의 관계는 어떤가요?", "answer": "대부분 팀장급 이상도 닉네임이나 영어이름을 사용하며, 자유롭게 피드백을 주고받는 문화입니다."},
    {"category": "조직문화", "question": "사내 교육은 어떻게 운영되나요?", "answer": "입사 초기 온보딩 교육, 분기별 직무 역량 향상 교육과 외부 위탁교육 등이 제공됩니다."},
    {"category": "조직문화", "question": "신입사원을 위한 멘토링 제도나 OJT가 있나요?", "answer": "부서별 멘토가 배정되며, 1~3개월간 OJT를 통해 업무를 단계별로 배우게 됩니다."},
    {"category": "조직문화", "question": "회식이나 사내 행사 분위기는 어떤가요?", "answer": "강제성 없는 자율 참여 중심이며, 분기마다 워크샵이나 리프레시 프로그램도 진행됩니다."},

    {"category": "인사제도", "question": "평가 제도는 어떻게 운영되나요?", "answer": "분기별 OKR 기반 성과 평가와 직무/역량 평가가 병행되며, 직속 상사와의 면담도 포함됩니다."},
    {"category": "인사제도", "question": "승진은 어떤 기준으로 이뤄지나요?", "answer": "근속연수보다는 직무성과와 리더십 역량을 종합 반영하며, 승진 심사는 연 1회 실시됩니다."},
    {"category": "인사제도", "question": "개인의 목표설정이나 OKR은 자유롭게 설정하나요?", "answer": "부서 목표를 기준으로 자율적으로 설정하되, 팀장과의 사전 협의가 필요합니다."},
    {"category": "인사제도", "question": "연봉협상은 어떤 방식으로 진행되나요?", "answer": "연 1회 성과평가와 회사 전체 실적을 기반으로 조정되며, PI나 PS 형태의 인센티브도 있습니다."},
    {"category": "인사제도", "question": "부서 간 이동이나 직무 전환 기회도 주어지나요?", "answer": "연 1회 내부 희망 전환 신청이 가능하고, 필요 시 인사팀 주도로 순환보직도 검토됩니다."},

    {"category": "복리후생", "question": "식대나 교통비는 지원되나요?", "answer": "중식은 구내식당 이용이 가능하며, 외부 이용 시 월 10만 원 한도로 식대가 지원됩니다. 교통비는 별도 지원되지 않습니다."},
    {"category": "복리후생", "question": "연차 외에 특별휴가 제도가 있나요?", "answer": "경조사, 생일, 리프레시 휴가 등이 있으며, 근속 3년부터는 포상휴가도 주어집니다."},
    {"category": "복리후생", "question": "재택근무나 유연근무제도 운영 중인가요?", "answer": "일부 부서에 한해 주 1~2회 재택근무가 가능하고, 시차 출퇴근제도도 도입 중입니다."},
    {"category": "복리후생", "question": "자기계발비나 교육비는 지원되나요?", "answer": "자격증 취득비와 외부교육비를 연간 50만 원까지 지원하고 있으며, 신청 절차는 간단합니다."},
    {"category": "복리후생", "question": "건강검진이나 의료 관련 복지는 어떻게 되나요?", "answer": "매년 전 임직원 대상 건강검진이 제공되며, 간단한 심리상담 및 헬스케어 앱 연계 서비스도 지원됩니다."}
]

# 질문 출력
st.title("💬 질문을 선택하고 답변을 확인하세요")


if menu == "Q&A":
    st.header("📮 Q&A 문의 접수")
    with st.form("qa_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("성함")
            org = st.text_input("소속")
            career = st.text_input("경력")
        with col2:
            email = st.text_input("회신 받을 이메일 주소")
            phone = st.text_input("연락처")

        question = st.text_area("문의하실 질문 내용을 작성해주세요", height=200)
        submitted = st.form_submit_button("제출")
        if submitted:
            st.success("문의가 접수되었습니다. 확인 후 회신드리겠습니다.")

elif menu == "커피챗":
    st.header("☕ 커피챗 신청서")
    with st.form("coffee_form"):
        name = st.text_input("성함")
        phone = st.text_input("연락처")
        dept = st.text_input("희망 지원 부문 또는 관심 분야")
        resume = st.file_uploader("포트폴리오 또는 이력서를 첨부해주세요", type=["pdf", "docx", "pptx"])
        submitted = st.form_submit_button("신청")
        if submitted:
            st.success("신청이 완료되었습니다. 검토 후 연락드리겠습니다.")

# 관리자 전용 방문기록 차트
elif menu == "방문 통계":
    st.header("📊 방문자 통계 열람")

    pw = st.text_input("🔐 관리자 비밀번호 입력", type="password", help="승인된 관리자만 열람 가능합니다.")
    if pw != "t1234":
        st.markdown("<span style='color:gray; font-size:14px;'>관리자 권한이 필요합니다. 비밀번호를 입력해주세요.</span>", unsafe_allow_html=True)
        st.stop()

    if os.path.exists("visitors.csv"):
        df = pd.read_csv("visitors.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date
        df["week"] = df["timestamp"].dt.to_period("W").astype(str)
        df["month"] = df["timestamp"].dt.to_period("M").astype(str)

        st.subheader("일별 방문자 수")
        daily = df.groupby("date").size().reset_index(name="방문자 수")
        st.line_chart(daily.set_index("date"))

        st.subheader("주간 방문자 수")
        weekly = df.groupby("week").size().reset_index(name="방문자 수")
        st.bar_chart(weekly.set_index("week"))

        st.subheader("월간 방문자 수")
        monthly = df.groupby("month").size().reset_index(name="방문자 수")
        st.bar_chart(monthly.set_index("month"))

        st.subheader("전체 방문 기록")
        st.dataframe(df)
    else:
        st.info("방문자 기록이 아직 없습니다.")
