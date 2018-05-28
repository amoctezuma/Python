#---Arnold Moctezuma---
# www.arnoldmoctezuma.me
# LinkedIn: linkedin.com/in/arnoldmoctezuma
# GitHub: github.com/amoctezuma

#version 0.1

# simple 'Rock Paper Scissor' game
#   - accepts a single letter string input from user/player, and stores for future use.
#   - selects random letter from tuple(rps)for computer/pc, and stores for future use.
#   - comapres player vs pc with if-elif; from stored data, and print to screen winner.

#!/usr/bin/python
import string
import random

#---RockPaperScissor tuple; ordered and unchangeable collection---]
rps=('r', 'p', 's')

#---get player input choice and store in plyr, skip a line and brint back player choice---]
plyr=input('(r)ock, (p)aper, (s)cissor \n')
print("Player pickerd: " + plyr)

#---random select PC choice and print to screen---]
pc=random.choice(rps)
print("Computer picked: " + pc)

#---compare player and pc choice, print winner---]
if plyr == pc:
    print("It's a tie!")
#--instance where paper wins--]
elif plyr=='r' and pc=='p':
    print("Paper Wins!")
elif plyr=='p' and pc=='r':
    print("Paper wins!")
#--instance where rock wins--]
elif plyr=='r' and pc=='s':
    print("Rock Wins!")
elif plyr=='s' and pc=='r':
    print("Rock Wins")
#--instance where scissor wins--]
elif plyr=='p' and pc=='s':
    print("Scissor wins!")
elif plyr=='s' and pc=='p':
    print("Scissor Wins")
