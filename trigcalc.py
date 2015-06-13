#In this code, I am attempting to make a triginometry calculator that completes two obejctives, determines the third side of right triangle given two other other sides, and also calculates the tangent of an angle given the lengths of the sides of a triangle.

import math

def tangent(side2,side3):
    tangent = float(side3)/float(side2)
    return (tangent)

def pythagorus(side1,side2):
    pythagorus = (float(side1)**2 + float(side2)**2)**0.5
    return (pythagorus)

side1 = input("The length of side one is: ")
side2 = input("The length of side two is: ")
side3 = input("The length of side three is: ")

if float(side1 + side2) <= side3:
    print"This is not a triangle"
else:
    a = tangent(side1,side2)
    x = "The tangent of the angle between sides one and two is %20f." %(a)
    print x

    b = pythagorus(side1,side2)
    y = "The length of the hypotenuse is %15f." %(b)
    print y
