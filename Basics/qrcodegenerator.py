import qrcode as qr
img = qr.make("http://golesuman.pythonanywhere.com/distance")
img.save("golepython.png")
