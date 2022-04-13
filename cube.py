from string import whitespace
import numpy as nmpy
#numpy is a open source python library used to work with numerical data. Using this for the faces of the cube.
#Will be using the normal/standard  colors for the faces of the cube(White, Green, Yellow, Red, Blue, Orange)

#Each face is a 3x3 and I will be using a 3D array for each 
white = [
    ["w","w","w"],
    ["w","w","w"],
    ["w","w","w"]
]
white = nmpy.array(white)

red = [
    ["r", "r", "r"],
    ["r", "r", "r"],
    ["r", "r", "r"]
]
red = nmpy.array(red)

green = [
    ["g","g","g"],
    ["g","g","g"],
    ["g","g","g"]
]
green = nmpy.array(green)

yellow = [
    ["y","y","y"],
    ["y","y","y"],
    ["y","y","y"]
]
yellow = nmpy.array(yellow)

blue = [
    ["b","b","b"],
    ["b","b","b"],
    ["b","b","b"]
]
blue = nmpy.array(blue)

orange = [
    ["o","o","o"],
    ["o","o","o"],
    ["o","o","o"]
]
orange = nmpy.array(orange)
