import base64
from PIL import Image

file_png = r'Ek.png'
img = Image.open(file_png)
img.save('Ek.ico')

with open('Ek.ico','rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

ico_to_py = "img = ''%s'''" %encoded_string
str(ico_to_py)
ico_to_py = ico_to_py[0:8] + ico_to_py[9:-1]
file = open('icon.py','w+')
file.write(ico_to_py)
file.close()
