"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

import pickle

person = {
    "first_name": "Derek",
    "last_name": "Jensen",
    "age": 100,
    "eye_color": "green",
    "programming_languages": ["python", "c#", "Switft"]
}


with open("person.ser", "bw") as person_file:
    pickle.dump(person, person_file)


with open("person.ser", "rb") as person_file:
    new_person = pickle.load(person_file)
    print(new_person)
