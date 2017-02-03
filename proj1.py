import os, numpy, PIL
from PIL import Image

files = os.listdir(os.getcwd())
imgs = [filename for filename in files if filename[-4:] in [".png"]]

width, height = Image.open(imgs[0]).size
n = len(imgs)

arr = numpy.zeros((height, width, 3), numpy.float)

for i in imgs:
    imgarr = numpy.array(Image.open(i), dtype=numpy.float)
    arr = arr+imgarr/n
    
arr = numpy.array(numpy.round(arr), dtype = numpy.uint8)

finalImg = Image.fromarray(arr, mode = "RGB")
finalImg.save("finalImg.png")
finalImg.show()