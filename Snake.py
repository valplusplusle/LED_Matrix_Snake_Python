import keyboard  # using module keyboard
import requests
from copy import deepcopy
import time
import pickle

def request(pixels):
    requests.post('http://192.168.178.91/display', json={"pixels": pixels})
    print(pixels)

def gameOver():
    print("error")
    pixels = pickle.load(open( "./skullarray", "rb"))
    request(pixels)
    time.sleep(10)

def movePixels(pixels, direction):
    first = deepcopy(pixels[0])
    if direction == 0:
        first["X"] = (first["X"]+1)%16
    if direction == 1:
        first["X"] = (first["X"]-1)%16
    if direction == 2:
        first["Y"] = (first["Y"]+1)%16
    if direction == 3:
        first["Y"] = (first["Y"]-1)%16
    if len(pixels) < 4:
        newPixels = [first]+pixels
    else:
        newPixels = [first]+pixels[:-1]          
    newPixels[1]["R"]=0
    newPixels[1]["G"]=0
    newPixels[1]["B"]=255
    return newPixels

def main():
    x = 0
    y = 0
    direction = 0

    pixels = [{"X": x, "Y":y, "R":255, "G":0, "B":0}]
    request(pixels)

    while True:  # making a loop 
        pixels = movePixels(pixels, direction)
        request(pixels) 

        if keyboard.is_pressed('d'):  
            if direction != 1:
                direction = 0
            else:
                gameOver()

        if keyboard.is_pressed('a'):  
            if direction != 0:
                direction = 1
            else:
                gameOver()

        if keyboard.is_pressed('w'):  
            if direction != 3:
                direction = 2
            else:
                gameOver()

        if keyboard.is_pressed('s'):  
            if direction != 2:
                direction = 3
            else:
                gameOver()

        time.sleep(0.05)
  
if __name__== "__main__":
  main()
