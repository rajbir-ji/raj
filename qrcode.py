import qrcode

   # Data to be encoded in the QR code
data = "https://www.typingclub.com/.com"

   # Create a QR code
qr = qrcode.make(data)

   # Save the QR code as an image file
qr.save("example_qrcode.png")
print("QR Code generated and saved as 'example_qrcode.png'")
   