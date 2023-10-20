## CMPT 120 FINAL PROJECT PART 1: DRAW.PY FUNCTIONS
## Simran Mann
## November 21 2022


import cmpt120image
import random as r


apples = cmpt120image.getImage("images/apples.png")
bread = cmpt120image.getImage("images/bread.png")
burger = cmpt120image.getImage("images/burger.png")
child = cmpt120image.getImage("images/child.png")
coffee = cmpt120image.getImage("images/coffee.png")
dog = cmpt120image.getImage("images/dog.png")
door = cmpt120image.getImage("images/door.png")
eggs = cmpt120image.getImage("images/eggs.png")
fish = cmpt120image.getImage("images/fish.png")
oranges = cmpt120image.getImage("images/oranges.png")
salt = cmpt120image.getImage("images/salt.png")
tipi = cmpt120image.getImage("images/tipi.png")

canvas = cmpt120image.getWhiteImage(400,300)  ## for last 2 functions

def recolorImage(img,color):
    ##create a new image
    newImg= cmpt120image.getBlackImage(len(img[0]), len(img))

    for row in range(len(img)):
            for col in range(len(img[0])):
                if img[row][col]== [255, 255, 255]:  ###if the pixel is white
                    newImg[row][col]= img[row][col]  ###then the piexl in the new image is white

                else :
                    newImg[row][col]= color

    return newImg

## test the function
#cmpt120image.showImage(child)
#input("....")
#res = recolorImage(child,[0,255,0])
#cmpt120image.showImage(res)
#input("....")


def minify(img):

    newImg= cmpt120image.getBlackImage(len(img[0])//2, len(img)//2)

    for row in range(len(newImg)):
        for col in range(len(newImg[0])):
            listRGB=[]
            for i in [0, 1, 2]:
                avgRGB= (img[2*row][2*col][i]+img[2*row][(2*col)+1][i]+img[(2*row)+1][2*col][i]+img[(2*row)+1][(2*col)+1][i])/4
                listRGB.append(int(avgRGB))

            newImg[row][col]= listRGB

    return newImg

##test the function
#cmpt120image.showImage(child)
#input("....")
#res = minify(child)
#cmpt120image.showImage(res)
#input("....")



def mirror(img):
  # Add your code here
    newImg= cmpt120image.getBlackImage(len(img[0]), len(img))
    for row in range(len(img)):
        for col in range(len(img[0])):
            newpos= (len(img[0])-col-1)
            newImg[row][col]=img[row][newpos]

    return newImg

##test the function
#cmpt120image.showImage(child)
#input("continue....")
#mirrorImg=mirror(child)
#cmpt120image.showImage(mirrorImg)


def drawItem(canvas, item,row,col):
  # Add your code here
    for r in range(len(item)):
        for c in range(len(item[0])):
            if r+row >= len(canvas) or c+col >= len(canvas[0]):
                continue
            if item[r][c] != [255, 255, 255]:
                canvas[r+row][c+col]=item[r][c]

    return canvas


def distributeItems(canvas,item,n):
    for i in range(n):
        row= r.randrange(250)
        col=r.randrange(150)
        drawItem(canvas, item, row, col)

    return canvas

##test the function
#img = cmpt120image.getImage("images/child.png")
#res= distributeItems(canvas, img, 4)
#cmpt120image.showImage(res)
