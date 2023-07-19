import tkinter as tk

from automatic import automtic_oranges

sizeList, colorIndexList = automtic_oranges("4.bmp")
m=0
my_list = [[0 , 0, sizeList[i], 0, colorIndexList[i]] for i in range(len(sizeList))]
print(my_list)