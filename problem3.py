# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

broj = 13195
broj_veci = 600851475143
najveci_prost_broj = 0


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
for i in range(2,broj_veci+1):
    if prosti_brojevi(i) and broj_veci % i == 0:
        print(i)

# resenje 6857