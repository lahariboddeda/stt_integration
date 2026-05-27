from flask import Blueprint, request, jsonify

from services.stt_service import transcribe_audio
from validators.transcript_validator import validate_transcript
from utils.file_handler import allowed_file, save_audio_file

transcript_bp = Blueprint("transcript_bp", __name__)

@transcript_bp.route("/transcribe", methods=["POST"])
def transcribe():

    # Check audio exists
    if "audio" not in request.files:
        return jsonify({
            "success": False,
            "error": "No audio file uploaded"
        }), 400

    audio = request.files["audio"]

    # Check filename
    if audio.filename == "":
        return jsonify({
            "success": False,
            "error": "Empty filename"
        }), 400

    # Check valid extension
    if not allowed_file(audio.filename):
        return jsonify({
            "success": False,
            "error": "Unsupported file type"
        }), 400

    # Save file
    file_path = save_audio_file(audio)

    # Send to Whisper
    stt_result = transcribe_audio(file_path)

    if not stt_result["success"]:
        return jsonify({
            "success": False,
            "error": stt_result["error"]
        }), 500

    transcript = stt_result["transcript"]

    # Validate transcript
    is_valid, message = validate_transcript(transcript)

    if not is_valid:
        return jsonify({
            "success": False,
            "error": message
        }), 400

    return jsonify({
        "success": True,
        "transcript": transcript
    }), 200