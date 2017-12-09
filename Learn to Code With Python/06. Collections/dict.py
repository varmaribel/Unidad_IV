"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

char_count = {'a':5, 'b':7, 'A':5, 'T':8, 'B':10}

char_frequency = dict()
for key, value in char_count.items():
    if key.lower() in char_frequency:
        char_frequency[key.lower()] += value
    else:
        char_frequency[key.lower()] = value

print(char_frequency)




char_frequency = {
    key.lower(): char_count.get(key.lower(), 0) + char_count.get(key.upper(), 0)
    for key in char_count.keys()
}
print(char_frequency)
