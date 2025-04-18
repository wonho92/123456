
from datetime import datetime
# 파일 저장 함수
def save_uploaded_file(uploaded_file):
    directory = "uploads"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

def save_submission(file, data):
    if not os.path.exists(file):
        df = pd.DataFrame(columns=data.keys())
    else:
        df = pd.read_csv(file)
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(file, index=False)




import streamlit as st
import pytz
from datetime import datetime

# 현재 시간 (대한민국 표준시) 표시
seoul_tz = pytz.timezone("Asia/Seoul")
now = seoul_tz.localize(datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

# 두 개의 컬럼 (로고 + 시간)
col1, col2 = st.columns([1, 4])  # ✅ 이 줄 꼭 필요

with col1:
    st.image("티사이언티픽로고(1538x582)_가로로 길게.png", width=180)

with col2:
    st.markdown(
        f"<div style='text-align:right; font-size:14px; color:gray;'>🕒 현재 시간: {now}</div>",
        unsafe_allow_html=True
    )



import pandas as pd
import pytz
from datetime import datetime
# 파일 저장 함수
def save_uploaded_file(uploaded_file):
    directory = "uploads"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path
import os
from datetime import datetime
# 파일 저장 함수
def save_uploaded_file(uploaded_file):
    directory = "uploads"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

# ✅ 안전한 CSS 배경 적용


# ✅ 방문자 수 추적 (최초 1회만)
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
    count = update_visitor_count()
    st.session_state["visited"] = True
else:
    count = pd.read_csv("visitors.csv").shape[0]

# ✅ 사이드바 메뉴
menu = st.sidebar.radio("메뉴를 선택하세요", [
    "원호정주식회사", 
    "회사제도안내-회사비전",
    "회사제도안내-근무제도",
    "회사제도안내-조직문화",
    "회사제도안내-평가보상", 
    "회사생활안내", 
    "커피챗", 
    "Q&A", 
    "관리자 전용"
])

if menu == "Tscientific":
    st.title("🎯 원호정주식회사에 오신 것을 환영합니다")
    st.write("좌측 메뉴를 클릭하여 제도안내, 회사생활, 문의 등을 확인하세요.")
st.sidebar.markdown("<br><br><span style='font-size:12px; color:gray'>🔐 관리자 전용 ➤ 방문 통계</span>", unsafe_allow_html=True)
st.sidebar.markdown(f"👁 방문자 수: {count}명")

# ✅ 질문 데이터
qa_data = [
    {'category': '회사제도안내-회사비전', 'question': '회사의 주요 사업 분야는 무엇인가요?', 'answer': '보안 솔루션 개발 및 시스템 구축, 그리고 모바일 커머스 서비스를 주력으로 하고 있습니다.'},
    {'category': '회사제도안내-회사비전', 'question': '회사의 비전이나 중장기 전략이 있다면 알려주세요.', 'answer': '기술 기반의 지속가능한 보안 생태계 구축을 목표로 하며, 글로벌 보안 시장 진출도 계획 중입니다.'},
    {'category': '회사제도안내-회사비전', 'question': '최근 1~2년간 주요 성과가 있다면 무엇인가요?', 'answer': '국내 대형 공공기관 대상 보안 솔루션 수주와 T사 파트너십을 통해 연 매출 400억 원을 돌파했습니다.'},
    {'category': '회사제도안내-근무제도', 'question': '회사의 근무지는 본사 외에도 다른 지역에 있나요?', 'answer': '현재는 서울 본사 한 곳에서만 운영되며, 재택/하이브리드 근무는 부서별로 다르게 적용됩니다.'},
    {'category': '회사제도안내-근무제도', 'question': '부서 간 이동이나 직무 전환 기회도 주어지나요?', 'answer': '연 1회 내부 희망 전환 신청이 가능하고, 필요 시 인사팀 주도로 순환보직도 검토됩니다.'},
    {'category': '회사제도안내-근무제도', 'question': '연차 외에 특별휴가 제도가 있나요?', 'answer': '경조사, 생일, 리프레시 휴가 등이 있으며, 근속 3년부터는 포상휴가도 주어집니다.'},
    {'category': '회사제도안내-근무제도', 'question': '재택근무나 유연근무제도 운영 중인가요?', 'answer': '일부 부서에 한해 주 1~2회 재택근무가 가능하고, 시차 출퇴근제도도 도입 중입니다.'},
    {'category': '회사제도안내-조직문화', 'question': '조직 규모는 어떻게 되나요?', 'answer': '현재 약 250명 정도의 임직원이 재직 중이며, R&D와 기술영업 인력이 절반 이상을 차지하고 있습니다.'},
    {'category': '회사제도안내-조직문화', 'question': '사내 커뮤니케이션 방식은 어떤 편인가요?', 'answer': '협업툴로 슬랙과 노션을 활용하며, 수평적인 분위기에서 의견 교환이 활발합니다.'},
    {'category': '회사제도안내-조직문화', 'question': '상사나 동료와의 관계는 어떤가요?', 'answer': '대부분 팀장급 이상도 닉네임이나 영어이름을 사용하며, 자유롭게 피드백을 주고받는 문화입니다.'},
    {'category': '회사제도안내-조직문화', 'question': '사내 교육은 어떻게 운영되나요?', 'answer': '입사 초기 온보딩 교육, 분기별 직무 역량 향상 교육과 외부 위탁교육 등이 제공됩니다.'},
    {'category': '회사제도안내-조직문화', 'question': '신입사원을 위한 멘토링 제도나 OJT가 있나요?', 'answer': '부서별 멘토가 배정되며, 1~3개월간 OJT를 통해 업무를 단계별로 배우게 됩니다.'},
    {'category': '회사제도안내-조직문화', 'question': '회식이나 사내 행사 분위기는 어떤가요?', 'answer': '강제성 없는 자율 참여 중심이며, 분기마다 워크샵이나 리프레시 프로그램도 진행됩니다.'},
    {'category': '회사제도안내-평가보상', 'question': '평가 제도는 어떻게 운영되나요?', 'answer': '분기별 OKR 기반 성과 평가와 직무/역량 평가가 병행되며, 직속 상사와의 면담도 포함됩니다.'},
    {'category': '회사제도안내-평가보상', 'question': '승진은 어떤 기준으로 이뤄지나요?', 'answer': '근속연수보다는 직무성과와 리더십 역량을 종합 반영하며, 승진 심사는 연 1회 실시됩니다.'},
    {'category': '회사제도안내-평가보상', 'question': '개인의 목표설정이나 OKR은 자유롭게 설정하나요?', 'answer': '부서 목표를 기준으로 자율적으로 설정하되, 팀장과의 사전 협의가 필요합니다.'},
    {'category': '회사제도안내-평가보상', 'question': '연봉협상은 어떤 방식으로 진행되나요?', 'answer': '연 1회 성과평가와 회사 전체 실적을 기반으로 조정되며, PI나 PS 형태의 인센티브도 있습니다.'},
    {'category': '회사제도안내-평가보상', 'question': '식대나 교통비는 지원되나요?', 'answer': '중식은 구내식당 이용이 가능하며, 외부 이용 시 월 10만 원 한도로 식대가 지원됩니다. 교통비는 별도 지원되지 않습니다.'},
    {'category': '회사제도안내-평가보상', 'question': '자기계발비나 교육비는 지원되나요?', 'answer': '자격증 취득비와 외부교육비를 연간 50만 원까지 지원하고 있으며, 신청 절차는 간단합니다.'},
    {'category': '회사제도안내-평가보상', 'question': '건강검진이나 의료 관련 복지는 어떻게 되나요?', 'answer': '매년 전 임직원 대상 건강검진이 제공되며, 간단한 심리상담 및 헬스케어 앱 연계 서비스도 지원됩니다.'},
    {'category': '회사생활안내', 'question': '업무 관련 비용을 어떻게 청구하나요?', 'answer': '비용 발생 후 법인카드 사용 내역 혹은 영수증을 첨부해 그룹웨어 경비청구서에 등록하면 됩니다.'},
    {'category': '회사생활안내', 'question': '개인 카드로 결제한 경우에도 청구가 가능한가요?', 'answer': '네, 선결제의 경우 담당자의 승인 후 영수증과 함께 청구하면 익월 급여일에 지급됩니다.'},
    {'category': '회사생활안내', 'question': '출장비는 어떤 기준으로 정산되나요?', 'answer': '교통비, 식비, 숙박비 항목별로 한도 내 실비 정산하며, 출장보고서 제출이 필수입니다.'},
    {'category': '회사생활안내', 'question': '법인카드는 언제부터 사용할 수 있나요?', 'answer': '부서장 승인 후 발급 가능하며, 신입사원의 경우 3개월 경과 후 개인별 지급됩니다.'},
    {'category': '회사생활안내', 'question': '경비청구 마감일은 언제인가요?', 'answer': '매월 말일 기준으로 익월 5영업일까지 등록해야 당월 급여에 반영됩니다.'},
    {'category': '회사생활안내', 'question': '연차는 언제부터 사용할 수 있나요?', 'answer': '입사일 기준 1개월 후부터 발생하며, 매달 1일씩 최대 11일까지 자동 생성됩니다.'},
    {'category': '회사생활안내', 'question': '반차나 시간 단위 연차도 사용 가능한가요?', 'answer': '반차는 가능하고, 시간 단위 연차는 사전 협의가 필요한 부서가 있습니다.'},
    {'category': '회사생활안내', 'question': '휴가는 어떻게 신청하나요?', 'answer': '그룹웨어에서 전자결재로 신청하며, 팀장 승인 후 휴가 캘린더에 자동 반영됩니다.'},
    {'category': '회사생활안내', 'question': '병가를 사용할 수 있는 기준은 어떻게 되나요?', 'answer': '유급 병가는 3일 이내의 경우 진단서 없이 가능하고, 4일 이상은 진단서 제출이 필요합니다.'},
    {'category': '회사생활안내', 'question': '지각이나 조퇴 처리 기준은 어떻게 되나요?', 'answer': '1시간 이내는 지각/조퇴로 처리되며, 누적 3회 시 연차 0.5일 차감됩니다.'},
    {'category': '회사생활안내', 'question': '그룹웨어 로그인은 어떻게 하나요?', 'answer': '입사 시 이메일로 안내된 임시 비밀번호로 로그인 후 비밀번호를 변경하시면 됩니다.'},
    {'category': '회사생활안내', 'question': '이메일 서명은 어떻게 설정하나요?', 'answer': '사내 표준 서식이 있으며, 그룹웨어 공지사항에서 서명 양식을 확인할 수 있습니다.'},
    {'category': '회사생활안내', 'question': '회의실 예약은 어떻게 하나요?', 'answer': '그룹웨어 일정관리 탭에서 회의실 선택 후 사용 시간을 등록하면 예약됩니다.'},
    {'category': '회사생활안내', 'question': '재택근무 신청은 어떤 방식으로 하나요?', 'answer': '부서장 사전 승인 후, 재택근무 신청서를 그룹웨어로 제출하면 승인됩니다.'},
    {'category': '회사생활안내', 'question': '노트북이나 장비를 추가로 요청할 수 있나요?', 'answer': '예, 장비 신청서를 작성해 IT팀에 요청하면 재고 확인 후 지급됩니다.'},
    {'category': '회사생활안내', 'question': '보고는 어떤 방식으로 하나요?', 'answer': '간단한 업무는 메신저/메일로, 정기적인 보고는 주간보고나 결재라인을 활용합니다.'},
    {'category': '회사생활안내', 'question': '회의록은 누구 책임인가요?', 'answer': '회의 주관자가 작성하며, 사내 문서 양식을 활용해 부서 공유폴더에 저장합니다.'},
    {'category': '회사생활안내', 'question': '업무 지시를 구두로 받았을 경우 어떻게 기록하나요?', 'answer': '메신저나 메일로 내용 정리 후 재확인을 요청하는 방식으로 정리하면 좋습니다.'},
    {'category': '회사생활안내', 'question': '복장 규정이 따로 있나요?', 'answer': '공식적인 복장은 없지만, 외부 미팅이 없는 날은 자유복장이 허용됩니다.'},
    {'category': '회사생활안내', 'question': '점심시간과 쉬는 시간은 어떻게 되나요?', 'answer': '점심은 12:00~13:00이며, 원호 기분분에 따라 탄력적으로 조정 가능합니다. 커피 타임 등은 자유롭게 운영됩니다.'},
]


# Q&A 폼
if menu == "Q&A":
    st.header("📮 Q&A 문의 접수")
    with st.form("qa_form"):
        name = st.text_input("성함")
        org = st.text_input("소속")
        career = st.text_input("경력")
        email = st.text_input("회신받을 이메일")
        phone = st.text_input("연락처")
        question = st.text_area("문의하실 질문", height=150)
        submitted = st.form_submit_button("제출")
        if submitted:
            save_submission("qa_submissions.csv", {
                "name": name,
                "org": org,
                "career": career,
                "email": email,
                "phone": phone,
                "question": question
            })
            st.success("✅ Q&A 문의가 정상적으로 제출되었습니다.")
            st.experimental_rerun()
    st.experimental_rerun()
    save_submission("qa_submissions.csv", {
                "name": name,
                "org": org,
                "career": career,
                "email": email,
                "phone": phone,
                "question": question
            })
    pass

# 커피챗 폼
elif menu == "커피챗":
    st.header("☕ 커피챗 신청")
    with st.form("coffee_form"):
        name = st.text_input("성함")
        phone = st.text_input("연락처")
        dept = st.text_input("관심 있는 부문 또는 희망 지원 부서")
        resume = st.file_uploader("이력서/포트폴리오 첨부", type=["pdf", "docx"])
        submitted = st.form_submit_button("신청")
        if submitted:
            save_submission("coffee_submissions.csv", {
                "name": name,
                "phone": phone,
                "dept": dept,
                "resume_uploaded": resume.name if resume else "미첨부",
                "resume_path": save_uploaded_file(resume) if resume else ""
            })
            st.success("✅ 커피챗 신청이 정상적으로 제출되었습니다.")
            st.experimental_rerun()
    st.experimental_rerun()
    save_submission("coffee_submissions.csv", {
                "name": name,
                "phone": phone,
                "dept": dept,
                "resume_uploaded": resume.name if resume else "미첨부", "resume_path": save_uploaded_file(resume) if resume else ""
            })
    pass

# Q&A 표시
elif any(menu == q["category"] for q in qa_data):
    st.header(f"📘 {menu}")
    for qa in qa_data:
        if qa["category"] == menu:
            with st.expander("💬 " + qa["question"]):
                st.write(qa["answer"])

    pass

# 관리자 통계
elif menu == "관리자 전용":
    st.header("📊 방문자 통계")
    pw = st.text_input("관리자 비밀번호", type="password")
    if pw != "t1234":
        st.warning("비밀번호가 올바르지 않습니다.")
        st.stop()

    if os.path.exists("visitors.csv"):
        df = pd.read_csv("visitors.csv")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date
        df["week"] = df["timestamp"].dt.to_period("W").astype(str)
        df["month"] = df["timestamp"].dt.to_period("M").astype(str)

        st.subheader("일별 방문자 수")
        st.line_chart(df.groupby("date").size())

        st.subheader("주간 방문자 수")
        st.bar_chart(df.groupby("week").size())

        st.subheader("월간 방문자 수")
        st.bar_chart(df.groupby("month").size())

        st.dataframe(df)
    else:
        st.info("방문 기록이 아직 없습니다.")

    st.subheader("📮 Q&A 제출내역")
    if os.path.exists("qa_submissions.csv"):
        df_qa = pd.read_csv("qa_submissions.csv")
        st.dataframe(df_qa)
    else:
        st.info("Q&A 제출 기록이 없습니다.")

    st.subheader("☕ 커피챗 신청내역")
    if os.path.exists("coffee_submissions.csv"):
        df_coffee = pd.read_csv("coffee_submissions.csv")
        st.dataframe(df_coffee)

        st.markdown("### 📎 첨부파일 다운로드")
        download_dir = st.text_input("첨부파일을 저장할 로컬 경로를 입력하세요 (예: C:/Users/Downloads)", value="downloads")

        for i, row in df_coffee.iterrows():
            if pd.notna(row.get("resume_path")) and os.path.exists(row["resume_path"]):
                with open(row["resume_path"], "rb") as file:
                    st.download_button(
                        label=f"📄 {row['name']} - 첨부파일 다운로드",
                        data=file.read(),
                        file_name=row["resume_uploaded"],
                        mime="application/octet-stream"
                    )
    else:
        st.info("커피챗 신청 기록이 없습니다.")

        st.markdown("### 📎 첨부파일 다운로드")
        for i, row in df_coffee.iterrows():
            if pd.notna(row.get("resume_path")) and os.path.exists(row["resume_path"]):
                with open(row["resume_path"], "rb") as file:
                    st.download_button(
                        label=f"📄 {row['name']} - 첨부파일 다운로드",
                        data=file.read(),
                        file_name=row["resume_uploaded"],
                        mime="application/octet-stream"
                    )

