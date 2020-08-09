#Investigating stopping distances of cars
#Spencer Organ - KESH Academy
#modified for the purposes of this experiment

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys
import random

sense.clear(0,0,0)

b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
w = (255,255,255)

red_on = [
b,b,w,w,w,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b
]

green_on = [
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,w,w,w,b,b
]

def writeToFile(filename, speed, name, fileobj):
    fileobj.write(str(filename)         + "|")
    fileobj.write(str(speed)            + "|")
    fileobj.write(str(name)             + "|")
    fileobj.write(str(round(elapsed,5)) + "|")
    fileobj.write(str(distance)        + "\n")

def nameOf():
    name = str(raw_input("What is your name? "))
    return name

try:
    file_name = str(raw_input("What day is it? (number) "))
    speed = 65

    f = open("../data/"+file_name+"_n.txt", "a")
    g = open("../data/"+file_name+"_y.txt", "a")

    while 1:
        name = nameOf()
        if name == "q":
            break
        notTexting = True
        for fileobj in [f,g]:
            if notTexting:
                print "Non-Texting Instructions:\nAs soon as you see the green traffic light turn red, press ENTER."
            else:
                print "Texting Instructions:\nStart typing a message saying you will be home late. While typing, when you see the green traffic light turn red, press ENTER."
            msg = str(raw_input("Press ENTER when you are ready to start..."))
            filename = file_name + ("_n" if fileobj == f else "_y")
            sense.set_pixels(green_on)
            time.sleep(random.randint(3,10))
            sense.clear()
            sense.set_pixels(red_on)
            start = time.time()
            msg = raw_input("Press ENTER now!")
            end = time.time()
            sense.clear()
            elapsed = end - start
            print ("You took " + str(round(elapsed,4)) + " seconds to press ENTER.")
            distance = (speed * 0.44704) * elapsed
            print ("At " + str(speed) + " miles per hour you would have travelled " + str(distance) + " meters.")
            writeToFile(filename, speed, name, fileobj)
            notTexting = False
finally:
    try:
        fileobj.close()
        f.close()
        g.close()
    except: pass
    sense.clear()
