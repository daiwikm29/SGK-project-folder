import random
import time
s = 1000
m = 10000
l = 50000



def listGen(size):
    nums = []
    for i in range(size):
        nums.append(random.randint(0, 100))
    return nums

def logListGen(size):
    return(sorted(listGen(size)))



def linear(nums):
    max = nums[0]
    start = time.perf_counter()
    for i in range(len(nums)):
        if nums[i] > max:   max = nums[i]
    end = time.perf_counter()
    return end-start

def quadratic(nums):
    start = time.perf_counter()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == nums[i]:  dupes = True
    end = time.perf_counter()
    return end - start

def logarithm(nums):
    start = time.perf_counter()
    target = random.randint(0, 100)
    left = 0
    right = len(nums)-1
    
    while left <= right:
        middle = (left + right)/2
        if nums[middle] == target:  targetBool = True
        elif target < nums[middle]: right = middle-1
        else:   left = middle+1 
        
    end = time.perf_counter()
    return end-start

sList = listGen(s)
mList = listGen(m)
lList = listGen(l)

print("Times for Small List Size of 1000")
print("Linear: "+str(linear(sList)))
print("Quadratic: "+str(quadratic(sList)))
print("Logarithmic: "+str(logarithm(sList)))

print()

print("Times for Medium List Size of 10,000")
print("Linear: "+str(linear(mList)))
print("Quadratic: "+str(quadratic(mList)))
print("Logarithmic: "+str(logarithm(mList)))

print()

print("Times for Large List Size of 50,000")
print("Linear: "+str(linear(lList)))
print("Quadratic: "+str(quadratic(lList)))
print("Logarithmic: "+str(logarithm(lList)))