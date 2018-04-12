#!/usr/bin/env python
# (c)2014 John Strickler
# 
from president import President

for term in 1, 26, 41, 44:
    p = President(term)   # George Washington

    print("{0} {1} was born at {2}, {3} on {4}".format(
        p.first_name, p.last_name, p.birth_place, p.birth_state, p.birth_date
    ))
    print()
