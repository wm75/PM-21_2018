import statistics
import random


# Wachstum in cm von Roggen unter zwei Bedingungen
ohne_N2 = [2.1, 4.1, 2.0, 2.3, 3.1, 3.2, 3.4, 5.0, 3.2, 2.8]
mit_N2 = [3.1, 5.3, 6.2, 6.3, 6.2, 4.0, 4.9, 4.2, 4.5, 4.8]

observed_diff = statistics.mean(mit_N2) - statistics.mean(ohne_N2)
n_ohne_N2 = len(ohne_N2)
n_mit_N2 = len(mit_N2)

n = 50_000
count_one_sided = 0
count_two_sided = 0
combined = mit_N2 + ohne_N2
for trial in range(n):
    random.shuffle(combined)
    diff = (
        statistics.mean(combined[:n_mit_N2])
        - statistics.mean(combined[n_mit_N2:])
        )
    if abs(diff) >= observed_diff:
        count_two_sided += 1
        if diff >= observed_diff:
            count_one_sided += 1

print('p-Wert (einseitiger Test):', count_one_sided/n)
print('p-Wert (zweiseitiger Test):', count_two_sided/n)

