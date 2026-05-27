# STT Integration Layer

A backend Speech-to-Text (STT) integration project developed using Flask and OpenAI Whisper. This project allows users to upload audio files through REST APIs and converts speech into text transcripts.

---

# Features

- Audio file upload support
- Speech-to-Text conversion using OpenAI Whisper
- Transcript validation
- Error handling for invalid files and transcripts
- REST API integration
- Secure file handling

---

# Technologies Used

- Python 3.10
- Flask
- OpenAI Whisper
- PyTorch (Torch)
- Werkzeug
- FFmpeg
- Postman

---

# Project Structure

```bash
stt-integration/
│
├── app.py
├── requirements.txt
│
├── routes/
│   └── transcript_routes.py
│
├── services/
│   └── stt_service.py
│
├── validators/
│   └── transcript_validator.py
│
├── utils/
│   └── file_handler.py
│
├── uploads/
│
└── README.md

#Installation

Clone Repository
git clone "https://github.com/lahariboddeda/stt_integration"
cd stt-integration
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Requirements
pip install -r requirements.txt
Install FFmpeg

Download and install FFmpeg:

https://ffmpeg.org/download.html

Add FFmpeg to system environment variables.

#Verify installation:

ffmpeg -version
Run the Project
python app.py

#Server runs at:

http://127.0.0.1:5000
API Endpoint
Transcribe Audio
Endpoint
POST /transcribe
Request Type
form-data
Key	Type	Value
audio	File	Audio File
Successful Response
{
  "success": true,
  "transcript": "Hello how are you"
}
Error Responses
Unsupported File
{
  "success": false,
  "error": "Unsupported file type"
}
Empty Transcript
{
  "success": false,
  "error": "Transcript is empty"
}

#Workflow

Audio Upload
↓
API Request
↓
File Validation
↓
Whisper Processing
↓
Transcript Generation
↓
Validation
↓
JSON Response

#Challenges Faced
Unsupported audio formats
Invalid transcript outputs
Whisper runtime errors
Dependency compatibility issues
FFmpeg configuration problems
Solutions Implemented
File format validation
Transcript validation handlers
Exception handling
Secure file upload handling
Compatible Python and Torch versions
Python & Torch Versions
Python Version: 3.10
Torch Version: Compatible with Python 3.10
Testing

API testing was performed using Postman for:

Audio uploads
Transcript generation
Validation testing
Error response testing
