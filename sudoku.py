# -*- coding: utf-8 -*-

rows = 'ABCDEFGHI'
columns = '123456789'

# Write a helper function, cross(a, b), which, given two strings - a and b -
# will return the list formed by all the possible concatenations of a letter char_a in string a with a letter char_b in string b.
# It has to be a two-liner
def cross(a, b):
    return [char_a+char_b for char_a in a for char_b in b]

boxes = cross(rows, columns)

# For row units, you want an list of identifiers for each of the 9 rows
# How do you specify that you want exactly 9 list without explicitly saying 9?
row_units = [cross(r, columns) for r in rows]

column_units = [cross(rows, c) for c in columns]

# For square units, first you want an list of identifiers for the first of the 3 rows and columns
# Then for the next three columns and same rows, then for the last 3 columns and same rows
# Then for the middle 3 rows and first 3 columns, then the next three columns and same rows...
# How do you specify that you want the loop to move in increments of 3?
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]


unitlist = row_units + column_units + square_units

# Create a dictionary for each box, containing all the units that it's part of
which_units = dict((box, [unit for unit in unitlist if box in unit]) for box in boxes)

# Create a dictionary for each box, containing all its peers, minus the box itself
which_peers = dict((box, set(sum(which_units[box], [])) - set([box])) for box in boxes)

# Implement function that will convert this string to a dictionary of values
# for each corresponding box in the boxes list: '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
def grid_values(string_repr):
    return dict((box, string_repr[index]) for index, box in enumerate(boxes))
# Since the above function provides the dict() with a list of tuples, you could
# also simply do: return dict(zip(boxes, string_repr))
