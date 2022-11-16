import sys

import pyqrcode
from pyqrcode import QRCode

# String which represents the QR Code
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR Code

url = pyqrcode.create(s)

# Create and save the png file named "myqr.png"
url.svg("myqrcode.svg", scale=8)
