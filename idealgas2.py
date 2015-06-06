#Connor Marrs 6/1/15: In this code, I am trying to make an ideal gas
#law calculator that gives the volume of a gas in amounts of 1-25 moles.
gasname = input("What is the name of the gas?:")

def idealgas(atm,mol,kel):
    idealgas = float(kel)*float(mol)*float(0.08206)/float(atm)
    return (idealgas)

for mol1 in range(0,25):
    vol=idealgas(1,mol1,500)
    print vol