while True:
    factorialInput = input("What number would you like to take the factorial of: ")
    past_searches = {}

    def factorialFinder(n):
        #base case
        if n==0 or n==1: return 1
        elif n in past_searches: n = past_searches[n]
        #recursive case
        elif n>1:
            return n*factorialFinder(n-1)

    print()

    print(factorialFinder(int(factorialInput)))
    past_searches[int(factorialInput)] = factorialFinder(int(factorialInput))