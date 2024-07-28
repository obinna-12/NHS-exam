from PIL import Image, ImageDraw, ImageFont
from pyzbar.pyzbar import decode

# Load the image with QR codes
image_path = "./QRcode.PNG"
image = Image.open(image_path)

# Decode all QR codes in the image
decoded_objects = decode(image)

# Initialize ImageDraw object to draw text and shapes
draw = ImageDraw.Draw(image)

# Load a font (using default bitmap font, no size adjustment possible)
font = ImageFont.load_default()

# Process each decoded QR code
for obj in decoded_objects:
    # Extract the data and bounding box
    qr_data = obj.data.decode('utf-8')  # Decode QR code data as a string
    qr_bbox = obj.rect  # Get the bounding box of the QR code
    
    # Define text position (above the QR code)
    text_position = (qr_bbox.left, qr_bbox.top - 10)  # Position the text 10 pixels above the QR code

    # Draw a rectangle around the QR code
    draw.rectangle(
        [(qr_bbox.left, qr_bbox.top), (qr_bbox.left + qr_bbox.width, qr_bbox.top + qr_bbox.height)],
        outline="red",  # Red color for the rectangle
        width=3  # Line width of the rectangle
    )

    # Draw the QR code data on the image
    draw.text(text_position, qr_data, font=font, fill=(0, 0, 0))  # Write the decoded text above the QR code

# Save the modified image in the same directory with a new name
output_image_path = "./Decoded_QRCodes_Highlighted.png"
image.save(output_image_path)
