# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between
# the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of
# the squares of the first one hundred natural numbers and the square of the sum.

def zbir_kvadrata_broja(broj):
    resenje = 0
    for i in range(0,broj+1):
        resenje = resenje + (i**2)
    return resenje
def kvadrat_zbira_broja(broj):
    resenje = 0
    for i in range(0,broj+1):
        resenje = resenje + i
    return resenje**2
brojevi = 100
print(kvadrat_zbira_broja(brojevi)-zbir_kvadrata_broja(brojevi))