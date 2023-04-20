import pickle

# Charger le fichier pickle
with open("tokens.pkl", "rb") as file:
    tokens = pickle.load(file)

# Afficher le contenu du fichier pickle
print(tokens[4])
