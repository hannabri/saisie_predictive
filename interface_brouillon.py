import tkinter as tk
from tkinter import ttk
from project_copie import prediction, completion

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.combobox = ttk.Combobox(self)
        self.combobox.pack(side="top")
        
        self.combobox.bind('<<ComboboxSelected>>', self.on_combobox_selected)
        self.combobox.bind('<KeyRelease>', self.on_key_release)
        
        self.predicted_word = tk.StringVar(self, value="")
        self.prediction_label = tk.Label(self, textvariable=self.predicted_word)
        self.prediction_label.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def on_key_release(self, event):
        entered_text = self.combobox.get()
        if entered_text[-1] == " ":
            predicted = prediction(entered_text)
            self.predicted_word.set(f"Predicted next word: {predicted}")
        else:
            suggested = completion(entered_text)
            # Assuming 'completion' returns a list of suggestions
            self.combobox['values'] = suggested

    def on_combobox_selected(self, event):
        self.combobox.set(self.combobox.get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
