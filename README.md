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

```bash
docker-compose up --build
```

Visit the API at:  
📜 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

MongoDB will be available at `mongodb://localhost:27017` (or from within the container: `mongodb://mongodb:27017`)

---

## 💡 Environment Variables

Create a `.env` file at the root:

```
OPENAI_API_KEY="sk-..."
MONGO_URI="mongodb://localhost:27017"  # Optional override for local use
```

---

## 🧪 Running Tests

Tests are written using `pytest`.

> ⚠️ Tests require a local MongoDB instance to be running (outside Docker).

```bash
pytest tests/
```

Make sure the following are installed:
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

- **Anonymization**: Prompt & response texts are sanitized before saving.
- **Conversation context**: Query payloads to GPT include full history.
- **OpenAPI Spec**: Strictly followed. Minor differences explained in comments/code.
- **MongoDB Integration**: Beanie ODM used for async, document-based persistence.

---

## 🧊 Optional: Frontend (Task 2)

Not included in this repo. If added, would be located in a separate `frontend/` folder.

---

## 👨‍💻 Author

- Chen Jian Jie
- GitHub: [@jianjie22](https://github.com/jianjie22)