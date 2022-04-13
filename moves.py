import cube
#In this file I will define all of the different moves that can be made
#Reference the document to learn more about each move and how they affect the cube

#You can move a rubiks cube planes both clockwise and counterclockwise
#Instead of writing new algorithms to go counterclockwise, I will just be using a for loop to move them around 3 times
#Because many of the algorithms use each movement twice, noted as U2, R2, F2, etc.

def U(): #Moves the upper horizontal plane of the cube clockwise
    cube.white = cube.white[::-1]#reverses array
    cube.white = cube.white.transpose#transposes array
    
    tempg = [cube.green[0][0], cube.green[0][1], cube.green[0][2]] #created temp green array
    tempo = [cube.orange[0][0], cube.orange[0][1], cube.orange[0][2]] #created temp orange array
    tempb = [cube.blue[0][0], cube.blue[0][1], cube.blue[0][2]] #created temp blue array
    tempr = [cube.red[0][0], cube.red[0][1], cube.red[0][2]] #created temp red array
    
    #switching green with red, orange with green, blue with orange, and red with blue
    cube.green[0][0],cube.green[0][1],cube.green[0][2] = tempg[0],tempg[1],tempg[2]
    cube.blue[0][0],cube.blue[0][1],cube.blue[0][2] = tempb[0],tempb[1],tempb[2]
    cube.red[0][0],cube.red[0][1],cube.red[0][2] = tempr[0],tempr[1],tempr[2]
    cube.orange[0][0],cube.orange[0][1],cube.orange[0][2] = tempo[0],tempo[1],tempo[2]

def U2():#Movement of U twice
    for i in range(2):
        U()

def u(): #Opposite movement of U
    for i in range(3):
        U()

def D(): #Moves the lower horizontal plane of the cube clockwise
    cube.yellow = cube.yellow[::-1]
    cube.yellow = cube.yellow.transpose()
    
    
    tempb = [cube.blue[2][0],cube.blue[2][1],cube.blue[2][2]]
    tempg = [cube.green[2][0],cube.green[2][1],cube.green[2][2]]
    tempr = [cube.red[2][0],cube.red[2][1],cube.red[2][2]] 
    tempo = [cube.orange[2][0],cube.orange[2][1],cube.orange[2][2]]
    

    tempg,tempo,tempb,tempr = tempo,tempb,tempr,tempg

    cube.green[2][0],cube.green[2][1],cube.green[2][2] = tempg[0],tempg[1],tempg[2]
    cube.orange[2][0],cube.orange[2][1],cube.orange[2][2] = tempo[0],tempo[1],tempo[2]
    cube.blue[2][0],cube.blue[2][1],cube.blue[2][2] = tempb[0],tempb[1],tempb[2]
    cube.red[2][0],cube.red[2][1],cube.red[2][2] = tempr[0],tempr[1],tempr[2]

def D2():#Movement of D twice
    for i in range(2):
        D()

def d():#Opposite movement of D
    for i in range(3):
        D()
    
def L(): #Moves the left vertical plane of the cube down
    cube.orange = cube.orange[::-1]
    cube.orange = cube.orange.transpose()

    tempg = [cube.green[0][0],cube.green[1][0],cube.green[2][0]]
    tempw = [cube.white[0][0],cube.white[1][0],cube.white[2][0]]
    tempb = [cube.blue[2][2],cube.blue[1][2],cube.blue[0][2]]
    tempy = [cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0]]

    tempw,tempb,tempy,tempg = tempb,tempy,tempg,tempw

    cube.green[0][0],cube.green[1][0],cube.green[2][0] = tempg[0],tempg[1],tempg[2]
    cube.white[0][0],cube.white[1][0],cube.white[2][0] = tempw[0],tempw[1],tempw[2]
    cube.blue[2][2],cube.blue[1][2],cube.blue[0][2] = tempb[0],tempb[1],tempb[2]
    cube.yellow[0][0],cube.yellow[1][0],cube.yellow[2][0] = tempy[0],tempy[1],tempy[2]

