#get user input for degree of polynomial
degree = input("What is the degree of the polynomial you would like to differentiate:\n")

#Write a function that accepts coefficients from the user, for loop to call this n times
def get_coef_from_user(coef_n):
    coef = input("Type coefficient: %s \n" %coef_n)
    return(coef)

list_of_coefs = list()
d_coefs = list()
print

for i in range(0, degree + 1):
    thing_to_extend = get_coef_from_user(i)
    list_of_coefs.extend([thing_to_extend])
    
    #Multiply values by degree of variable & bundle
    other_thing_to_extend = list_of_coefs[i] * (degree - i)
    d_coefs.extend([other_thing_to_extend])

#Print the values (maybe pretty printing)
print"The coefficients of the function are:"
print list_of_coefs
print"The coefficients of the derivative are:"
print d_coefs