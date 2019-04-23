# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
def prost_broj(broj):
    if broj < 2:
        return False
    for i in range(2,broj//2+1):
        if broj%i == 0:
            return False
    return True
brojac = 0
poslednji_prost_broj = 10001
for i in range(0,99999999):
    if brojac == poslednji_prost_broj:
        print(i-1)
        break
        # print(brojac)
    elif prost_broj(i) and brojac<poslednji_prost_broj:
        brojac +=1

