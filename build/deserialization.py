import pickle

def load(fileName):
    with open(fileName, "rb") as file:
        return pickle.load(file)