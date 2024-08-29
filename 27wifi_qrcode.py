import qrcode
img = qrcode.make('Pujana BAnstola')


### WIFI Link
wifi_type = "WPA"
wifi_ssid = "binita79_fpkhr"
wifi_password = "nin24ja!?123"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")