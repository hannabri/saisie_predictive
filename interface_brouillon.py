import tkinter as tk
from tkinter import messagebox
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
        self.message_entry.focus_set()

        self.message_completion = tk.Listbox(self.root)
        self.message_completion.pack()
        self.message_completion.bind("<Double-Button-1>", self.insert_selected_completion)
        self.message_completion.bind("<Return>", self.insert_selected_completion)

    def send_message(self, event):
        message = self.message_entry.get("1.0", tk.END).strip()
        self.message_history.insert(tk.END, "Me: " + message + "\n")
        self.message_entry.delete("1.0", tk.END)

        # Efface la liste de complétion
        self.clear_completion()

    def on_key_release(self, event):
        entered_text = self.message_entry.get("1.0", tk.END).strip()

        if entered_text.endswith(" "):
            # Prédire le prochain mot
            predicted = prediction(3, entered_text)
            if predicted:
                self.display_completion(predicted)
            else:
                self.clear_completion()
        else:
            # Suggérer des complétions pour le mot en cours
            suggested = completion(entered_text)
            if suggested:
                self.display_completion(suggested)
            else:
                self.clear_completion()

    def display_completion(self, suggestions):
        self.message_completion.delete(0, tk.END)
        for suggestion in suggestions:
            self.message_completion.insert(tk.END, suggestion)

    def clear_completion(self):
        self.message_completion.delete(0, tk.END)

    def insert_selected_completion(self, event):
        selection = self.message_completion.get(tk.ACTIVE)
        if selection:
            current_text = self.message_entry.get("1.0", tk.END).strip()
            last_word = current_text.split(" ")[-1]
            completed_text = current_text.rsplit(" ", 1)[0] + " " + selection
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, completed_text)

    def run(self):
        self.root.mainloop()

root = tk.Tk()
app = ChatApp(root)
app.run()
