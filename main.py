"""
Nom du fichier : main.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : juin 2023
Description : Ce fichier est le point d'entrée de l'application. Il est le premeir fichier à executer.
"""

from build.chat_app import *
import build.command_parse as c
from build.tests_prediction_completion import df_results

if c.aide_en_ligne().test:
    df_results()

else: 
    root = tk.Tk()
    app = ChatApp(root)
    app.run()