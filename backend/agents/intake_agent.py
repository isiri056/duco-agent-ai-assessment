from tools.gemini_client import ask_gemini

def process_query(query):

    prompt = f"""
    Extract:

    - patient names
    - insurance plans
    - requested procedures

    Query:

    {query}
    """

    return ask_gemini(prompt)