# 📄 CV Reviewer Copilot

An AI-powered tool that analyzes a resume against a job description and provides detailed feedback on alignment, strengths, and areas for improvement — all through a clean Streamlit interface.

---

## 🚀 Features

- 🧠 Uses Hugging Face Transformers (`flan-t5-base`) for intelligent feedback
- 📄 Accepts `.pdf` and `.txt` resumes
- 📌 Upload job descriptions in `.txt` format
- ⚡ Lightweight UI powered by Streamlit
- 🔒 API key management via `.env`

---

## 🏗️ Project Structure

cv-reviewer-copilot/
│
├── app.py # Main Streamlit app
├── utils/
│ ├── file_extractors.py # Resume/job description text parsers
│ └── model_runner.py # Model loading and analysis logic
├── sample_data/
│ ├── resume.pdf
│ └── sample_job.txt
├── .env # Your Hugging Face API key
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cv-reviewer-copilot.git
cd cv-reviewer-copilot
2. Set Up a Virtual Environment
bash
Copy code
python -m venv .venv
# Activate the environment
# For Windows:
.venv\Scripts\activate
# For macOS/Linux:
source .venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Add Your API Key
Create a .env file in the root directory:

ini
Copy code
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
5. Run the App
bash
Copy code
streamlit run app.py
🧠 Model
This project uses:

google/flan-t5-base: A powerful language model from Hugging Face's model hub.

Model downloading is automatic on first run.

🧪 Usage Instructions
Upload a resume (.pdf or .txt)

Upload a job description (.txt)

Click 🔍 Analyze Resume

You'll receive structured feedback highlighting:

✅ Strengths

⚠️ Suggestions for improvement

🔁 Resume-job alignment

✅ Example Output
vbnet
Copy code
✅ Strengths:
- Strong experience in data analysis
- Proficient in Python, SQL, and forecasting models

⚠️ Suggestions:
- Resume doesn't mention project management skills listed in the job description
- Consider tailoring technical terminology to match the job post
📌 Notes
Ensure resume and job description are clear, specific, and well-formatted for best results.

You can extend support for .docx or other formats inside file_extractors.py.

Currently uses flan-t5-base. You can experiment with larger or domain-specific models by updating model_runner.py.

🛠️ Future Enhancements
📊 Add scoring system for resume-job match

🔗 LinkedIn integration

🗂️ Save user feedback sessions

🧠 Fine-tune model for resume screening

📎 License
This project is under the MIT License. See LICENSE for details.