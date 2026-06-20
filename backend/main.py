from fastapi import FastAPI
from agents.cob_agent import calculate_acl_claim

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "DuCO Agent Running"
    }

@app.get("/claim")

def claim():

    return calculate_acl_claim()