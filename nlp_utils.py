import spacy

# Load ScispaCy model (requires: pip install scispacy && pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz)
nlp = spacy.load("en_ner_bc5cdr_md")

def extract_entities(text):
    doc = nlp(text)
    diseases = []
    locations = []

    for ent in doc.ents:
        if ent.label_ == "DISEASE":
            diseases.append(ent.text)
        elif ent.label_ == "GPE":
            locations.append(ent.text)

    return list(set(locations)), list(set(diseases))
