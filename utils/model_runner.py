from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.file_extractors import extract_text_from_txt, extract_text_from_pdf, clean_text  # if clean_text is in a separate file

def load_model():

    model_name = "google/flan-t5-base"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    print("Model and tokenizer loaded successfully.")

    return model, tokenizer

    
def analyze_resume(uploaded_file, uploaded_jd, model, tokenizer):
    # Extract and clean resume
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        raise ValueError("Unsupported resume format")

    # Extract and clean job description
    if uploaded_jd.name.endswith(".txt"):
        job_description = uploaded_jd.read().decode("utf-8")
    else:
        raise ValueError("Only .txt job descriptions are supported.")
    
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    # Prompt
    prompt = f"""
You are a career coach. Read the Job Description and Resume below.

Job Description = 
{job_description}

Resume:
{resume_text}

Example:
Eligibility: Eligible
Tips:
- Add more experience with Flask framework.
- Highlight AWS projects more clearly.
- Include specific Python version expertise.

Now do the same for the given inputs:

Eligibility:

   """ 

    # Inference
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model.generate(**inputs, max_new_tokens=256)
    feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return feedback