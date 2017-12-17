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
