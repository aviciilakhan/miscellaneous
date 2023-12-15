import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import gray
import io

def create_watermark(content):
    # Create a PDF for the watermark
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    # Set up the watermark properties
    c.setFont("Helvetica", 60)  # Larger font size
    c.setFillColor(gray, alpha=0.3)  # Light gray color, semi-transparent
    c.rotate(45)  # Rotate the text by 45 degrees

    # Position the watermark (adjust as needed)
    c.drawString(200, 50, content)

    c.save()

    # Move the watermark to a PyPDF2 PageObject
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)
    watermark = new_pdf.getPage(0)
    return watermark

def add_watermark(input_pdf, output_pdf, watermark):
    # Read the original PDF
    original = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    output = PyPDF2.PdfFileWriter()

    # Add watermark to each page
    for i in range(original.getNumPages()):
        page = original.getPage(i)
        page.mergePage(watermark)
        output.addPage(page)

    # Write the watermarked PDF to a file
    with open(output_pdf, 'wb') as outputStream:
        output.write(outputStream)

# Usage
watermark = create_watermark("Anup's Property")
add_watermark("C# Question Bank with Answers.pdf", "watermarked_output1.pdf", watermark)

