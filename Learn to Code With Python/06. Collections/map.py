"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

def sweet(x):
    return (x*2)**2

for n in range(5):
    print(sweet(n))

print(list(map(sweet, range(5))))
