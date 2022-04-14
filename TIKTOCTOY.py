from ast import While
from math import gamma
from pickle import TRUE
from re import X

game=[[" "," "," "],
      [" "," "," "],
      [" "," "," "]]
def check(): 
    if c1==1:
       name="computer"
    elif c1==2:
        name="user"
    if game[0][0]=="X"  and  game[0][1]=="X" and  game[0][2]=="X" : 
        print("win computer ")
    if game[1][0]=="X"  and  game[1][1]=="X" and  game[1][2]=="X" : 
        print("win computer ")
    if game[2][0]=="X"  and  game[2][1]=="X" and  game[2][2]=="X" : 
        print("win computer ")    

    if game[0][0]=="X"  and  game[1][0]=="X" and  game[2][0]=="X" : 
        print("win computer ")
    if game[0][1]=="X"  and  game[1][1]=="X" and  game[2][1]=="X" : 
        print("win computer ")
    if game[0][2]=="X"  and  game[1][2]=="X" and  game[2][2]=="X" : 
        print("win computer ")
        
    if game[0][0]=="X"  and  game[1][1]=="X" and  game[2][2]=="X" : 
        print("win computer ")
    if game[0][2]=="X"  and  game[1][1]=="X" and  game[2][0]=="X" : 
        print("win computer ")



    if game[0][0]=="O"  and  game[0][1]=="O" and  game[0][2]=="O" : 
        print("win USER ")
    if game[1][0]=="O"  and  game[1][1]=="O" and  game[1][2]=="O" : 
        print("win USER ")
    if game[2][0]=="O"  and  game[2][1]=="O" and  game[2][2]=="O" : 
        print("win USER ")    

    if game[0][0]=="O"  and  game[1][0]=="O" and  game[2][0]=="O" : 
        print("win USER ")
    if game[0][1]=="O"  and  game[1][1]=="O" and  game[2][1]=="O" : 
        print("win USER ")
    if game[0][2]=="O"  and  game[1][2]=="O" and  game[2][2]=="O" : 
        print("win USER ")
        
    if game[0][0]=="O"  and  game[1][1]=="O" and  game[2][2]=="O" : 
        print("win USER ")
    if game[0][2]=="O"  and  game[1][1]=="O" and  game[2][0]=="O" : 
        print("win USER ")  


for row in game:
        print(row)
while True:
    print("p1")
    
    while True:
        row=int(input())
        col=int(input())  
        if 0 <=row<=2 and 0 <=col <=2:
            if game[row][col]==" ":
                game[row][col]   ="x"
                break
            else:
                    print("try again")  
        else:
            print("enter the saf number")             
    for row in game:
        print(row)
    print("p2")
    while True:
        row=int(input())    
        col=int(input())
        if 0 <=row<=2 and 0 <=col <=2:
            if game[row][col]==" ":
                game[row][col]   ="o" 
                break
            else:
                    print("try again")  
        else:
            print("enter the saf number")  
    for row in game:
        print(row)
