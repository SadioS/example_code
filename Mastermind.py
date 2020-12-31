# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 23:17:00 2019

@author: sadio_aya5cf2
"""

import random
print ("\n                     ~MASTERMIND~\n        " )
print("The goal of the game is to guess the code, which is a combination of 4 digit between 1 and 4. Each digit may appear several times, at different places. \nYou have ten attempt. \n")
print("After each attempt, the game give you some clue:\n   -A black pawn means that you have discover 1 digit of the winning combination at the good place\n   -A white pawn means that you have discover 1 digit of the winning combination, but placed in the wrong place" )
print("\nThe game will stop when you have guess the good combination. After 10 attempts,  if you have not discover the good combination, the winning combination will be given to you. \nGood Luck!!\n\n")

a= random.randint(1,4) #permet de génerer à chaque partie un chiffre différent
b= random.randint(1,4)
c= random.randint(1,4)
d= random.randint(1,4)

L1= [a,b,c,d] #permet de former l'enchainement de chiffre à déterminer
r=10
for i in range (10):
    
 #ici on demande au joueur d'entrer l'enchainement de chiffre   
    e= int(input("Enter a number between 1 and 4: "))
    f= int(input("Enter a number between 1 and 4: "))
    g= int(input("Enter a number between 1 and 4: "))
    h= int(input("Enter a number between 1 and 4: "))
    print("")
    print("")
    
    L3=L1.copy()
    
    L2= [e,f,g,h]
    n=0
    b=0
    print ("The combination you propose is:", L2)
    for k in range (4):
        if L1[k]==L2[k]:
            n=n+1
            L3[k]=0
            L2[k]=5

    for k in range (4):
        for j in range (4):
            if k != j:
                if L3[k]==L2[j]:
                    b=b+1
                    L3[k]=0
                    L2[j]=5
                    break             
    if n==4:
        print("Congratulation! You have found the answer!!")
        break
    #si le joueur trouve le bon enchainement, le jeu s'arrête
        
    else:
        r=r-1
        print ("You have", b, "white pawn(s)", n, "black pawn(s). \nYou have", r, "chances left.")
   
        
print("The good combination is:", L1)
print("")
print("")