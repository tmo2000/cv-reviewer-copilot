import streamlit as st 
# from utils.file_extractors import extract_text_from_txt, extract_text_from_pdf
from utils.model_runner import load_model, analyze_resume

st.set_page_config(
    page_title="Resume Reviewer",
    page_icon=":file_folder:",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("Resume Reviewer")
st.markdown("""
    This app reviews resumes against job descriptions using a Hugging Face model. \n
    Upload a job description in TXT format and your resume in PDF formalt to get started.
""")

resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_desc_file = st.file_uploader("Upload job description (TXT)", type=["txt"])

@st.cache_resource
def get_model():
    return load_model()

model, tokenizer = get_model()

if st.button("Analyze Resume"):
    if not resume_file or not job_desc_file:
        st.warning("Please upload both a resume and a job description.")
    else:
         with st.spinner("Analyzing..."):
            try:
                feedback = analyze_resume(resume_file, job_desc_file, model, tokenizer)
                st.success("✅ Analysis Complete!")
                st.markdown("### 📝 Feedback")
                st.write(feedback)
            except Exception as e:
                st.error(f"Something went wrong: {e}")