# ChatBot
# 🧠 AI Model API

This is a simple API service built with **FastAPI**, **OpenAI's GPT model**, and **MongoDB** to handle chat prompts, generate AI-based responses, and store the conversation history. The project is fully containerized using **Docker** and **Docker Compose**.

---

## 🚀 Features

- Accepts text prompts from users via a REST API.
- Sends prompts to OpenAI and returns generated responses.
- Stores prompt–response pairs in MongoDB for recordkeeping.
- Easily deployable using Docker and Docker Compose.

---

## 🛠 Tech Stack

- **FastAPI** — Web API framework
- **OpenAI API** — For generating intelligent responses
- **MongoDB** — NoSQL database for storing chats
- **Docker** — Containerization
- **Docker Compose** — Multi-container orchestration
- **Pydantic** — For request/response validation

---

## 📁 Project Structure
chatbot/ 
├── app/ │ 
  ├── main.py # FastAPI entry point │ 
  ├── openai_api.py # Handles OpenAI API calls │ 
  ├── models.py # (Optional) DB models if needed │ 
  ├── database.py # MongoDB connection │ 
  └── schemas.py # Pydantic models 
├── Dockerfile # Docker image setup 
├── docker-compose.yml # Compose configuration 
├── requirements.txt # Python dependencies 
├── .env # Environment variables 
└── README.md # This file
---

## 🐳 Docker Usage

### Build & Run:
```bash
docker-compose up --build
```




📝 To Do / Improvements
Add user authentication

  -- Build a front-end (React or similar)

  -- Add a UI to view chat history

  -- Rate limiting & logging

  -- Possible intergration with Whatsapp
