# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def prosti_brojevi(b):
    if b == 1:
        return False
    if b == 2:
        return True
    if b > 2 and b % 2 ==0:
        return False
    for i in range(2,int(b**0.5)+1):
        if b % i == 0:
            return False
    return True
sum = 0
for i in range(2,2000000):
    if prosti_brojevi(i):
        sum = sum + i

print(sum)


# 142913828922