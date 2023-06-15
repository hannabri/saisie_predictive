"""
Nom du fichier : main.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : juin 2023
Description : Ce fichier est le point d'entrée de l'application. Il est le premeir fichier à executer.
"""

from build.chat_app import *
from build.command_parse import aide_en_ligne

root = tk.Tk()
app = ChatApp(root)
app.run()

aide_en_ligne()