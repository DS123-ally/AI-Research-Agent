import streamlit as st
from graph import graph
from pdf_generator import save_as_pdf

# Page config
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput > div > div > input {
    border-radius: 12px;
    padding: 12px;
}

.stButton {
    display: flex;
    justify-content: flex-start;
    margin-top: 15px;
}

.stButton > button {
    width: 220px;
    height: 52px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #4F46E5, #06B6D4);
    color: white;
    border: none;
}

.report-box {
    background: #1E293B;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #60A5FA;
}

.subtitle {
    text-align: center;
    color: #CBD5E1;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🤖 AI Research Agent</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Generate professional AI-powered research reports instantly</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION ----------------
st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([1, 6, 1])

with center:
    st.markdown("### 🔍 Enter Research Topic")

    topic = st.text_input(
        "",
        placeholder="Enter your topic (e.g. Artificial Intelligence in Healthcare)",
        label_visibility="collapsed"
    )

    # Button on left bottom side
    generate = st.button("🚀 Generate Report")

# Generate report
if generate:

    if not topic.strip():
        st.warning("Please enter a research topic")

    else:
        with st.spinner("Researching and generating report..."):

            result = graph.invoke({
                "topic": topic,
                "queries": [],
                "results": [],
                "final_report": ""
            })

            report = result["final_report"]

        st.success("✅ Report Generated Successfully!")

        # Report Display
        st.markdown("## 📄 Research Report")

        st.markdown(
            f'<div class="report-box">{report}</div>',
            unsafe_allow_html=True
        )

        # PDF
        pdf_file = save_as_pdf(report)

        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name="AI_Research_Report.pdf",
                mime="application/pdf"
            )

# Sidebar
st.sidebar.title("⚡ Features")
st.sidebar.markdown("""
- AI-powered research  
- Real-time web search  
- Automated summarization  
- PDF export  
- Professional reports
""")

st.sidebar.info("Built with LangGraph + Streamlit")