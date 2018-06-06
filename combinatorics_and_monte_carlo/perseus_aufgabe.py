import random

# set up the three caves
caves = [1,2,3]
# initialze counters for the two possible outcomes
counter_andromeda_in_original_cave = 0
counter_andromeda_in_third_cave = 0

trials = 10000
for trial in range(trials):
    andromeda_in = random.choice(caves)
    perseus_guess = random.choice(caves)
    remaining_caves = [
        c for c in caves if c not in (andromeda_in, perseus_guess)
        ]
    pegasus_hint = random.choice(remaining_caves)
    if andromeda_in == perseus_guess:
        counter_andromeda_in_original_cave += 1
    elif andromeda_in == pegasus_hint:
        raise RuntimeError("Oops, this shouldn't have happened!")
    else:
        counter_andromeda_in_third_cave += 1

print(
    'Reconsidering his original choice would have been good for Perseus in '
    '{0} out of {1} cases.'
    .format(counter_andromeda_in_third_cave, trials)
    )
    
