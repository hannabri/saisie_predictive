import pickle

def load(object):
    with open(str(object)+ ".pkl", "rb") as file:
        return pickle.load(file)