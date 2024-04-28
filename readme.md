# Certificate Authentication Website with QR Code Generator

Welcome to the Certificate Authentication Website with QR Code Generator project! This project provides a comprehensive solution for companies to issue certificates and implement an authentication system using QR codes.

## About

This project consists of a web application for certificate authentication and a QR code generator. It enables companies to issue certificates to individuals and provides an authentication system for verifying the authenticity of these certificates using QR codes.

## Features

- Certificate Authentication Website:
  - Upload certificates for authentication.
  - Decrypt binary data from QR codes into readable text.
  - Verify the authenticity of certificates.

- QR Code Generator:
  - Generate QR codes from certificate information.
  - Convert certificate information into binary data for QR code generation.

## How it Works

### Certificate Authentication Website:
1. Users upload certificates for authentication.
2. The website decrypts binary data from QR codes into readable text.
3. Certificate information is displayed for verification.

### QR Code Generator:
1. Certificate information is converted into binary format.
2. QR codes are generated from the binary data.
3. Generated QR codes can be used for certificate authentication.

## Usage

1. Clone this repository.
2. Certificate Authentication Website:
    - Open `index.html` in your preferred web browser to access the Certificate Authentication Website.
    - Upload certificates for authentication.
    - Verify certificate authenticity using the provided QR code authentication system.
3. QR Code Generator:
    - Run the Python script `generate_qr_code.py` to generate QR codes from certificate information.
    - Use the generated QR codes for certificate verification.

## Installation

To run the Certificate Authentication Website locally, ensure you have Python installed. Then, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
