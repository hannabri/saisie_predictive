import pickle

def load(object): #obejct : str
    with open(object + ".pkl", "rb") as file:
        return pickle.load(file)