# CV Reviewer Copilot

A lightweight, locally-run AI-powered copilot to help you review resumes and job descriptions using natural language.

## 🚀 What It Does

This tool allows you to:

- Summarize resumes or job descriptions
- Check alignment between a CV and a job description
- Ask natural-language questions like:
  - “Does this CV show leadership experience?”
  - “What are the candidate’s strengths and weaknesses?”
  - “Is this CV suitable for the role of a product manager?”

It uses a fine-tuned version of Google's `flan-t5-small` model from Hugging Face to run efficiently on machines with 8GB RAM and no dedicated GPU.

## 🔧 Features

- Runs completely offline (no API keys or cloud services needed)
- Designed for local use in Jupyter Notebook or Python script
- Compatible with modest hardware (8GB RAM or more)
- Preloaded with prompt templates for structured querying
## 🛠️ Tools and Technologies Used

- **Python**
- **Hugging Face Transformers** – For loading and interacting with the `flan-t5-small` model  
- **Hugging Face Datasets** – For quick testing and examples (optional)
- **PyTorch** – Backend for running the model (compatible with CPU)
- **Jupyter Notebook** – For interactive use and testing
- **Textwrap & Utils** – For formatting and display enhancements
- 
## 📁 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/cv-reviewer-copilot.git
   cd cv-reviewer-copilot
