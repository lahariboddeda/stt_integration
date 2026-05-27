from flask import Flask
from routes.transcript_routes import transcript_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(transcript_bp)

if __name__ == "__main__":
    app.run(debug=True)