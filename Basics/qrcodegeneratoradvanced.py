from tkinter import Image
from turtle import back
import qrcode as qr
from PIL import Image
makef = qr.QRCode(version = 1, 
        error_correction = qr.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4, 
)
makef.add_data("http://golesuman.pythonanywhere.com/distance")
makef.make(fit = True)
img = makef.make_image(fill_color = "red", back_color = "blue")
img.save("goleapi.png")