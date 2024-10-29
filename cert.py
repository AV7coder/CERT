from PIL import Image, ImageDraw, ImageFont
import csv
import os

# Define paths
template_path = "template.jpg"  # Replace with your actual file name if different
output_folder = "generated_certificates"
csv_file = "participant.csv"
font_path = "Sterion.ttf"  # Replace with your actual font file if different

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load the certificate template image
template = Image.open(template_path)
width, height = template.size

# Font settings (adjust size if needed)
font_size = 48
font = ImageFont.truetype(font_path, font_size)

# Position for the text (adjust based on your template)
text_x = width // 2
text_y = height // 2  # Center of certificate template

def generate_certificate(name, participant_class):
    # Copy the template for each certificate
    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    # Add participant's name
    text_name = name.upper()
    text_width, text_height = draw.textsize(text_name, font=font)
    position_name = (text_x - text_width // 2, text_y - text_height // 2)
    draw.text(position_name, text_name, fill="black", font=font)
    
    # Add participant's class below the name
    text_class = f"Class: {participant_class}"
    class_width, class_height = draw.textsize(text_class, font=font)
    position_class = (text_x - class_width // 2, text_y + text_height)
    draw.text(position_class, text_class, fill="black", font=font)

    # Save the certificate
    cert_path = os.path.join(output_folder, f"{name}.pdf")
    cert.save(cert_path, "PDF")

# Read participant names and classes from CSV and generate certificates
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if present
    for row in reader:
        name = row[0].strip()          # Participant name in first column
        participant_class = row[1].strip()  # Participant class in second column
        generate_certificate(name, participant_class)

print("Certificates generated successfully!")
