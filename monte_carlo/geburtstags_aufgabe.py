# Geburtstagsparadoxon
#
# siehe auch:
# https://de.wikipedia.org/wiki/Geburtstagsparadoxon

import random


def calculate_likelihood_for_2_out_of_n(n):
    count_trials_with_people_with_same_birthday = 0
    trials = 10000
    for trial in range(trials):
        birthdays = set(random.choices(range(365), k=n))
        if len(birthdays) < n:
            count_trials_with_people_with_same_birthday += 1
    return count_trials_with_people_with_same_birthday / trials

# TO DO:
# Turn this into a program that asks the user for the number of people
# in the room, then outputs the chances that two or more of them have the
# same birthday!
