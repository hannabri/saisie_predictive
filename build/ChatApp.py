import tkinter as tk
from project import *
from data_preparation import clean_and_tokenize
from deserialization import load

class ChatApp:
    def __init__(self, root):
        self.dictio = load("dictionnaire_trigrammes")
        self.trie = load("trie")
        self.root = root
        self.root.title("Chat App")

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
        self.suggestion_listbox.bind("<Return>", self.insert_selected_suggestion)
        self.suggestion_listbox.bind("<Right>", self.handle_right_arrow)
        
        self.selected_index = -1
        self.suggestions = []

    def send_message(self, event):

        message = self.message_entry.get("1.0", tk.END).strip()
        self.message_history.insert(tk.END, "Me: " + message + "\n")
        self.message_entry.delete("1.0", tk.END)

        # APPELER FONCTION UPDATE
        updatePrediction(clean_and_tokenize(message), self.dictio)
        updateCompletion(clean_and_tokenize(message), self.trie)
        self.clear_suggestions()

    def on_key_release(self, event):

        entered_text = self.message_entry.get("1.0", tk.END)
        wordsList = entered_text.split()

        if entered_text[len(entered_text)-2] != " ":
            print(entered_text)
        # Suggérer des complétions pour le mot en cours
            suggested = completion(wordsList[-1])
            print("Suggested wordsList:", suggested)
            if suggested:
                self.suggestions = suggested
                self.display_suggestions()
            else:
                self.clear_suggestions()
        else:
        # Prédire le prochain mot
            predicted = prediction(wordsList,self.trie)
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
            wordsList[-1] = suggestion  # Remplacer le dernier mot par la suggestion
            completed_text = " ".join(wordsList) + " "
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)
            self.clear_suggestions()
            self.selected_index = -1

    def handle_right_arrow(self, event):
        if self.selected_index >= 0:
            suggestion = self.suggestions[self.selected_index]
            current_text = self.message_entry.get("1.0", tk.END)

        # Si le dernier caractère non vide est un espace, on prédit, sinon on complète.
            if current_text[-2] == " ":
                completed_text = current_text + suggestion + " "
            else:
                wordsList = current_text.split()
                if wordsList:  # wordsList n'est pas vide
                    wordsList[-1] = suggestion
                    completed_text = " ".join(wordsList) + " "
                else:
                    completed_text = suggestion + " "
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)
            self.clear_suggestions()
            self.selected_index = -1

    def run(self):
        self.root.mainloop()

root = tk.Tk()
app = ChatApp(root)
app.run()
