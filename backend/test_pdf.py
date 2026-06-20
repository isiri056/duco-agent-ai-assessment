from tools.pdf_parser import extract_pdf_text

text = extract_pdf_text(
    "../mock_data/aarav_mri_report.pdf"
)

print(text)