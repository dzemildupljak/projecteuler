# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def broj_deljiv_1_20(broj):
    for i in range(1,21):
        if broj % i != 0:
            return  False
    return True

broj = 1
while True:
    if broj_deljiv_1_20(broj):
        break
    broj = broj + 1
print(broj)