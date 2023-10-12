import numpy as np
import random
import curses

M = np.zeros((4, 4), dtype=int)
# print(M[0, 0], M[0, -1], M[-1, 0], M[-1, -1]) # topLeft, topRight, bottomLeft, bottomRight
longY = len(M[:, 0])
longX = len(M[0, :])

nbTry = 0

valWeights = (0.7, 0.27, 0.03)
valEndRound = (2, 4, 8)

def checkIfPlayable():
    bool = False
    for j in range (longY):     
        for i in range (longX-1):
            if (M[j, i] == M[j, i+1]):
                bool = True
    for i in range (longX):
        for j in range (longY-1):
            if (M[j, i] == M[j+1, i]):
                bool = True
    return bool

def endRound():
    global nbTry
    nbTry += 1
    if 0 not in M :
        if not checkIfPlayable():
            print(f'Lost in {nbTry} tries !')
            return False
        return True
    else :
        randX = random.randint(0, longX-1)
        randY = random.randint(0, longY-1)
        while (M[randY, randX] != 0):
            randX = random.randint(0, longX-1)
            randY = random.randint(0, longY-1)
        M[randY, randX] = random.choices(valEndRound, weights=valWeights)[0]
        return True
    
def additionBox(direction):
    boolAddition = False
    if direction == 3 or direction == 1: # right or left
        for j in range (longY):
            for i in range (longX-1):
                if (M[j, i] != 0 and M[j, i] == M[j, i+1]):
                    boolAddition = True
                    M[j, i+1] *= 2 if (direction == 3) else 0
                    M[j, i] *= 0 if (direction == 3) else 2
                    
    if direction == 2 or direction == 5: # bottom or top
        for i in range (longX):
            for j in range (longY-1):
                if (M[j, i] != 0 and M[j, i] == M[j+1, i]):
                    boolAddition = True
                    M[j+1, i] *= 2 if (direction == 2) else 0
                    M[j, i] *= 0 if direction == 2 else 2
    return boolAddition

def shiftBox(direction):
    boolShift = False
    if direction == 3: # right
        for j in range (longY):     
            for i in range (longX-1):
                if (M[j, i+1] == 0 and M[j, i] != 0):
                    M[j, i+1], M[j, i] = M[j, i], 0
                    boolShift = True
    elif direction == 1: # left
        for j in range (longY):     
            for i in range (1, longX):
                if (M[j, -i-1] == 0 and M[j, -i] != 0):
                    M[j, -i-1], M[j, -i] = M[j, -i], 0
                    boolShift = True
    elif direction == 2: # bottom
        for i in range (longY):     
            for j in range (longX-1):
                if (M[j+1, i] == 0 and M[j, i] != 0):
                    M[j+1, i], M[j, i] = M[j, i], 0
                    boolShift = True
    else: # direction = 5, top
        for i in range (longY):     
            for j in range (1, longX):
                if (M[-j-1, i] == 0 and M[-j, i] != 0):
                    M[-j-1, i], M[-j, i] = M[-j, i], 0
                    boolShift = True
    return boolShift
    
        
def action(stdscr):
    isPlaying = True
    endRound()
    while isPlaying:
        stdscr.clear()
        stdscr.addstr(f'------------ ROUND N°{nbTry} ------------\n')
        stdscr.addstr(str(M) + '\n')
        stdscr.addstr('-----------------------------------\n')

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            n = 1
        elif key == curses.KEY_UP:
            n = 5
        elif key == curses.KEY_DOWN:
            n = 2
        elif key == curses.KEY_RIGHT:
            n = 3
        else:
            continue

        boolAddition = True
        boolShift = True

        while boolAddition or boolShift:
            boolAddition = additionBox(n)
            boolShift = shiftBox(n)

        isPlaying = endRound()

curses.wrapper(action)