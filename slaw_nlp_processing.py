import spacy

def extract_keywords(text):
    """Extract keywords from a business idea description."""
    nlp = spacy.load("en_core_web_sm")  # Load small English model
    doc = nlp(text.lower())
    # Extract nouns, proper nouns, and adjectives as keywords
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"]]
    return " ".join(keywords)

def process_idea(idea_text):
    """Process idea text and return keywords for classification."""
    if not idea_text or not isinstance(idea_text, str):
        return ""
    return extract_keywords(idea_text)