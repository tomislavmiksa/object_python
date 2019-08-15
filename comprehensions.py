input_strings = ['1', '2', '3', '4']

# CLASSIC CODE
output_integers = []
for num in input_strings:
    output_integers.append(int(num))

# COMPREHENSION
output_integers.clear()
output_integers = [int(num) for num in input_strings]

# COMPREHENSION WITH CONDITION
output_integers.clear()
output_integers = [int(num) for num in input_strings if n > 2]


from collections import namedtuple
Book = namedtuple("Book", "author title genre")
books = [ 
        Book("Pratchet", "Nightwatch", "fantasy"),
        Book("Pratchet", "Thief of time", "fantasy"),
        Book("Le Guin", "The Dispossesed", "scifi"),
        Book("Le Guin", "The Wizard of Earthsea", "fantasy")
    ]
fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}

import sys
inname, outname = sys.argv[1:3]
with open(inname) as infile:
    with open(outname, 'w') as outfile:
        warnings = l.replace('\tWARNING','')
                   for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
            
