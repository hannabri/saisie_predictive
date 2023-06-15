"""
Nom du fichier : chat_app.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier définit la classe ChatApp avec laquelle est créé l'interface graphique. Elle relie prédiction et complétion.
"""

import os
import tkinter as tk
from build.initialisation_objets import *
from build.data_preparation import clean_and_tokenize
from build.deserialization import load
from build.serialization import serialize

class ChatApp:
    def __init__(self, root):
        if os.path.exists("build/data/dictio_trigrammes.pkl"):
            self.dictio = load("build/data/dictio_maj.pkl")
        else:
            self.dictio = load("build/data/dictio.pkl")
        if os.path.exists("build/data/trie_maj.pkl"):
            self.trie = load("build/data/trie_maj.pkl")
        else:
            self.trie = load("build/data/trie.pkl")
        self.root = root
        self.root.title("Chat App")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) #X fermer fenêtre

        self.message_history = tk.Text(self.root, height=20, width=50)
        self.message_history.pack()

        self.message_entry = tk.Text(self.root, height=4, width=50)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)
        self.message_entry.bind("<KeyRelease>", self.on_key_release)
        self.message_entry.bind("<Right>", self.handle_right_arrow)
        self.message_entry.bind("<Up>", self.handle_up_arrow)
        self.message_entry.bind("<Down>", self.handle_down_arrow)
        self.message_entry.focus_set()

        self.suggestion_listbox = tk.Listbox(self.root)
        self.suggestion_listbox.pack()
        self.suggestion_listbox.bind("<Right>", self.handle_right_arrow)
        
        self.selected_index = -1
        self.suggestions = []

    def send_message(self, event):

        message = self.message_entry.get("1.0", tk.END).strip()
        self.message_history.insert(tk.END, "Me: " + message + "\n")
        self.message_entry.delete("1.0", tk.END)

        updatePrediction(clean_and_tokenize(message), self.dictio)
        updateCompletion(clean_and_tokenize(message), self.trie)
        self.clear_suggestions()

    def on_key_release(self, event):

        entered_text = self.message_entry.get("1.0", "end-1c")  # "end-1c" signifie "fin moins 1 caractère"
        wordsList = entered_text.split()

        if entered_text and entered_text[-1] != " " and len(wordsList)!=0:
            # Suggérer des complétions pour le mot en cours
            suggested = completion(wordsList[-1],self.trie)
            if suggested:
                self.suggestions = suggested
                self.display_suggestions()
            else:
                self.clear_suggestions()
        else:
            # Prédire le prochain mot
            predicted = prediction(wordsList,self.dictio)
            if predicted:
                self.suggestions = predicted
                self.display_suggestions()
            else:
                self.clear_suggestions()

    def display_suggestions(self):
        self.suggestion_listbox.delete(0, tk.END)
        for suggestion in self.suggestions:
            self.suggestion_listbox.insert(tk.END, suggestion)

    def clear_suggestions(self):
        self.suggestion_listbox.delete(0, tk.END)
        self.suggestions = []

    def handle_up_arrow(self, event):
        if self.selected_index > 0:
            self.selected_index -= 1
            self.suggestion_listbox.selection_clear(0, tk.END)
            self.suggestion_listbox.selection_set(self.selected_index)

    def handle_down_arrow(self, event):
        if self.selected_index < len(self.suggestions) - 1:
            self.selected_index += 1
            self.suggestion_listbox.selection_clear(0, tk.END)
            self.suggestion_listbox.selection_set(self.selected_index)

    def insert_selected_suggestion(self, event):
        if self.selected_index >= 0:
            suggestion = self.suggestions[self.selected_index]
            current_text = self.message_entry.get("1.0", tk.END).strip()
            wordsList = current_text.split()
            wordsList[-1] = suggestion  # Remplace le dernier mot par la suggestion
            completed_text = " ".join(wordsList) + " " 
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)
            self.message_entry.mark_set(tk.INSERT, 'end')  # Place le curseur a la fin
            self.clear_suggestions()
            self.selected_index = -1

    def handle_right_arrow(self, event):
        if self.selected_index >= 0:
            suggestion = self.suggestions[self.selected_index]
            current_text = self.message_entry.get("1.0", tk.END)
            if current_text and current_text[-2] == " ":
                completed_text = current_text.strip() + " " + suggestion + " "
            else:
                wordsList = current_text.split()
                if wordsList:  # wordsList n'est pas vide
                    wordsList[-1] = suggestion
                    completed_text = " ".join(wordsList) + " "
                else:
                    completed_text = suggestion + " "
            self.message_entry.delete("1.0", tk.END)
            completed_text = completed_text.replace("\n", "")
            self.message_entry.insert(tk.END, completed_text)
            self.message_entry.mark_set(tk.INSERT, 'end')
            self.clear_suggestions()
            self.selected_index = -1


    def on_closing(self):
        print("Fermeture de l'application")
        serialize(self.trie, "build/data/trie_maj.pkl")
        serialize(self.dictio, "build/data/dictio_maj.pkl")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# root = tk.Tk()
# app = ChatApp(root)
# app.run()
