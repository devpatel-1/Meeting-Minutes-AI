# 🎙️ Meeting Minutes AI

An AI-powered application that converts meeting recordings into clear, structured and professional meeting minutes.

## ✨ Features

- 🎙️ MP3 meeting recording upload
- 📝 Speech-to-text transcription using OpenAI
- 🤖 AI-powered meeting analysis
- 📋 Structured meeting minutes
- 🎯 Key decisions and action items
- 📄 Full transcript
- 🎨 Clean Gradio UI
- 🖼️ Custom logo and branding
- 💻 Runs locally without requiring a dedicated GPU

## 🧠 Workflow

```text
🎙️ MP3 Recording
       ↓
OpenAI gpt-4o-mini-transcribe
       ↓
📝 Full Transcript
       ↓
OpenAI GPT-4o-mini
       ↓
📋 Meeting Minutes

## 🖥️ Screenshots

### Application Interface

<img src="./screenshots/ss1.png" alt="Meeting Minutes AI" width="800"/>

### Meeting Recording Upload

<img src="./screenshots/ss2.png" alt="Upload Meeting Recording" width="800"/>

### Audio Transcription

<img src="./screenshots/ss3.png" alt="Audio Transcription" width="800"/>

### Generated Meeting Minutes

<img src="./screenshots/ss4.png" alt="Generated Meeting Minutes" width="800"/>

### Full Transcript

<img src="./screenshots/ss5.png" alt="Full Transcript" width="800"/>

🛠️ Tech Stack
Technology	Purpose
Python	Application development
Gradio	User interface
OpenAI API	AI processing
gpt-4o-mini-transcribe	Audio transcription
GPT-4o-mini	Meeting analysis
python-dotenv	Environment variables
🦙 Llama & Hugging Face Exploration

I also explored an alternative GPU-based architecture using:

Meta Llama 3.1 8B Instruct
Hugging Face Transformers
Hugging Face Hub
BitsAndBytes 4-bit quantization
PyTorch
GPU inference
Hugging Face ZeroGPU

The explored architecture:

MP3 Recording
      ↓
OpenAI Transcription
      ↓
Transcript
      ↓
Llama 3.1 8B Instruct
      ↓
BitsAndBytes 4-bit
      ↓
GPU Inference
      ↓
Meeting Minutes

Llama 3.1 8B requires suitable GPU resources for practical inference. BitsAndBytes 4-bit quantization reduces the model's memory footprint, making GPU-based inference more practical.

For the current version, OpenAI is used for meeting analysis so the complete application can run locally without requiring a dedicated GPU.

💻 Local Setup
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd meeting-minutes-ai
2. Create virtual environment
python3.11 -m venv .venv
3. Activate environment
source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Configure API Key

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
6. Run the application
python app.py

Open the Gradio URL shown in the terminal.

🔐 Security

API keys are stored using environment variables.

The .env file is excluded from Git using .gitignore.

Never commit API keys or other sensitive credentials to the repository.

📁 Project Structure
meeting-minutes-ai/
│
├── assets/
│   └── logo.png
│
├── screenshots/
│   ├── ss1.png
│   ├── ss2.png
│   ├── ss3.png
│   ├── ss4.png
│   └── ss5.png
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── meeting_analyzer.py
│   ├── prompts.py
│   ├── transcription.py
│   └── utils.py
│
├── ui/
│   ├── __init__.py
│   ├── styles.py
│   └── theme.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
🎯 Project Goal

The goal of Meeting Minutes AI is to simplify the process of turning long meeting recordings into useful documentation.

Instead of manually:

Listen to Recording
       ↓
Take Notes
       ↓
Review Recording
       ↓
Write Minutes
       ↓
Identify Action Items

the application provides:

Upload MP3
    ↓
AI Processing
    ↓
Meeting Minutes
🚀 Future Improvements
👥 Speaker identification
📄 PDF and DOCX export
📧 Email-ready summaries
💾 Meeting history
🔍 Search across meetings
🌐 Multi-language support
📅 Automatic meeting metadata extraction
👨‍💻 Author
Dev Patel

Made with ❤️ and passion.

Turn Conversations Into Clarity.