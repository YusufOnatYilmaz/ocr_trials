from PIL import Image,ImageDraw
from matplotlib import image
from numpy import size
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("lorem_ipsum.png")
imaj = "lorem_ipsum.png"
width, height = img.size

squares = pytesseract.image_to_boxes(img)
#print(squares)

with open("test.txt", 'w', encoding = 'utf-8') as f:
   f.write(squares)

with open("test.txt", 'r', encoding = 'utf-8') as f:
    box_data = f.readlines()

box_data = [box.split("\n")[0].split(" ") for box in box_data]

#print(box_data)

img1 = ImageDraw.Draw(img)

shape = [img1.rectangle([(int(box[1]), height-int(box[2])), (int(box[3]), height-int(box[4]))], outline ="red") for box in box_data]

''' saner way
for box in box_data:
    shape = [(int(box[1]), height-int(box[2])), (int(box[3]), height-int(box[4]))]
    img1.rectangle(shape, outline ="red")
'''

img.show()


''' MAYBE CHANGE
textord_linespace_iqrlimit	0.2	Max iqr/median for linespace
textord_xheight_mode_fraction	0.4	Min pile height to make xheight
textord_ascheight_mode_fraction	0.08	Min pile height to make ascheight
textord_descheight_mode_fraction	0.08	Min pile height to make descheight
textord_ascx_ratio_min	1.25	Min cap/xheight
textord_ascx_ratio_max	1.8	Max cap/xheight
'''