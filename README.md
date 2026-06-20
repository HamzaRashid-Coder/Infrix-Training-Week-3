# Infrix Training - Week 3

## LLM API with NLP Pipeline using Hugging Face

This project demonstrates the development of a simple AI-powered API that combines traditional Natural Language Processing (NLP) techniques with Large Language Models (LLMs) through the Hugging Face Inference API.

The system processes user queries, performs text preprocessing, intent detection, named entity recognition (NER), and generates intelligent responses using a Hugging Face-hosted language model.

---

## Project Structure

```text
Infrix-Training-Week-3
│
├── README.md
│
└── LLM_API
    │   app.py
    │   requirements.txt
    │   training_data.txt
    │
    ├── llm
    │   ├── generator.py
    │   ├── model.py
    │   └── prompt_builder.py
    │
    └── nlp
        ├── preprocess.py
        ├── tfidf.py
        ├── intent.py
        ├── ner.py
        └── pipeline.py
```

---

## Features

* Text preprocessing and cleaning
* TF-IDF based feature extraction
* Intent classification
* Named Entity Recognition (NER)
* Prompt engineering and prompt construction
* Integration with Hugging Face Inference API
* REST API interface using Flask
* Modular architecture for easy extension

---

## Workflow

```text
User Query
    │
    ▼
Text Preprocessing
    │
    ▼
Intent Detection
    │
    ▼
Named Entity Recognition
    │
    ▼
Prompt Builder
    │
    ▼
Hugging Face LLM API
    │
    ▼
Generated Response
```

---

## Technologies Used

* Python 3.x
* Flask
* Scikit-learn
* Hugging Face Inference API
* NLP Techniques

  * Tokenization
  * Text Cleaning
  * TF-IDF Vectorization
  * Intent Classification
  * Named Entity Recognition

---

## Module Description

### `app.py`

Main application entry point. Exposes API endpoints and connects the NLP pipeline with the LLM module.

### `nlp/preprocess.py`

Performs text cleaning, normalization, and preprocessing.

### `nlp/tfidf.py`

Generates TF-IDF features from textual input.

### `nlp/intent.py`

Handles intent detection and classification.

### `nlp/ner.py`

Extracts entities from user queries.

### `nlp/pipeline.py`

Combines all NLP components into a single processing pipeline.

### `llm/prompt_builder.py`

Constructs optimized prompts for the language model.

### `llm/model.py`

Manages Hugging Face API configuration and communication.

### `llm/generator.py`

Generates responses from the selected language model.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Infrix-Training-Week-3.git

cd Infrix-Training-Week-3/LLM_API
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / MacOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Hugging Face API

Create a Hugging Face Access Token from:

https://huggingface.co/settings/tokens

Set the token as an environment variable:

### Windows

```bash
set HF_API_TOKEN=your_token_here
```

### Linux / MacOS

```bash
export HF_API_TOKEN=your_token_here
```

---

## Running the Application

```bash
python app.py
```

The API server will start locally.

Example:

```text
http://localhost:5000
```

---

## Example Request

```json
{
    "query": "What is Artificial Intelligence?"
}
```

## Example Response

```json
{
    "response": "Artificial Intelligence (AI) refers to..."
}
```

---

## Learning Objectives

This project was developed as part of the Infrix Training Program Week 3 to help trainees learn:

* NLP fundamentals
* Intent Classification
* Named Entity Recognition
* Prompt Engineering
* API Integration
* Hugging Face Models
* Building AI-powered applications
* Modular Python Development

---

## Future Improvements

* Fine-tuned custom models
* Vector database integration
* Retrieval-Augmented Generation (RAG)
* Conversation memory
* Authentication and API security
* Deployment on cloud platforms

---

## Author

**Muhammad Hamza Rashid**

Training Program – Week 3

Building practical AI solutions with NLP and Large Language Models.
