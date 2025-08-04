# Bachelorthesis-LLM-Triage
This repository contains the code and documentation for my Bachelor thesis project: an LLM-powered conversational interface designed to improve patient self-assessment in healthcare settings using the Manchester Triage System.

## Technical Architecture

- **Frontend**: HTML, CSS, JavaScript with WebRTC for real-time communication
- **Backend**: Python Flask web server
- **AI Model**: OpenAI GPT-4 Realtime API
- **Communication**: WebRTC for audio streams and data channels for text

## Project Structure

```
├── app.py                 # Flask backend server
├── static/
│   ├── styles.css        # Frontend styling
│   └── images/           # UI icons and flags
├── templates/
│   └── index.html        # Main application interface
├── README.md
└── .env                  # Environment variables (create this)
```

## Prerequisites

- Python 3.x
- Flask
- OpenAI API key
- Modern web browser with WebRTC support
- Microphone access (optional, for voice input)

## Research Context
This system was developed as part of a Human-Centered Design (HCD) approach to investigate how LLM-based conversational interfaces can enhance usability in patient self-assessment compared to traditional rule-based systems.

### Research Question
Does an LLM-based conversational interface enhance usability over hardcoded Q&A systems?

⚠️ **Important**: This is a research prototype and should not be used for actual medical triage.
