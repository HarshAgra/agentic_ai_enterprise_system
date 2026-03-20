# 🚀 Agentic AI Enterprise System (Project Pragna)

## 📌 Overview

This project is a **multi-agent AI system** designed to automate enterprise workflows across multiple business functions such as **Customer Support, HR, Finance, and Procurement**.

The system uses an **Orchestrator Agent** to intelligently route user queries to specialized agents and integrates a **Retrieval-Augmented Generation (RAG)** pipeline to generate responses grounded in business documents.

---

## 🧠 Key Features

* 🤖 Multi-agent architecture (Orchestrator + Domain-specific agents)
* 🔀 Intelligent query classification and routing
* 📄 Retrieval-Augmented Generation (RAG) using PDF-based knowledge
* 🧩 Modular and scalable system design
* 🌐 Streamlit-based interactive web application

---

## 🏗️ System Architecture

```
User Query
   ↓
Orchestrator Agent (classification)
   ↓
Relevant Agent (Support / HR / Finance / Procurement)
   ↓
Retriever (fetch context from PDF)
   ↓
LLM (Azure OpenAI)
   ↓
Final Response
```

---

## 🛠️ Tech Stack

* Python
* Azure OpenAI (GPT-4o / GPT-4o-mini)
* Streamlit
* RAG (PDF-based retrieval using PyPDF)

---

## 📂 Project Structure

```
agentic-pragna-system/
│
├── agents/              # Individual agent prompts
├── workflows/           # Routing logic
├── utils/               # LLM client + retriever
├── data/                # Input documents (PDF)
│
├── app.py               # Streamlit UI
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd agentic-pragna-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add environment variables

Create a `.env` file:

```
AZURE_API_KEY=your_api_key
AZURE_ENDPOINT=https://your-resource.services.ai.azure.com
AZURE_DEPLOYMENT=your_deployment_name
```

---

### 4. Add your data

Place your PDF file inside the `data/` folder:

```
data/pragna_case.pdf
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🧪 Example Queries

* Why are customer queries increasing after Astra launch?
* How are vendor proposals evaluated?
* What operational challenges are faced by HR?
* Why are vendor payments getting delayed?
* How are shop floor issues handled?

---

## 💡 Key Learnings

* Designing **multi-agent systems** for business workflows
* Implementing **query routing using an orchestrator agent**
* Building a **basic RAG pipeline for document-grounded responses**
* Handling **LLM hallucination through controlled prompting and retrieval**

---

## 🔮 Future Improvements

* Vector database integration (FAISS / embeddings)
* Chat history and memory
* API-based deployment
* Advanced UI enhancements

---

## 💼 Use Case

This system simulates a real-world enterprise scenario where multiple departments operate in silos and demonstrates how **Agentic AI can unify workflows and improve decision-making efficiency**.

---

## 🔗 Author

**Harsh Agrawal**
MBA (Big Data Analytics)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
