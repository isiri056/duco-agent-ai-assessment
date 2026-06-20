from tools.gemini_client import ask_gemini
import os


def generate_preauth_letters():

    aarav_prompt = """
Generate a complete insurance pre-authorization letter.

Patient: Aarav Sen

Diagnosis:
- Complete ACL Tear
- Medial Meniscus Tear

Procedure:
- CPT 29888 ACL Reconstruction
- CPT 29881 Meniscectomy

Estimated Cost:
₹4,50,000

Insurance:
Primary Plan B (Insurer2)
Secondary Plan A (Insurer1)

Do NOT use placeholders.

Generate a professional finalized letter ready for insurance submission.
"""

    priya_prompt = """
Generate a complete insurance pre-authorization letter.

Patient: Priya Sen

Treatment:
- Physical Therapy Evaluation
- Therapeutic Exercise

CPT Codes:
- 97161
- 97110

Charges:
₹30,000

Insurance:
Primary Plan A (Insurer1)
Secondary Plan B (Insurer2)

Do NOT use placeholders.

Generate a professional finalized letter ready for insurance submission.
"""

    aarav_letter = ask_gemini(aarav_prompt)
    priya_letter = ask_gemini(priya_prompt)

    return {
        "aarav_letter": aarav_letter,
        "priya_letter": priya_letter
    }


def save_letters():

    letters = generate_preauth_letters()

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/aarav_preauth.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(letters["aarav_letter"])

    with open(
        "outputs/priya_preauth.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(letters["priya_letter"])

    return {
        "status": "success",
        "files_saved": [
            "outputs/aarav_preauth.txt",
            "outputs/priya_preauth.txt"
        ]
    }