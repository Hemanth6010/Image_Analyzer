# AI Fitness Image Analyzer

An AI-powered fitness assistant that combines image analysis with user queries and fitness-related knowledge retrieval to generate contextual fitness insights.

The project uses a vision-capable Large Language Model (LLM) along with Retrieval-Augmented Generation (RAG) to provide responses grounded in relevant fitness information.

## Features

- **Image-Based Analysis:** Analyzes user-provided images using OpenAI's GPT-4o-mini vision model.
- **Context-Aware Responses:** Considers both the uploaded image and the user's fitness-related query.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from a fitness knowledge base using vector embeddings.
- **Image Optimization:** Uses image resizing and compression before uploading images to Cloudinary.
- **Image Caching:** Uses image hashing to identify previously processed images and reuse stored image URLs.
- **Input Validation:** Filters unrelated and restricted queries.
- **Structured Output:** Generates responses containing observations, analysis, suggestions, and optional tips.
- **Token Tracking:** Tracks model token usage and estimated API costs.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenAI GPT-4o-mini | Vision analysis and response generation |
| LangChain | LLM workflow orchestration |
| ChromaDB | Vector database |
| Embeddings | Semantic search and retrieval |
| Cloudinary | Image hosting and optimization |
| Pillow (PIL) | Image processing |
| Pydantic | Structured response validation |
| Jupyter Notebook | Development and experimentation |

## Project Structure

```text
fitness-image-analyzer/
│
├── fitness_image_analyzer.ipynb
├── Rules_dummy.txt
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

## How It Works

1. The user provides an image and a fitness-related question.
2. The image is processed, resized, and compressed before being uploaded to Cloudinary.
3. The user's query is used to retrieve relevant fitness information from the ChromaDB vector database.
4. The image, query, and retrieved knowledge are passed through a LangChain pipeline.
5. GPT-4o-mini analyzes the visual information alongside the retrieved context.
6. The application generates a structured response with observations, analysis, suggestions, and tips.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd fitness-image-analyzer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

Add the required credentials:

- OpenAI API key
- Cloudinary cloud name
- Cloudinary API key
- Cloudinary API secret

Never upload your actual `.env` file or expose API credentials publicly.

### 5. Run the Project

Open `fitness_image_analyzer.ipynb` in Jupyter Notebook or VS Code.

Run the notebook cells in sequence after configuring the required environment variables and knowledge-base files.

## Knowledge Base

The project uses fitness-related reference material to provide additional context during response generation.

The documents are split into smaller chunks, converted into embeddings, and stored in ChromaDB for semantic retrieval.

## Disclaimer

This project is an experimental fitness assistance tool. Its outputs are intended for general informational purposes and should not be considered medical diagnoses or a replacement for professional fitness or healthcare advice.

## Future Improvements

- Convert the notebook workflow into a standalone application.
- Improve caching and retrieval efficiency.
- Expand the fitness knowledge base.
- Improve structured response handling.
- Develop a user-friendly interface.

## License

This project is distributed under the license included in this repository.