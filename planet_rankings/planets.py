# Planet data
# -----------
# There is a separate list for every property (names, diameter, etc.)
# of the planets in our solar system.

# The data is taken from:
# https://www.windows2universe.org/?page=/our_solar_system/planets_table.html

# planet names
planets = [
    'Mercury', 'Venus', 'Earth', 'Mars',       # inner planets
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'   # outer planets
    ]
# planet diameter relative to Earth
rel_diameter = [
    0.382, 0.949, 1, 0.532,
    11.209, 9.44, 4.007, 3.883
    ]
# planet mass relative to Earth
rel_mass = [
    0.055, 0.815, 1, 0.107,
    318, 95, 15, 17
    ]
# mean distance from the Sun in astronomic units (AU)
mean_dist = [
    0.39, 0.72, 1, 1.52,
    5.20, 9.54, 19.18, 30.06
    ]
# orbital eccentricity (how much the elliptic orbit deviates from a circle)
eccent = [
    0.2056, 0.0068, 0.0167, 0.0934,
    0.0483, 0.0560, 0.0461, 0.0097
    ]
# number of moons (current estimate for outer planets)
moons = [
    0, 0, 1, 2,
    67, 62, 27, 14
    ]

# End of planet data section


# A list of the properties we have in the data section
properties = [
    'Name', 'Diameter', 'Mass', 'Distance', 'Eccentricity', 'Moons'
    ]
# Wrap the individual property lists into an outer list.
# This way we can deal with them in loops without knowing
# the corresponding identifiers by name.
solar_data = [
    planets, rel_diameter, rel_mass, mean_dist, eccent, moons
    ]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TO DO section
# Here are the functions you need to implement to make things work.

def get_user_selection(options):
    """Present the user with options to choose from and return the selection.

    Prints a "Number - Option" line for every option in options.
    Asks the user to select an option by typing in its number.
    Checks that the input represents a valid selection and returns it.
    """

    pass    # implement the function so that it mentions the docstring here


def sorted_on_attribute(data, sort_row):
    """Return sorted (item, attribute) pairs from a larger data table.

    Expects a data table in the form of a sequence, in which the first
    element is a sequence of item names, and the following elements are
    sequences of values describing one property of the items each.
    sort_row indicates the index in the outer sequence that holds the
    property to sort on. If sort_row is 0, the items are sorted by their
    name and (item name, item name) tuples are returned.

    Example:

    >>> data = [
        ('S.cerevisiae', 'C.elegans', 'H.sapiens', 'E.coli'),  # organisms
        (12156677, 101169000, 3234830000, 4639221),    # haploid genome size
        (16, 6, 23, 1)    # number of chromosomes in the haploid set
        ]
    >>> sorted_on_attribute(data, 2)
    [('E.coli', 1), ('C.elegans', 6), ('S.cerevisiae', 16), ('H.sapiens', 23)]
    
    """

    pass    # implement the function so that it mentions the docstring here
    # Hint: you may want to
    # - zip together the data elements you are interested in
    # - pass the result to sort
    # - loop over the resulting list building up a new list with swapped
    #   elements or
    # - use an appropriate lambda `key` function during sorting
    # This is definitely non-trivial so don't despair if you can't figure it
    # out, but try!

    
if __name__ == '__main__':
    # Here is the main program, which should just work fine if
    # the above two functions are implemented correctly.
    
    print('     Planet Rankings')
    print('     ---------------')
    print()
    print('Nach welcher Eigenschaft soll sortiert werden?')

    selection = get_user_selection(properties)

    for planet, data in sorted_on_attribute(solar_data, selection):
        if selection == 0:
            print(planet)
        else:
            print(planet, data, sep='\t')
