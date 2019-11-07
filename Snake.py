import keyboard  # using module keyboard
import requests
from copy import deepcopy

def request(pixels):
    requests.post('http://192.168.178.91/display', json={"pixels": pixels})
    print(pixels)

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
    x=0
    y=0

    pixels = [{"X": x, "Y":y, "R":255, "G":0, "B":0}]
    request(pixels)

    while True:  # making a loop 
        if keyboard.is_pressed('d'):  
            pixels = movePixels(pixels, 0)
            request(pixels)

        if keyboard.is_pressed('a'):  
            pixels = movePixels(pixels, 1)
            request(pixels)

        if keyboard.is_pressed('w'):  
            pixels = movePixels(pixels, 2)
            request(pixels)

        if keyboard.is_pressed('s'):  
            pixels = movePixels(pixels, 3)
            request(pixels)
  
if __name__== "__main__":
  main()

