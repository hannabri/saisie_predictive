from trie_test import *
from tokenizer_cleaner import *
import tkinter as tk

# initiate new Trie
prediction = Trie()

# add words in our trie
print("Tokenizing...")
vocab = tokenize()
print("Tokenization done.")

def vocab2dict(vocab):
    vocab_sans_doublon = list(set(vocab))
    dict = {w: vocab.count(w) for w in vocab_sans_doublon}
    return dict

words = vocab2dict(vocab)

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
