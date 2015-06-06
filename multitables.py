#Connor Marrs 6/1/15: In this program, I am trying to make a program that prints multiplication tables. To do this, I will use a for loop.
def mult(range1, range2):
    mult = range1*range2
    return (mult)

for range1 in range(1,13):
    for range2 in range(1,13):
        table = mult(range1,range2)
        print table