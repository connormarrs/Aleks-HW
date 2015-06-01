#Connor Marrs May 18, 2015
#In this program, I am trying to create an ideal gas law calculator.

gasname = input("What is the name of the gas?:")

def idealgas(atm,mol,kel):
    idealgas = float(kel)*float(mol)*float(0.08206)/float(atm)
    return (idealgas)

vol=idealgas(1,5,500)
a="The volume of %s is %20f." % (gasname,vol)
print a
 #Refactored this with Aleks on 6/1/15
