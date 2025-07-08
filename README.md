# 🤖 CV Reviewer Copilot

A Streamlit-powered AI tool that helps job seekers analyze and tailor their resumes for specific job descriptions. Upload a resume and a job description — get back feedback and improvement suggestions, powered by a language model.

---

## 🚀 Features

- 📄 Upload resume (PDF or DOCX)
- 📝 Upload job description (TXT only)
- 🔍 AI-powered analysis using a transformer model
- 💡 Actionable resume tailoring tips
- 🖥️ Simple and intuitive Streamlit UI

---

## 🧠 Model

The app currently uses Hugging Face's [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small) model for inference. You can upgrade to a more powerful model like `flan-t5-base` or `flan-t5-large` by changing the model name in `model_runner.py`.

To use Hugging Face-hosted models, add your Hugging Face API key to a `.env` file:


## 🛠️ Installation
1. Clone the repository:

git clone https://github.com/yourusername/cv-reviewer-copilot.git
cd cv-reviewer-copilot

2. Set up a virtual environment:
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create .env file with your Hugging Face token:
echo HUGGINGFACE_API_KEY=your_token_here > .env

## 🏃 Running the App

Run the app with Streamlit:
streamlit run app.py

## 📁 File Structure
cv-reviewer-copilot/
│
├── app.py                    # Streamlit frontend
├── utils/
│   ├── model_runner.py       # Model loading and analysis logic
│   └── file_extractors.py    # File reading and cleaning functions
├── sample_data/              # Example resume and job description
├── .env                      # API key (not committed)
├── requirements.txt
└── README.md

## ✅ To-Do
 Improve feedback quality using more powerful models (e.g., FLAN-T5 Base or GPT)

 Add keyword matching and ATS score simulation

 Support job description in PDF format

 Enable saving feedback reports



