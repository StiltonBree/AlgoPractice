#Collatz Conjecture

#find steps to 1. If n is even, divide by 2, if n is odd, multiply by 3 and add 1

n = int(input("Enter a number: "))
count = 0
while n > 1:
    if (n % 2 == 0):
        n = n/2
    else:
        n = (n * 3) + 1
    count+=1

print("It takes " + str(count) + " steps to get to 1")       