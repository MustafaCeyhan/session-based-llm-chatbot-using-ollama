# Dockerfile for Frontend
FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip install streamlit requests

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
