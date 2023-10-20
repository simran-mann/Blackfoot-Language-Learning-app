####CMPT 120 FINAL PROJECT- SUBMISSION 2
####Author: Simran Mann
####Date: December 1st 2022
import pygame
import cmpt120image
import draw_mu1
import random as r
###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

def displaymenu():
    for i in range(len(menulist)):
        print(menulist[i])

    option = input("choose an option:")
    return option


def img(word):
    img1= "images/"+word+".png"
    return img1

def randomTF():
    num=r.randrange(10)
    if num%2 ==0:
        return True
    else:
        return False



menulist=["MAIN MENU", "1. Learn- Word Flashcards", "2. Play- Seek and Find Game", "3. Settings- Change Difficulty", "4. Exit"]

file = open("blackfoot.csv")
list= []
for line in file:
    linelist= line.strip().split(",")
    list.append(linelist[0])


rec= displaymenu()
challengeList= []
num_learn_words = 3

counter2 = 1

while int(rec) != 4:
    if int(rec) == 1:
        print("LEARN")
        if num_learn_words == 3 : ## first time user learns the first 3 words in the csv file
            counter = 1
            for i in range(3):
                image= img(list[i])
                image1= cmpt120image.getImage(image)
                canvas= cmpt120image.getWhiteImage(400, 300)
                draw_mu1.drawItem(canvas, image1, r.randrange(200), r.randrange(200))
                cmpt120image.showImage(canvas)
                playSound(list[i], ENV)
                print(counter, ". Press Enter to Continue")
                input("")
                challengeList.append(list[i])
                counter +=1
        elif num_learn_words != 3:
            counter2 = 1
            for i in range(num_learn_words):
                image= img(list[i])
                image1= cmpt120image.getImage(image)
                canvas= cmpt120image.getWhiteImage(400, 300)
                draw_mu1.drawItem(canvas, image1, r.randrange(200), r.randrange(200))
                cmpt120image.showImage(canvas)
                playSound(list[i], ENV)
                print(counter2, ". Press Enter to Continue")
                input("")
                challengeList.append(list[i])
                counter2 +=1
        rec= displaymenu()
        continue

    if int(rec)==2:
        print("This is a seek and count game. Listen to a word, and count how many of that item are in the image.")
        num_rounds = int(input("How many rounds would you like to play?"))
        for i in range(num_rounds):
            imgList = []

            if len(challengeList) >0:
                r.shuffle(challengeList)
                challengeList2=challengeList[:3]
                print(challengeList2)
            else:
                challengeList = list[:3]


            img_to_be_guessed = challengeList2[0]
            canvas= cmpt120image.getWhiteImage(400, 300)
            for i in range(len(challengeList2)):
                image = img(challengeList[i])
                image1= cmpt120image.getImage(image)
                color= [r.randrange(255), r.randrange(255), r.randrange(255)]
                while color == [250, 250, 250]:
                    color= [r.randrange(255), r.randrange(255), r.randrange(255)]
                image1= draw_mu1.recolorImage(image1, color)
                mirror= randomTF()
                minify = randomTF()
                if mirror:
                    draw_mu1.mirror(image1)
                if minify:
                    draw_mu1.minify(image1)
                imgList.append(image1)
            for i in range(len(imgList)):
                if i == 0:
                    special_num = r.randrange(1, 4)
                    canvas= draw_mu1.distributeItems(canvas, imgList[i], special_num)
                    playSound(list[list.index(img_to_be_guessed)], ENV)
                    print("...")
                else:
                    num_draw = r.randrange(1,4)
                    canvas= draw_mu1.distributeItems(canvas, imgList[i], num_draw)

            cmpt120image.showImage(canvas)
            print(special_num)
            guess= input("Listen to the word. How many of them do you see?")

            if int(guess) == special_num:
                input("Right! Press enter to continue")
            elif int(guess) != special_num and special_num == 1:
                input("Sorry, there was "+str(special_num)+" . Press enter to continue")
            else:
                input("Sorry, there were "+str(special_num)+" . Press enter to continue")
        rec = displaymenu()
        continue

    if int(rec) == 3:
        num_learn_words=int(input("You are currently learning "+str(num_learn_words)+" words.How many would you like to learn? (3-"+str(len(list))+")"))
        if num_learn_words > len(list) or num_learn_words <3:
            num_learn_words = 3
            print("Sorry that is not a valid number.Resetting to 3 words")
        rec= displaymenu()
        continue

    else:
        rec=input("Sorry that is not a valid number. Please choose option 1-4: ")
        rec= displaymenu()
        continue

if int(rec) == 4:
    print("Goodbye!")




