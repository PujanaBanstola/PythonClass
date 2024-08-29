import qrcode
img = qrcode.maker('Pujana Banstola')
type(img)  # qrcode.image.pil.PilImage
img.save("pujana.png")



