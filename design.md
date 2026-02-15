# CommunityConnect AI Design

## System Architecture

The system uses Streamlit as frontend and HuggingFace AI models for processing.

Flow:

User → Streamlit Interface → Processing → AI Models → Response

## Components

Frontend:
- Streamlit

Backend:
- Python

AI Models:
- Translation model (English-Hindi)
- Summarization model
- Whisper speech-to-text
- gTTS text-to-speech

Data:
- Local FAQ file (faqs.json)

## Working Flow

1. User inputs text or voice
2. Voice converted to text using Whisper
3. Query searched in FAQ database
4. Answer summarized
5. Answer translated
6. Voice generated
7. Response displayed
