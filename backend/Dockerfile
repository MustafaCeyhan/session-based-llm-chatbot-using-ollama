# Dockerfile for Backend
FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install fastapi langchain langchain_community langchain_core langchain_openai uvicorn pydantic

# Ensure Ollama is installed on the host system
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
