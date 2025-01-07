
import qrcode
img = qrcode.make('Pujana Banstola')

### WIFI Link
phone=9813950953
message="Hello I am Pujana Banstola"
sms = f"SMSTO:{phone}:{message}"
img = qrcode.make(sms)
type(img)  # qrcode.image.pil.PilImage
img.save("sms.png")