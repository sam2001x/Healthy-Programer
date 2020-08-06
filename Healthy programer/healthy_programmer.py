#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
  
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            break

def log(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    #musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_excersice = time()
    watersecs = 40*60
    exsecs = 45*60
    eyessecs = 35*60

    while True:
        if time() - init_water > watersecs:
            print("water drinking time. enter 'drank' to stop the alarm")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log("drank water at")

        if time() - init_eyes > eyessecs:
            print("eyes excersice  time. enter 'done' to stop the alarm")
            musiconloop('eyes.mp3', 'done')
            init_eyes = time()
            log("eyes relaxed at")

        if time() - init_excersice > exsecs:
            print("physical activity  time. enter 'done' to stop the alarm")
            musiconloop('excersice.mp3', 'done')
            init_excersice = time()
            log("done exercise at")
    


      