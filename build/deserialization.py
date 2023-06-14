"""
Nom du fichier : deserialiszation.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier contient une fonction pour ouvrir le fichier pickle et le retransformer en objet python.
"""

import pickle

def load(fileName):
    with open(fileName, "rb") as file:
        return pickle.load(file)