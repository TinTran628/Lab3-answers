'''
Author: Tin
KUID: 3175049
Date: 02/21/2025
Lab: lab3
Last modified: 02/21/2025
Purpose: Using ASCII
''' 

print ("1) Select a specific number\n2) Display visible ASCII values (33 to 126)\n3) Exit")
Choice = input ("Choice:")

while Choice != "3":
    if Choice == "1":
        Value = int(input("Enter a value:"))
        if Value >= 33 and Value <= 126:
            print (Value, "=", chr(Value))
            print ("\n1) Select a specific number\n2) Display visible ASCII values (33 to 126)\n3) Exit")
            Choice = input ("Choice:")
        else:
            print ("------------------------------\nTheres been an error\n------------------------------")
            print ("1) Select a specific number\n2) Display visible ASCII values (33 to 126)\n3) Exit")
            Choice = input ("Choice:")
    elif Choice == "2":
        for num in range(33,127):
            print (num, "=", chr(num))
        print ("\n1) Select a specific number\n2) Display visible ASCII values (33 to 126)\n3) Exit")
        Choice = input ("Choice:")
    else:
        print ("------------------------------\nTheres been an error\n------------------------------")
        print ("1) Select a specific number\n2) Display visible ASCII values (33 to 126)\n3) Exit")
        Choice = input ("Choice:")
print ("\n------------------------------\nEnding Program\nExiting......\n------------------------------\n")