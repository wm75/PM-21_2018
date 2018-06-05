# Perseus, Pegasus und Andromeda: eine Variante des Ziegenproblems
#
# siehe Seite 7 in:
# www.school-scout.de/vorschau/62770/mathematische-spiele-und-strategien-22012.pdf

import random

# set up the three caves
caves = [1,2,3]
# initialize counters for the two possible outcomes
counter_andromeda_in_original_cave = 0
counter_andromeda_in_third_cave = 0

trials = 10000
for trial in range(trials):
    # simulate and count outcomes
    # TO DO!!
    pass

# report results of simulation
print(
    'Reconsidering his original choice would have been good for Perseus in '
    '{0} out of {1} cases.'
    .format(counter_andromeda_in_third_cave, trials)
    )
    
