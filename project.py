from PIL import Image

#This block of code creates a list of all the opened image files.
myList = []
for i in range(1, 10):
    myList.append(Image.open(str(i) + ".png"))

#This line of code sets the width and height using the width and height of the first image    
width, height = myList[0].size

#This code creates a new image using the same width and height of the first image
newImg = Image.new("RGB", (width, height))
pixnew = newImg.load()

#This for loop goes through the width of the image
for x in range(width):
    #This for loop goes through the height of the image
    for y in range(height):
        pixel = []
        #This for loop goes through the images from the array myList and adds the pixel at x,y into the array of pixel
        for z in range(9):
            pixel.append(myList[z].getpixel((x,y)))
        pixel.sort() #sory the pixel array
        middle = ((10)/2)-1
        pixnew[x,y] = pixel[middle] #add the median array into the new image at x,y
        
#Save the new image made up of the median pixels
newImg.save("newFinalImg.jpg")