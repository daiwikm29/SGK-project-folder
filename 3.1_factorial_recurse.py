factorialInput = input("What number would you like to take the factorial of: ")

def factorialFinder(n):
    #base case
    if n==0 or n==1: return 1
    #recursive case
    elif n>1:
        print(n)
        return n*factorialFinder(n-1)

print()

print(factorialFinder(int(factorialInput)))