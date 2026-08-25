# Medical Chatbot

An AI-powered medical assistance system that provides informed responses to medical questions using Retrieval-Augmented Generation (RAG) technology.

## 📋 Project Description

The Medical Chatbot is a task-specific inference system trained on medical knowledge, designed to answer medical questions and provide informative feedback. It combines advanced language models with a comprehensive medical knowledge base to deliver accurate and contextually relevant responses to healthcare-related queries.

## 🏗️ Architecture

We employ a **Retrieval-Augmented Generation (RAG)** approach rather than fine-tuning because:
- RAG is cost-effective compared to fine-tuning which requires significant computational resources
- It allows quick updates to the knowledge base without retraining
- It provides better performance with limited training data

### RAG Pipeline:
1. **Knowledge Base Creation**: Extract documents from medical PDFs using LangChain
2. **Text Chunking**: Split documents into manageable chunks (500 characters with 20-character overlap)
3. **Embeddings**: Convert text chunks into vector embeddings using HuggingFace embeddings
4. **Vector Storage**: Store embeddings in Pinecone vector database for semantic search
5. **Retrieval & Generation**: Query similar documents and generate responses using Google's Gemini AI

## 📚 Data Source

**Book**: Gale Encyclopedia of Medicine - A comprehensive medical reference containing detailed information about various medical conditions, treatments, and healthcare topics.

### Data Processing Pipeline:
- Extract documents from PDF using PyPDFLoader
- Apply RecursiveCharacterTextSplitter for optimal chunking
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2` model
- Store vectors in Pinecone for efficient semantic search (retrieves top 3 similar documents)

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML/CSS |
| **LLM Framework** | LangChain |
| **Language Model** | Google Gemini 2.5 Flash |
| **Embeddings** | HuggingFace (sentence-transformers) |
| **Vector Database** | Pinecone |
| **Infrastructure** | AWS (EC2, ECR) |
| **CI/CD** | GitHub Actions |
| **API Keys** | OpenAI, Google Generative AI, Pinecone |

## 🔧 Key Dependencies

- **langchain**: Orchestration framework for LLM applications
- **langchain-pinecone**: Pinecone vector store integration
- **langchain-google-genai**: Google Gemini integration
- **flask**: Web framework
- **pypdf**: PDF document loading and processing
- **sentence-transformers**: Embedding generation
- **python-dotenv**: Environment variable management

## 📁 Project Structure

```
MedicalChatbot/
├── app.py                    # Flask application (main entry point)
├── requirements.txt          # Python dependencies
├── setup.py                  # Package configuration
├── store_index.py            # Vector store indexing script
├── template.sh               # Shell configuration template
│
├── src/                      # Source code modules
│   ├── __init__.py
│   ├── helper.py             # PDF loading, chunking, embedding functions
│   └── prompt.py             # System prompt and prompt templates
│
├── data/                     # Data files
│   └── Medical_book.pdf      # Medical reference book (Gale Encyclopedia)
│
├── templates/                # HTML templates
│   └── chat.html             # Chat interface
│
├── static/                   # Static assets
│   └── style.css             # CSS styling
│
├── research/                 # Research and experimentation
│   └── trails.ipynb          # Jupyter notebook for experimentation
│
└── .vscode/                  # VS Code configuration
    └── settings.json
```

## 🚀 How It Works

### 1. **Document Processing** (`helper.py`)
- Loads PDF files from the data directory
- Splits documents into chunks of 500 characters with 20-character overlap
- Filters metadata to maintain only source information and content

### 2. **Embedding & Storage** (`store_index.py`)
- Generates embeddings for all document chunks using HuggingFace
- Stores embeddings in Pinecone vector database with index name: `medical-chatbot`

### 3. **Query Processing** (`app.py`)
- User submits a medical question through the Flask web interface
- Question is converted to an embedding and used to retrieve similar documents (top 3)
- Retrieved documents are passed to Google Gemini AI with a system prompt
- AI generates a contextual, medically-informed response
- Response is returned to the user via the web interface

### 4. **REST API**
- **GET/POST `/`**: Serves the chat interface
- **GET/POST `/get`**: Processes user messages and returns chatbot responses
  - Input: `msg` (user question)
  - Output: Generated response from the RAG chain

## 🔐 Environment Setup

Create a `.env` file with the following variables:
```
PINECONE_MEDICAL_CHATBOT=<your-pinecone-api-key>
GEMINI_API_KEY=<your-google-generative-ai-key>
```

## 🌐 Deployment & CI/CD Pipeline

```
GitHub Repository → GitHub Actions → AWS ECR → AWS EC2
```

### Deployment Flow:
1. **Code Commit**: Push code to GitHub
2. **GitHub Actions**: Trigger automated workflows
3. **Docker Image**: Build and push Docker image to AWS ECR (Elastic Container Registry)
4. **EC2 Deployment**: Pull Docker image on EC2 instance
5. **Port Mapping**: Configure port mapping to expose the application
6. **Public Access**: Assign Elastic IP for user access

## 🎯 Key Features

- **RAG-based System**: Combines retrieval with generation for accurate responses
- **Vector Search**: Semantic search using embeddings for finding relevant medical information
- **Scalable Architecture**: Cloud-based deployment with Docker containerization
- **Real-time Chat**: Interactive web interface for seamless user experience
- **Medical Knowledge Base**: Built on comprehensive medical encyclopedia
- **Automated CI/CD**: Continuous integration and deployment via GitHub Actions

## 📊 Model Details

- **Language Model**: Google Gemini 2.5 Flash
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2
- **Chunk Size**: 500 characters with 20-character overlap
- **Retrieval**: Top-3 similar documents using cosine similarity
- **Vector Database**: Pinecone with index name `medical-chatbot`

## 🔄 Workflow

1. User submits a medical question via the web interface
2. Question is embedded and searched in Pinecone
3. Top 3 relevant medical documents are retrieved
4. Documents are combined with the system prompt and user question
5. Google Gemini processes the context and generates a response
6. Response is displayed to the user in real-time

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pinecone API key
- Google Generative AI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/tanuj5002/MedicalChatbot.git
cd MedicalChatbot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "PINECONE_MEDICAL_CHATBOT=your_key" > .env
echo "GEMINI_API_KEY=your_key" >> .env
```

### Running the Application
```bash
# Run Flask application
python app.py

# Access the chatbot at http://localhost:8080
```

## 📝 Notes

- The system uses RAG instead of fine-tuning to reduce costs and improve flexibility
- Vector embeddings are pre-computed and stored in Pinecone for fast retrieval
- The Flask application runs on port 8080 with debug mode enabled for development
- The `.vscode/settings.json` contains project-specific VS Code configurations

## 🔮 Future Improvements

- Multi-language support
- Enhanced prompt engineering for specific medical specialties
- User feedback mechanism for continuous improvement
- Integration with medical APIs for real-time data
- Mobile app development
- Database for conversation history tracking

## 📜 License

This project is created for educational and research purposes.

---

**Repository**: [tanuj5002/MedicalChatbot](https://github.com/tanuj5002/MedicalChatbot)  
**Created**: December 30, 2025  
**Last Updated**: January 3, 2026
