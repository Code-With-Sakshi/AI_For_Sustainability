# AI_For_Sustainability


# 🌱 SaathiAI

SaathiAI is an AI-powered sustainability assistant designed to make sustainability guidance simple, accessible, and easy to use.

## Problem
Many people want to adopt sustainable practices but may not know what action to take. Sustainability information is often scattered across different sources, while existing digital tools can be difficult for users with limited technical or app-literacy.

SaathiAI reduces this effort by providing simple, context-based sustainability guidance through text, voice, and image inputs.

## Solution
**User Input → AI Understanding → Agent Logic → RAG / Image Analysis → Personalized Response**

SaathiAI can:
- Understand sustainability questions
- Accept voice input
- Analyze uploaded images
- Retrieve information from a trusted knowledge base using RAG
- Generate simple, actionable responses
- Route requests through an agentic workflow

## AI Elements
- **RAG:** Retrieves relevant information from a trusted sustainability knowledge base.
- **Agentic AI:** Decides whether to answer, retrieve knowledge, or analyze an image.
- **IBM Granite:** Language-model component for understanding and response generation.

## Target Users
Students, households, local communities, campus users, and people with limited technical or app-literacy.

## Technologies
Python, Streamlit, IBM Granite / IBM watsonx, RAG, Agentic AI, text processing, voice input, and image analysis.

## Project Structure
```text
SaathiAI/
├── app.py
├── knowledge_base.txt
├── requirements.txt
├── README.txt
├── data/
├── assets/
└── screenshots/
```

## Run Locally
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd SaathiAI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Add required API credentials through environment variables or a `.env` file if your implementation uses an external AI service. Never upload API keys to GitHub.

## Expected Impact
SaathiAI aims to make sustainability information more accessible, understandable, and actionable, helping users make better everyday decisions related to waste management, water conservation, energy use, and responsible consumption.

## Future Scope
- Regional and local sustainability knowledge
- More Indian languages
- Improved image analysis
- Personalized recommendations
- Community-level sustainability insights
- Real-time environmental information

## Disclaimer
SaathiAI is an educational prototype. Its recommendations are general guidance and should not replace official, professional, or safety advice.
