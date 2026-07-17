
# Gemini Audio Transcription

A lightweight Gradio web application that uses the Google Gemini 2.5 Flash model to transcribe recorded audio exactly as spoken.

## Prerequisites

- Python 3.10 or higher
- A Google Gemini API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application requires an environment variable named `GEMINI_API_KEY`. 

### Linux/macOS
```bash
export GEMINI_API_KEY="your_actual_api_key_here"
```

### Windows (Command Prompt)
```cmd
set GEMINI_API_KEY=your_actual_api_key_here
```

### Windows (PowerShell)
```powershell
\$env:GEMINI_API_KEY="your_actual_api_key_here"
```

## Running the Application

Start the web server by running the script:
```bash
python app.py
```

Open your browser and navigate to `http://localhost:7860` to access the interface.

## Deployment

This application reads the `PORT` environment variable and binds to `0.0.0.0`, making it fully compatible with cloud hosting platforms like Hugging Face Spaces, Render, or Railway.
