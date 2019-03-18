from graphics import *
import math
import random

def main():
    win = GraphWin("Packet Switching", 1000, 500)
    win.setBackground('Black')
    
    while True:
        active = 0
        for x in range(0, 36):
            if random.randint(0, 10) == 1:
                active += 1
        active2 = active
        for i in range(0, 900, 100):
            for j in range(0, 400, 100):
                cir = Circle(Point(i + 100, j + 100), 30)
                cir.setFill('White')
                cir.draw(win)
        while active > 0:
            cir = Circle(Point(random.randint(1, 9)*100, random.randint(1, 4)*100), 30)
            cir.setFill('Blue')
            cir.draw(win)
            active -= 1
        text = "There are {} active users".format(active2)
        message = Text(Point(500,50), text)        message.setTextColor('White')        message.draw(win)
        active2 = 0
        time.sleep(1)
        message.undraw()

main()
