import cv2 as cv
# x and y, for starting position to crop image
x = int(input("Enter initial x value = "))
y = int(input("Enter initial y value = "))
# w and h for width and height of cropping image
h = int(input("Enter cropped image height = "))
w = int(input("Enter cropped image width = "))
img = cv.imread ("Images\lena.jpg",0)
#img = cv.imread ("G:\GoogleDrive\SU\CSE-431(IPCV)\Lab\IPCV Lab\Images\lena.jpg",0)
size = img.shape
rows = size[0]
cols = size[1]
# validate total image rows and cols so that 
# given input for x+h and y+w don't exceed normal image's rows and cols values.
if rows <= (x+h):
    print("Invalid entry for height.")
elif cols <= (y+w):
    print("Invalid entry for width.")
else:
    # cropping image
    crop_img = img[x:x+h, y:y+w]
    cv.imshow("cropped", crop_img)
    cv.waitKey(0)