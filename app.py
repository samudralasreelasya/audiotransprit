# ==========================================================
# GEMINI AUDIO TRANSCRIPTION (SAFE VERSION)
# ==========================================================

import os
import gradio as gr
from google import genai

# ==========================================================
# LOAD API KEY
# ==========================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("⚠️ GEMINI_API_KEY not set!")

client = genai.Client(api_key=API_KEY)

# ==========================================================
# TRANSCRIBE FUNCTION
# ==========================================================

def transcribe(audio_path):

    if not audio_path:
        return "❌ Please record some audio."

    if not API_KEY:
        return "❌ API key missing. Set GEMINI_API_KEY."

    try:
        # Upload audio file
        audio_file = client.files.upload(file=audio_path)

        # Generate transcription
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                "Transcribe this audio exactly as spoken. Do not summarize. Include punctuation.",
                audio_file,
            ],
        )

        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"

# ==========================================================
# GRADIO UI
# ==========================================================

with gr.Blocks(title="Gemini Audio Transcription") as demo:

    gr.Markdown("## 🎤 Audio Transcription with Gemini")
    gr.Markdown("Record your voice and get exact transcription")

    audio = gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="🎙️ Record Your Voice"
    )

    output = gr.Textbox(
        label="📝 Transcript",
        lines=10
    )

    btn = gr.Button("🚀 Transcribe")

    btn.click(
        fn=transcribe,
        inputs=[audio],
        outputs=[output]
    )

# ==========================================================
# LAUNCH
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
