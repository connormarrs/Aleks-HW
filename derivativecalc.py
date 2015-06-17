#In this code, I am attempting to make a calculator that accepts a cubic function and return the function's derivative.
import math

def cube(coef):
    cube = float(coef)*3
    return(cube)

def square(coef):
    square = float(coef)*2
    return(square)

print"type the coefficients of a cubic equation in the form of ax^3 + bx^2 + cx + d"
a = input("What is a in this equation:\n")
b = input("What is b in this equation:\n")
c = input("What is c in this equation:\n")

da = cube(a)
db = square(b)

print"This function's derivative is %fx^2 + %fx + %f" %(da,db,c)