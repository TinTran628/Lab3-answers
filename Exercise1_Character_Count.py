'''
Author: Tin
KUID: 3175049
Date: 02/14/2025
Lab: lab3
Last modified: 02/14/2025
Purpose: Using loops 
'''



stringinput = input("Enter a string:")
characterinput = input("Enter a character to count:")
character_count = 0
for i in stringinput:
    if i == characterinput:
        character_count = character_count +1
print ("In the string",stringinput," the character 'a' occurs",character_count, "time(s)")

