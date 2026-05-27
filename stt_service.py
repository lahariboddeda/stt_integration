import whisper

# Load whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_path):

    try:
        result = model.transcribe(audio_path)

        transcript = result["text"]

        return {
            "success": True,
            "transcript": transcript
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }