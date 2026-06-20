from tools.image_parser import extract_image_text

text = extract_image_text(
    "../mock_data/priya_pt_invoice.png"
)

print(text)