# AI Personal Assistant with Backend and Frontend

This project is a conversational AI assistant built using FastAPI for the backend and Streamlit for the frontend. The backend uses SQLite for conversation logging and integrates with an Ollama LLM model, while the frontend provides a user-friendly interface to interact with the AI.

## Features
- **Frontend**: Built with Streamlit, providing a chat interface for users.
- **Backend**: Powered by FastAPI, handling LLM interactions and SQLite logging.
- **LLM Integration**: Leverages Ollama for AI responses.
- **Session Management**: Maintains conversation history and unique session IDs.
- **Dockerized Deployment**: Fully containerized using Docker Compose.

---

## Project Structure
```
project/
├── backend/
│   ├── Dockerfile
│   ├── app.py
├── frontend/
│   ├── Dockerfile
│   ├── streamlit_app.py
├── docker-compose.yml
├── README.md
```

---

## Prerequisites
- [Docker](https://www.docker.com/) installed on your system
- [Docker Compose](https://docs.docker.com/compose/) installed

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Build and Start the Services
Use Docker Compose to build and start the services:
```bash
docker-compose up --build
```
This will:
- Start the **backend** service at `http://localhost:8000`
- Start the **frontend** service at `http://localhost:8501`

### 3. Access the Application
- **Frontend**: Open your browser and navigate to `http://localhost:8501`.
- **Backend**: API documentation is available at `http://localhost:8000/docs` (Swagger UI).

---

## Environment Variables
If you are using environment variables, create a `.env` file in the root directory with necessary values. Example:
```
# Example environment variables
OLLAMA_BASE_URL=http://host.docker.internal:11434
LLM_MODEL=llama3.2:1b
```
Make sure to load the `.env` file in your backend code.

---

## Backend Configuration
The backend is a FastAPI application that provides an endpoint for interacting with the AI:
- **Endpoint**: `/llm`
- **Method**: `POST`
- **Payload Example**:
```json
{
  "question": "What is AI?",
  "language": "en",
  "history": [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello, how can I help you?"}
  ],
  "session_id": "12345-67890"
}
```

---

## Frontend Configuration
The frontend is built with Streamlit, providing a chat interface to interact with the AI. It communicates with the backend to fetch responses based on user input.

## Troubleshooting

### Common Issues
1. **Port Already in Use**:
   - Stop any services running on ports 8000 or 8501.
   - Use `docker-compose down` to stop running containers.

2. **Backend Not Responding**:
   - Check logs using `docker-compose logs backend`.

3. **Frontend Not Responding**:
   - Check logs using `docker-compose logs frontend`.

---

## Contributing
Feel free to fork this repository, make changes, and submit pull requests.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
