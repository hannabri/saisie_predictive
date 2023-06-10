import argparse

# -h: Aide plus options avec ce qu'ils font
# -u: mettre à jour (faut l'implémenter encore)
# -nbm: Option pour choisir la taille de la list (faut l'implémenter encore)

help_description = ("Le but du programme est de vous propser une liste des mots qui sont probables pour constituer la suite du message." +
                    "Pour utiliser le programme, veuillez commencer à tapper un message. Dès la première lettre, une liste de mots va vous être proposée. " +
                    "Si le mot que vous voulez saisir se trouve parmi les mots proposés, il suffit de le sélectionner. " +
                    "Il y a quelques problèmes que le programme peut avoir : Si le programme ne propose pas de mots, cela peut avoir deux origines. Si vous n'avez pas encore commencer à rédiger le message, le programme n'a pas de contexte pour vous proposer des mots. Sinon cela est dû au fait qu'il ne connait aucun mot qui commence par la suite de lettres que vous êtes en train de tapper. Pour cette raison, il ne peut pas vous proposer le mot que vous voulez écrire. " +
                    "Notre programme ne peut pas lire dans vos pensées. Il fait de son mieux pour vous proposer des mots basés sur la fréquence d'utilisation. Mais parfois il est possible que votre mot cherché ne figure pas parmi les propositions. " +
                    "Et si vous voyez des mots avec des fautes d'orthogrphe, ceci est dû aux fautes présentes dans les données d'entrainement de notre programme. Conçu pour l'aide à la saisie de SMS, il n'est pas un correcteur orthographique, mais vous y trouverez des abbréviation et du langage familier.")

parser = argparse.ArgumentParser(description=help_description)

parser.add_argument('-u','--update', metavar='update', help="Mettre à jour la liste des mots")
parser.add_argument('-nbm','--nombre-de-mots', type=int, choices=range(1, 6), metavar=[1-5], help="Choisir le nombre de mots proposés dans la liste")

args = parser.parse_args()

