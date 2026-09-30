# AI Image & Document Assistant

A beginner-friendly multimodal AI application built with Streamlit and Groq.

The app accepts an image and a natural-language question, then sends both to a multimodal model for visual understanding.

## Features

- Image understanding
- Visual question answering
- Document image understanding
- Information extraction
- Educational diagram explanation
- Hallucination-aware prompting
- Simple Streamlit interface

## Project Structure

```text
MULTIMODAL-AI-ASSISTANT/
├── app.py
├── multimodal/
│   ├── __init__.py
│   └── vision.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

```text
User
  ↓
Upload Image
  ↓
Ask Question
  ↓
Convert Image to Base64 Data URL
  ↓
Multimodal LLM
  ↓
Visual Analysis
  ↓
Answer
```

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create Streamlit Secrets in:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
GROQ_MODEL = "your_multimodal_vision_model"
```

The secrets file is ignored by Git and must never be committed.

## Run

```bash
python -m streamlit run app.py
```

## Suggested Tests

### 1. Product Image
Question:
"What product is shown in this image?"

### 2. Document Image
Question:
"Extract the title, date, and important information from this document."

### 3. Educational Diagram
Question:
"Explain this diagram in simple words."

### 4. Unavailable Information
Question:
"What is the person's phone number?"

If the phone number is not visible, the assistant should say that it is not visible instead of inventing one.

## Prompt Comparison

Vague prompt:

"What is this?"

Clear prompt:

"Identify the main product visible in this image and describe its key visible features. Do not guess information that is not visible."

Clear prompts help make the expected output more specific and reliable.

## Real-World Use Case

This type of assistant can support customer service, education, document processing, and accessibility. For example, a support agent could upload a product photo or document and ask the AI to identify visible information before responding to a customer.

## Day 14 Learning Goals

This project demonstrates:

- Multimodal Generative AI
- Image understanding
- Visual Question Answering (VQA)
- Document understanding
- Structured information extraction
- Prompt clarity
- Hallucination prevention
