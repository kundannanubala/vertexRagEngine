# Vertex AI RAG Engine

A Python-based implementation of Retrieval-Augmented Generation (RAG) using Google Cloud's Vertex AI platform.

## Overview

This project demonstrates the implementation of a RAG system using Vertex AI's capabilities. It allows you to create and manage RAG corpora, upload documents, and perform intelligent document retrieval and generation tasks.

## Prerequisites

- Python 3.x
- Google Cloud Project with Vertex AI API enabled
- Google Cloud credentials (Service Account)

## Installation

1. Clone the repository:
```
git clone https://github.com/kundannanubala/vertexRagEngine.git
cd vertex-rag-engine
```

2. Create and activate a virtual environment:
```bash
python -m venv ragvenv
source ragvenv/bin/activate  # On Windows: ragvenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```plaintext
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_REGION=your-region
```

## Project Structure

```plaintext
├── core/
│   └── config.py         # Configuration settings
├── main.py              # Main application file
├── ragEnginecreds.json  # Google Cloud credentials (not tracked in git)
├── requirements.txt     # Project dependencies
└── .env                # Environment variables (not tracked in git)
```

## Configuration

The project uses Pydantic for configuration management. Key configurations are handled in `core/config.py`, including:
- Google Cloud Project settings
- Application credentials
- Environment variable management

## Features

- Vertex AI initialization and authentication
- RAG corpus creation and management
- File upload capabilities to RAG corpus
- Support for Google's text embedding models

## Usage

1. Ensure your Google Cloud credentials are properly set up in `ragEnginecreds.json`

2. Initialize the Vertex AI client:
```python
from core.config import settings
import vertexai

vertexai.init(project=settings.GOOGLE_CLOUD_PROJECT, location=settings.GOOGLE_CLOUD_REGION)
```

3. Upload files to your RAG corpus:
```python
from vertexai.preview import rag

rag_file = rag.upload_file(
    corpus_name="your-corpus-name",
    path="path/to/your/file",
    display_name="file-name",
    description="file-description"
)
```

## Dependencies

The project relies on several key packages:
- `google-cloud-aiplatform`: Google Cloud AI Platform SDK
- `vertexai`: Vertex AI SDK
- `pydantic`: Data validation and settings management
- `pydantic-settings`: Settings management
- `IPython`: Interactive shell support

## Security Notes

- Keep your `ragEnginecreds.json` secure and never commit it to version control
- The `.env` file containing environment variables is excluded from version control
- Always follow Google Cloud security best practices

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]