def L2():#Movement of L twice
    for i in range(2):
        L()

def l():#Opposite movement of L
    for i in range(3):
        L()

def F(): #Moves the front face of the cube clockwise
    cube.green = cube.green[::-1]
    cube.green = cube.green.transpose()

    tempr = [cube.red[0][0],cube.red[1][0],cube.red[2][0]]
    tempw = [cube.white[2][0],cube.white[2][1],cube.white[2][2]]
    tempo = [cube.orange[2][2],cube.orange[1][2],cube.orange[0][2]]
    tempy = [cube.yellow[0][0],cube.yellow[0][1],cube.yellow[0][2]]
    
    tempw,tempo,tempy,tempr = tempo,tempy,tempr,tempw

    cube.orange[0][2],cube.orange[1][2],cube.orange[2][2] = tempo[0],tempo[1],tempo[2]
    cube.white[2][0],cube.white[2][1],cube.white[2][2] = tempw[0],tempw[1],tempw[2]
    cube.yellow[0][2],cube.yellow[0][1],cube.yellow[0][0] = tempy[0],tempy[1],tempy[2]
    cube.red[0][0],cube.red[1][0],cube.red[2][0] = tempr[0],tempr[1],tempr[2]

def F2():#Movement of F twice
    for i in range(2):
        L()
    
def f():#Opposite movement of F
    for i in range(3):
        L()
    
def R(): #Moves the right vertical plane of the cube up
    cube.red = cube.red[::-1]
    cube.red = cube.red.transpose()

    tempg = [cube.green[0][2],cube.green[1][2],cube.green[2][2]]
    tempw = [cube.white[0][2],cube.white[1][2],cube.white[2][2]]
    tempb = [cube.blue[2][0],cube.blue[1][0],cube.blue[0][0]]
    tempy = [cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2]]

    tempw,tempb,tempy,tempg = tempg,tempw,tempb,tempy

    cube.green[0][2],cube.green[1][2],cube.green[2][2] = tempg[0],tempg[1],tempg[2]
    cube.white[0][2],cube.white[1][2],cube.white[2][2] = tempw[0],tempw[1],tempw[2]
    cube.blue[2][0],cube.blue[1][0],cube.blue[0][0] = tempb[0],tempb[1],tempb[2]
    cube.yellow[0][2],cube.yellow[1][2],cube.yellow[2][2] = tempy[0],tempy[1],tempy[2]

def R2():#Movement of R twice
    for i in range(2):
        R()

def r():#Opposite movement of R
    for i in range(3):
        R()
    
def B(): #Moves the back plane of the field clockwise(when facing that plane, CCW when looking at it from the front)
    cube.blue = cube.blue[::-1]
    cube.blue = cube.blue.transpose()

    tempw = [cube.white[0][0],cube.white[0][1],cube.white[0][2]]
    tempo = [cube.orange[0][0],cube.orange[1][0],cube.orange[2][0]]
    tempy = [cube.yellow[2][2],cube.yellow[2][1],cube.yellow[2][0]]
    tempr = [cube.red[0][2],cube.red[1][2],cube.red[2][2]]

    tempw,tempo,tempy,tempr = tempr,tempw,tempo,tempy

    cube.white[0][0],cube.white[0][1],cube.white[0][2] = tempw[0],tempw[1],tempw[2]
    cube.orange[2][0],cube.orange[1][0],cube.orange[0][0] = tempo[0],tempo[1],tempo[2]
    cube.yellow[2][0],cube.yellow[2][1],cube.yellow[2][2] = tempy[0],tempy[1],tempy[2]
    cube.red[0][2],cube.red[1][2],cube.red[2][2] = tempr[0],tempr[1],tempr[2]

def B2():#Movement of B twice
    for i in range(2):
        B()

def b():#Opposite movement of B
    for i in range(3):
        B()
    


