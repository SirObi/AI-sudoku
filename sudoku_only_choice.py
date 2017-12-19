# -*- coding: utf-8 -*-

from collections import Counter

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
# Replace each '.' with '123456789'
def grid_values(string_repr):
    string_repr = list(string_repr)
    for i in range(len(string_repr)):
        if string_repr[i] == '.':
            string_repr[i] = '123456789'
    return dict((box, string_repr[index]) for index, box in enumerate(boxes))
# Since the above function provides the dict() with a list of tuples, you could
# also simply do: return dict(zip(boxes, string_repr))

grid_dict = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')

# Implement function that iterates over boxes in puzzle that only have one value!! assigned to them
# and remove this value from every one of its peers
def eliminate(grid):
    for box in grid:
        if len(grid[box]) == 1:
            peers = which_peers[box]
            box_value = grid[box]
            for peer in peers:
                grid[peer] = grid[peer].replace(box_value, "")
        else:
            continue
    return grid

# For values from 1 to 9, iterate through every unit in unitlist.
# Check which fields in the unit have this value in the list of possible values
# If only one field in a unit can contain that value, the value is assigned to that field on the grid
# You want to compare strings with strings, therefore range(0,10) is not useful
def only_choice(grid):
    for unit in unitlist:
        for value in '123456789':
            boxes_with_value = [box for box in unit if value in grid[box]]
            if len(boxes_with_value) == 1:
                grid[boxes_with_value[0]] = value
    return grid

eliminate(grid_dict)
only_choice(grid_dict)

print grid_dict
