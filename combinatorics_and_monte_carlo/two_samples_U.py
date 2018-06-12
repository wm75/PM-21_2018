import random
import math


def calc_U (series1, series2):
    # TO DO
    # follow the simple Method 1 illustrated under
    # https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test#Calculations
    return 0


def calc_z_prob (z):
    # TO DO
    # to implement with random gaussian sampling
    # i.e. randomly draw values from a standard gaussian distribution and
    # see how many of them are equally or more extreme than z.
    return 0


# Wachstum in cm von Roggen unter zwei Bedingungen
ohne_N2 = [2.1, 4.1, 2.0, 2.3, 3.1, 3.2, 3.4, 5.0, 3.2, 2.8]
mit_N2 = [3.1, 5.3, 6.2, 6.3, 6.2, 4.0, 4.9, 4.2, 4.5, 4.8]

n1 = len(ohne_N2)
n2 = len(mit_N2)

U_expect = n1 * n2 / 2
sigma_U = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
U = calc_U(ohne_N2, mit_N2)
print(U)

z = (U_expect - U - 0.5) / sigma_U
print('p-Wert (zweiseitiger Test):', calc_z_prob(z))
