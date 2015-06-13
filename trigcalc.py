#In this code, I am attempting to make a triginometry calculator that completes two obejctives, determines the third side of right triangle given two other other sides, and also calculates the tangent of an angle given the lengths of the sides of a triangle.

import math

def tangent(side2,side3):
    tangent = float(side3)/float(side2)
    return (tangent)

def pythagorus(side1,side2):
    pythagorus = (float(side1)**2 + float(side2)**2)**0.5
    return (pythagorus)
    
print"If you want to calculate the tangent of an angle, press 1. If you want to calculate the thrid side of a right triangle, press 2"
userchoice = input("Type 1 or 2:\n")
if userchoice == 1:
        side1 = input("The length of side one is: ")
        side2 = input("The length of side two is: ")
        side3 = input("The length of side three is: ")
        
        if float(side1 + side2) <= side3:
            print"This is not a triangle"
        
        else:
            a = tangent(side2,side3)
            x = "The tangent of the angle between sides one and two is %20f." %(a)
            print x

if userchoice == 2:
    side1 = input("The length of side 1 is: ")
    side2 = input("The length of side 2 is: ")
    
    b = pythagorus(side1,side2)
    y = "The length of the hypotenuse is %15f." %(b)
    print y
