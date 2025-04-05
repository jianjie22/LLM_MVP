# 🚀 LLM MVP - Backend (FastAPI)

This is a backend MVP application that facilitates interaction with LLMs (OpenAI GPT-4o-mini). It supports:

- ✅ CRUD operations on conversations
- 💬 Sending prompts and getting responses from OpenAI
- 🧠 Using previous conversation history as context
- 🔐 Anonymizing and storing prompts/responses in MongoDB for auditing

---

## 📦 Tech Stack

| Tech              | Purpose                             |
|-------------------|-------------------------------------|
| Python 3.11+      | Core language                       |
| FastAPI           | Web framework                       |
| Pydantic          | Request validation / models         |
| Beanie + Motor    | ODM for MongoDB                     |
| MongoDB           | Data storage                        |
| Docker + Compose  | Containerization & orchestration    |
| OpenAI Python SDK | LLM Integration                     |

---

## 🛠️ Getting Started

### 📁 Clone the repo

```bash
git clone https://github.com/jianjie22/llm-mvp.git
cd llm-mvp
```

### 🐳 Run with Docker (Recommended)

Make sure your `.env` is configured like this:

```env
OPENAI_API_KEY=your_openai_key_here
MONGO_URI=mongodb://mongodb:27017
```

> 🔁 `mongodb` here refers to the container name in `docker-compose.yml`.

Then run:

```bash
docker-compose up --build
```

Once running, access the app:

- 📜 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- 🧪 ReDoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 💡 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key_here
MONGO_URI=mongodb://mongodb:27017
```

---

## 🧪 Running Tests (Local Only)

> ⚠️ Tests currently require a **locally running MongoDB** (not Docker-based).

```bash
pytest tests/
```

Install test dependencies:

```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio httpx asgi-lifespan
```

---

## 🧱 API Endpoints

All endpoints follow the OpenAPI spec provided (`openapi.yaml`).

### ✅ `/conversations`
- `POST` – Create a new conversation
- `GET` – List all conversations

### ✅ `/conversations/{id}`
- `GET` – Get conversation by ID
- `PUT` – Update conversation
- `DELETE` – Delete conversation

### 💬 `/queries`
- `POST` – Send a prompt with conversation context, receive LLM response

All requests and responses are stored **anonymized** for audit compliance.

---

## 🧠 Design Considerations

- **Anonymization**: Prompts and responses are stripped of user-identifiable data.
- **Contextual Queries**: Conversation history is passed to the LLM for more coherent responses.
- **Schema Adherence**: Implementation follows the provided OpenAPI spec.
- **Async & Performant**: Beanie ODM ensures efficient async interaction with MongoDB.

---

## ❌ Frontend (Task 2)

This repository **does not include** Task 2 (frontend).  
Only Task 1 (backend API) is submitted for this assignment.

---

## 👨‍💻 Author

- Chen Jian Jie  
- GitHub: [@jianjie22](https://github.com/jianjie22)