# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
for a in range(3,1000):
    for b in range(a+1,999):
        c_na_kvadrat = a**2+b**2
        c = c_na_kvadrat**0.5
        if a + b + c == 1000:
                print(a,b,c)
                print(a*b*c)


# a=200 b=375 c=425.0
# a*b*c=31875000.0

