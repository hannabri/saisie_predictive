from trie import *
from data_preparation import *
import tkinter as tk
import pickle

# initiate new Trie
prediction = Trie()

# add words in our trie
with open("tokens.pkl", "rb") as file:
    tokens = pickle.load(file)

def tokens2dict(tokens):
    # Aplatir la liste de listes en une seule liste
    flat_tokens = [word for sublist in tokens for word in sublist]

    tokens_sans_doublon = list(set(flat_tokens))
    dict = {w: flat_tokens.count(w) for w in tokens_sans_doublon}
    return dict


words = tokens2dict(tokens)

for word in words.keys():
    prediction.insert(word, words[word])

def generate_suggestions(input_text):
    suggestions_dict = prediction.search(input_text)
    sorted_suggestions = dict(sorted(suggestions_dict.items(), key=lambda x: x[1], reverse=True)[:3])
    return sorted_suggestions

def update_suggestions_on_gui(suggestions):
    suggestions_label.config(text="\n".join(suggestions.keys()))

def on_key_release(event):
    input_text = text_input.get()
    suggestions = generate_suggestions(input_text)
    update_suggestions_on_gui(suggestions)

main_window = tk.Tk()
main_window.title("Complétion de texte")

text_input = tk.Entry(main_window, width=40)
text_input.bind('<KeyRelease>', on_key_release)
text_input.pack(pady=10)

suggestions_label = tk.Label(main_window, text="")
suggestions_label.pack(pady=10)

print("Starting mainloop...")  # Ajout du print ici
main_window.mainloop()
