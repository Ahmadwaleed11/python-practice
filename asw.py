import pypandoc

# Convert PDF to Word
input_pdf = "Ahmad Waleed cv.pdf"
output_docx = "output.docx"

pypandoc.convert_text(open(input_pdf, 'rb').read(), 'docx', format='pdf', outputfile=output_docx, extra_args=['--standalone'])

print("✅ Conversion complete! Saved as", output_docx)
