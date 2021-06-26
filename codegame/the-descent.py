import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

mountain=[]
henk =0 
temp=[]
# game loop
while True:
    while henk < 8:
        mountain_h = int(input()) # represents the height of one mountain.
        mountain.append(mountain_h)
        henk +=1
    temp=mountain
    temp.reverse()
    while temp == True:
        x= temp[0]
        temp.remove(x)
        h= mountain.index(x)
        uitkomst=(str(h)) 
        print(uitkomst)



