from tools.pdf_parser import extract_pdf_text
from tools.image_parser import extract_image_text
from tools.gemini_client import ask_gemini

def analyze_documents():

    mri_text = extract_pdf_text(
        "../mock_data/aarav_mri_report.pdf"
    )

    invoice_text = extract_image_text(
        "../mock_data/priya_pt_invoice.png"
    )

    estimate_text = extract_image_text(
        "../mock_data/surgeon_estimate.png"
    )

    prompt = f"""
    You are a medical claims analyst.

    MRI Report:
    {mri_text}

    PT Invoice:
    {invoice_text}

    Surgeon Estimate:
    {estimate_text}

    Extract:

    1. Diagnosis
    2. Recommended Procedure
    3. CPT Codes
    4. Estimated Charges
    5. Medical Necessity

    Return JSON only.
    """

    return ask_gemini(prompt)