# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "MH0063971251355G|300500.00|Rami Bajji|encdate=flL"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 3)


import qrcode
# Link for website
input_data = "MH0063971251355G|300500.00|Rami Bajji|encdate=flL Name -Ravikant Yadav  callme 9005552324"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode004.png')
