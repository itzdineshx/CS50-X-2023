import os
import qrcode

# Get link from user
n = input("Link: ")

# Make the file to save the QR code
img = qrcode.make("https://www.youtube.com/live/5Jppcxc1Qzc?si=LPMJ4f2n6Di-1OGW")

# Save the file
img.save("qr.png", "PNG")

# Open the file based on the operating system
if os.name == 'posix':  # macOS and Linux
    os.system("open qr.png")
elif os.name == 'nt':   # Windows
    os.system("start qr.png")
else:
    print("Unsupported operating system. Please open qr.png manually.")
