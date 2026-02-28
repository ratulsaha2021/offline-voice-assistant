from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_docs(path: str)->List[str]:
    docs= []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line= line.strip()
            if line:
                docs.append(line)
        return docs

DOCS = load_docs("knowledge.txt")

vectorizer = TfidfVectorizer()
DOC_VECTORS = vectorizer.fit_transform(DOCS)

def rag_answer(query:str)->str:
    if not query.strip():
        print("I did not recieve the question")

    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, DOC_VECTORS)[0]

    best_index = sims.argmax()
    best_doc = DOCS[best_index]
    return best_doc

if __name__ == "__main__":
    while True:
        q = input("Ask (empty to stop): ") 
        if not q:
            break
        print("Answer", rag_answer(q))