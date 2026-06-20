from tools.pdf_parser import extract_pdf_text
from tools.image_parser import extract_image_text

def parse_documents():

    mri_text = extract_pdf_text(
        "mock_data/aarav_mri_report.pdf"
    )

    invoice_text = extract_image_text(
        "mock_data/priya_pt_invoice.png"
    )

    estimate_text = extract_image_text(
        "mock_data/surgeon_estimate.png"
    )

    return {
        "mri": mri_text,
        "invoice": invoice_text,
        "estimate": estimate_text
    }