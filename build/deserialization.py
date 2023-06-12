import pickle

def load(object):
    with open("build/" + str(object)+ ".pkl", "rb") as file:
        return pickle.load(file)