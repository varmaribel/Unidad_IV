"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

def sweet(x):
    return (x + abs(x))**3

def positive(x):
    return x > 0

print(list(map(sweet, filter(positive, range(-4, 5)))))
