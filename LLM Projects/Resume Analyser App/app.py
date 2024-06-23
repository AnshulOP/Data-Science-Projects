import base64
import io
from dotenv import load_dotenv
import streamlit as st
import os
import pdf2image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def gemini_response(input, resume_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, resume_content[0], prompt])
    return response.text

def input_doc_pdf(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit Application
st.set_page_config(page_title="Resume Analyzer and Reviewer", page_icon="/Users/aizen/Desktop/Resume Analyzer using LLMs/Resume.jpeg")
st.title("Resume Tracker and Reviewer")

# Job Description Input
st.sidebar.subheader("Job Description")
input_text = st.sidebar.text_area("Enter Job Description", key="input")

# Resume Upload
st.sidebar.subheader("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Upload your Resume file (Only PDF files accepted)", type=["pdf"])

if uploaded_file is not None:
    st.sidebar.write("Resume Uploaded Successfully")

# Buttons for Different Actions
with st.sidebar:
    st.subheader("Actions")
    submit_1 = st.button(" Percentage Match with Job Description")
    submit_2 = st.button(" In-Depth Review with Skill Gap Analysis")
    submit_3 = st.button(" Enhanced Spell Check with Contextual Analysis")
    submit_5 = st.button(" How to improvise the Resume for Job Description")

# Input Prompts
input_prompts = {
    " Percentage Match with Job Description": """
        You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of complete ATS functionality along with technical fields like Data Science, Machine Learning, Cloud Engineering, DevOps, MLOps, Software Development, Data Analyst, Business Analyst, Business Consultant, Big Data Engineer, Full Stack Web Development, AI Engineer, UX-UI Designer, Networking Systems. 
        Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. First the output should come as percentage and then Missing Keywords or skills that the job description requires but are not available in the candidate's resume that should be included.
    """,
    " In-Depth Review with Skill Gap Analysis": """
        You are a seasoned HR professional with a keen eye for detail and a talent for spotting potential.  Provide a comprehensive evaluation of the resume based on the job description.

        **Step 1: Strengths & Weaknesses:**
            - Identify the candidate's strengths based on their skills and experience mentioned in the resume.
            - Analyze the candidate's weaknesses compared to the specific requirements  mentioned in the job description.

        **Step 2: Skill Gap Analysis:**
            - Identify any skill gaps between the candidate's skills and the essential skills required for the job description.
            - For each skill gap, explain the importance of the skill in the context of the job description and suggest ways the candidate can potentially address the gap (e.g., relevant courses, certifications, or projects).  

        **Step 3: Actionable Recommendations:**
            - Provide specific and actionable recommendations on how the candidate can tailor their resume to better highlight their relevant skills and experience for the specific job.

        **Output:**
            -  Present a detailed report with the following information:
                - Summary of the candidate's strengths aligned with the job description.
                - Analysis of the candidate's weaknesses compared to the job requirements.
                - Skill gap analysis identifying missing essential skills and suggestions for improvement.
                - Actionable recommendations for resume tailoring to target the job description. 
    """,
    " Enhanced Spell Check with Contextual Analysis": """
        You are a meticulous proofreader with a superpower for spotting typos and a keen eye for context.  Analyze the resume for any spelling or grammatical errors.

        **Step 1: Error Detection:**
            - Identify any potential spelling errors, grammatical mistakes, or typos in the resume.

        **Step 2: Contextual Analysis:**
            - Analyze the identified errors within the context of the sentence to determine the most likely correction.
            - Consider synonyms and related words to suggest alternative phrasings that might improve clarity and professionalism.

        **Step 3: Overall Accuracy:**
            - Calculate the overall accuracy score for the resume based on the number of errors identified and the resume length.

        **Output:**
            - Provide a detailed spell check report with the following information:
                - List of identified spelling or grammatical errors with suggested corrections based on context.
                - Overall accuracy score for the resume.
                - Suggestions for improving clarity and professionalism of the resume language.
    """,
    " How to improvise the Resume for Job Description": """
        You are a resume strategist with a talent for aligning candidate profiles with desired job requirements. Analyze the resume and the job description. 

        **Step 1: Skill Gap Analysis:**
            - Identify any skill gaps between the candidate's skills and the essential skills required for the job description.

        **Step 2: Targeted Resume Revamp:**
            - Provide a step-by-step guide on how to strategically revamp the resume to  better match the  job description. Consider  
            -  Adding relevant keywords and action verbs  aligned with the job description.
            - Highlighting transferable skills from previous experience that demonstrate potential for the role.
            - Quantifying achievements with metrics to showcase the impact of the candidate's work.
            - Tailoring the content of each section  to resonate  with the specific requirements  of the job description.

        **Step 3: Actionable Recommendations:**
            - Offer concrete and actionable recommendations for revising the resume content, structure, and formatting to make it a stronger match for the job description.

        **Output:**
            -  Present a strategic revamp guide with the following information:
                -  Analysis of skill gaps identified between the candidate's skills and the job description requirements.
                -  Step-by-step instructions on how to  revamp the resume for a better match with the job description.
                -  Specific recommendations for adding relevant keywords, highlighting transferable skills, quantifying achievements, and tailoring content to the job description. 
    """
}

# Action based on button click
if submit_1:
    if uploaded_file is not None:
        resume_content = input_doc_pdf(uploaded_file)
        response = gemini_response(input_prompts[" Percentage Match with Job Description"], resume_content, input_text)
        st.subheader("Response : ")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit_2:
    if uploaded_file is not None:
        resume_content = input_doc_pdf(uploaded_file)
        response = gemini_response(input_prompts[" In-Depth Review with Skill Gap Analysis"], resume_content, input_text)
        st.subheader("Response : ")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit_3:
    if uploaded_file is not None:
        resume_content = input_doc_pdf(uploaded_file)
        response = gemini_response(input_prompts[" Enhanced Spell Check with Contextual Analysis"], resume_content, input_text)
        st.subheader("Response : ")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit_5:
    if uploaded_file is not None:
        resume_content = input_doc_pdf(uploaded_file)
        response = gemini_response(input_prompts[" How to improvise the Resume for Job Description"], resume_content, input_text)
        st.subheader("Response : ")
        st.write(response)
    else:
        st.write("Please upload the resume")
