from fastapi import FastAPI

from agents.document_agent import analyze_documents
from agents.cob_agent import coordinate_benefits
from agents.preauth_agent import generate_preauth_letters

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DuCO Agent Running"}


@app.get("/analyze")
def analyze():

    print("STEP 1")
    documents = analyze_documents()

    print("STEP 2")
    cob = coordinate_benefits()

    print("STEP 3")
    letters = generate_preauth_letters()

    print("STEP 4")

    return {
        "documents": documents,
        "cob": cob,
        "letters": letters
    }