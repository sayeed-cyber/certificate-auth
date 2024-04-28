import qrcode

def convert_to_binary(data):
    # Convert data to binary
    binary_data = ' '.join(format(ord(char), '08b') for char in data)
    return binary_data

def generate_qr_code(data):
    # Convert data to binary
    binary_data = convert_to_binary(data)
    
    # Generate QR code from binary data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(binary_data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    return qr_image

# Example usage:
certificate_info = "Certificate Information: John Doe, Certificate Number: 12345"
qr_code_image = generate_qr_code(certificate_info)
qr_code_image.save("certificate_qr_code.png")
print("QR code generated successfully!")
