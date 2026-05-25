# ResumeBot RAG Project


ResumeBot is a Retrieval-Augmented Generation (RAG) assistant built to interact with a candidate's resume in a conversational way.

## 🚀 Description

This project ingests resume content into a vector store and uses that content to answer questions, summarize skills, explain experience, and generate interview-style responses.

ResumeBot is designed to make resume review faster and smarter by combining document retrieval with natural language generation.

## 🧠 Whole Flow

1. `ingest.py` reads the resume source documents and stores semantic embeddings in a local Chroma database.
2. `ask.py` loads the embedding index and accepts user questions.
3. A retrieval layer finds the most relevant resume snippets for the query.
4. The language model generates an answer using the retrieved resume context.
5. The user receives a concise, resume-aware response.

## 🌈 Visual Flow

```mermaid
flowchart TD
    A[📄 Resume Source] --> B[🧾 Ingest Module (`ingest.py`)]
    B --> C[🧠 Vector Store (Chroma)]
    D[💬 User Question (`ask.py`)] --> E[🔍 Retrieve Relevant Resume Chunks]
    C --> E
    E --> F[🤖 LLM Answer Generation]
    F --> G[✅ ResumeBot Response]
```

## 📌 Key Use Cases

- **Resume Q&A**: Ask the bot about candidate experience, education, skills, and project details.
- **Skill Summary**: Request a summary of technical skills or domain expertise from the resume.
- **Interview preparation**: Generate sample answers or talking points based on the candidate's background.
- **Resume validation**: Confirm that the resume includes specific tools, certifications, or achievements.

## 🛠️ Files

- `ingest.py` — builds the Chroma database from the resume text and embeddings.
- `ask.py` — runs the user interaction flow and returns answers using retrieved resume context.
- `requirements.txt` — required Python dependencies.
- `chroma_db/` — stores the local Chroma vector database.

## ✅ How to Use

```bash
python ingest.py
python ask.py
```

## 💡 Recommended Flow

1. Add or update resume text in the source document used by `ingest.py`.
2. Run `python ingest.py` to refresh the vector index.
3. Ask questions by running `python ask.py`.

## 📎 Benefits

- Fast retrieval of resume facts using semantic search.
- Answers are grounded in the actual resume content.
- Useful for recruiters, hiring managers, and interviewers.
- Enables data-driven follow-up questions.

## 🔧 Notes

- Ensure the Python environment has all dependencies installed from `requirements.txt`.
- The local `chroma_db/` folder stores the resume embeddings for repeated use.
- This project is optimized for resume interaction rather than generic chatbot conversation.
