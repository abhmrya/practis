import qrcode
data = 'https://www.instagram.com/abh.mrya/'
img = qrcode.make(data)
img.save("testing.png")

