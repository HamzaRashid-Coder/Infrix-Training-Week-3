from .preprocess import clean_text
from .ner import extract_entities
from .tfidf import TfidfSearch
from .intent import classify_intent

def load_chunks(path="training_data.txt", chunk_size=500):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def run_pipeline(user_query):
    chunks = load_chunks()
    cleaned = [clean_text(c) for c in chunks]

    tfidf = TfidfSearch(cleaned)
    top_indices, scores = tfidf.search(user_query)

    relevant_docs = [chunks[i] for i in top_indices]
    entities = extract_entities(user_query)
    intent = classify_intent(user_query)

    return {
        "intent": intent,
        "entities": entities,
        "documents": relevant_docs,
    }