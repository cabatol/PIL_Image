from PIL import Image

myList = []

for i in range(1, 10):
    myList.append(Image.open(str(i) + ".png"))
    
width, height = myList[0].size

newImg = Image.new("RGB", (width, height))
pixnew = newImg.load()

for x in range(width):
    for y in range(height):
        pixel = []
        for z in range(9):
            pixel.append(myList[z].getpixel((x,y)))
        pixel.sort()
        middle = ((10)/2)-1
        pixnew[x,y] = pixel[middle]
newImg.save("newFinalImg.jpg")