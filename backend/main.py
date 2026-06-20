from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.document_agent import analyze_documents
from agents.cob_agent import coordinate_benefits

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "DuCO Agent Running"
    }

@app.get("/analyze")
def analyze():

    documents = analyze_documents()

    cob = coordinate_benefits()

    return {
        "documents": documents,
        "cob": cob
    }
@app.get("/claim")
def claim():

    return coordinate_benefits()