import tkinter as tk
from project_copie import prediction, completion

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.message_history = tk.Text(self.root, height=20, width=50)
        self.message_history.pack()

        self.message_entry = tk.Text(self.root, height=4, width=50)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)
        self.message_entry.bind("<KeyRelease>", self.on_key_release)
        self.message_entry.bind("<Right>", self.complete_suggestion)
        self.message_entry.bind("<Up>", self.handle_up_arrow)
        self.message_entry.bind("<Down>", self.handle_down_arrow)
        self.message_entry.focus_set()

        self.suggestion_listbox = tk.Listbox(self.root)
        self.suggestion_listbox.pack()
        self.suggestion_listbox.bind("<Return>", self.insert_selected_suggestion)
        self.suggestion_listbox.bind("<Right>", self.complete_suggestion)
        
        self.selected_index = -1
        self.suggestions = []

    def send_message(self, event):
        message = self.message_entry.get("1.0", tk.END).strip()
        self.message_history.insert(tk.END, "Me: " + message + "\n")
        self.message_entry.delete("1.0", tk.END)

        # Effacer la liste de complétion
        self.clear_suggestions()

    def on_key_release(self, event):
        entered_text = self.message_entry.get("1.0", tk.END)
        words = entered_text.split()

        if entered_text[-1] != " ":
        # Suggérer des complétions pour le mot en cours
            suggested = completion(words[-1])
            print("Suggested words:", suggested)
            if suggested:
                self.suggestions = suggested
                self.display_suggestions()
            else:
                self.clear_suggestions()
        else:
        # Prédire le prochain mot
            predicted = prediction(3, words[:-1])
            print("Predicted words:", predicted)
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
            words = current_text.split()
            words[-1] = suggestion  # Remplacer le dernier mot par la suggestion
            completed_text = " ".join(words) + " "
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)
            self.clear_suggestions()
            self.selected_index = -1

    def complete_suggestion(self, event):
        if self.selected_index >= 0:
            suggestion = self.suggestions[self.selected_index]
            current_text = self.message_entry.get("1.0", tk.END).strip()
            words = current_text.split()
            words[-1] = suggestion  # Remplacer le dernier mot par la suggestion
            completed_text = " ".join(words) + " "
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)
            self.clear_suggestions()
            self.selected_index = -1

    def run(self):
        self.root.mainloop()

root = tk.Tk()
app = ChatApp(root)
app.run()
