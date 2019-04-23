# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def najveci_moguci_broj(digits):
    broj = 0
    for i in range(digits):
        broj = broj + ((10**i))*9
    return broj
n = 3
broj = 0
for i in range(najveci_moguci_broj(n)+1):
    for j in range(najveci_moguci_broj(n)+1):
        polindrom = i * j
        if str(polindrom) == str(polindrom)[::-1]:
            if polindrom > broj:
                broj = polindrom
print(broj)
# resenje 906609