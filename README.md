# 🤖 AI Summarization API - FastAPI + HuggingFace + Docker

This is a FastAPI-based RESTful API that provides text summarization using a pre-trained transformer model from Hugging Face. It is built with production best practices, structured logging, environment configuration, and containerized with Docker.

---

## 📚 Features

- Summarizes long-form text using Hugging Face models (e.g., BART, T5)
- FastAPI with OpenAPI docs (`/docs`)
- Configurable via `.env`
- Rotating log files saved by date
- Dockerized and ready for Kubernetes

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Docker (for containerized setup)

### 📦 Install dependencies (for development)
```bash
pip install -r dev-requirements.txt
```

### 🧪 Run locally
```bash
python run.py
```

---

## 🐳 Build & Run with Docker

### 🛠️ Step 1: Build Docker image
```bash
docker build -t ai-api-suite .
```

### ▶️ Step 2: Run Docker container
```bash
docker run --env-file .env -p 8000:8000 ai-api-suite
```

---

## ⚙️ Environment Variables
Create a `.env` file in the root directory with variables like:
```env
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=INFO
MODEL_NAME="facebook/bart-large-cnn"
```

---

## 📝 Logging
- Logs are stored in the `logs/` directory.
- Rotated daily with filenames like `20250408.txt`.
- Both console and file logging are enabled.

---

## 📬 API Endpoint
### POST `/summarizer/summarize`
**Request Body:**
```json
{
  "text": "<your input text>",
  "max_length": 100,
  "min_length": 30,
  "do_sample": false
}
```

**Response:**
```json
{
  "summary": "<generated summary>",
  "char_count": 123,
  "word_count": 20
}
```

---

## 🧼 .gitignore Additions
Make sure to add the following to `.gitignore`:
```
logs/
.env
```

---

## 🛠️ License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Docker](https://www.docker.com/)