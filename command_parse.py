import argparse

help_description = ("Le but du programme est de vous propser une liste des mots qui sont probables pour constituer la suite du message." +
                    "Pour utiliser le programme, veuillez commencer à tapper un message. Dès la première lettre, une liste de mots va vous être proposée." +
                    "Si le mot que vous voulez saisir se trouve parmi les mots proposés, il suffit de le sélectionner.")

parser = argparse.ArgumentParser(description=help_description)

args = parser.parse_args()

