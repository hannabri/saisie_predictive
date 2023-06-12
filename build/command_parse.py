import argparse

# -h: Aide plus options avec ce qu'ils font
def aide_en_ligne():
    help_description = ("Le but du programme est de vous propser une liste des mots qui sont probables pour constituer la suite du message. \n" +
                        "Pour utiliser le programme, veuillez ouvrir l'interface et commencer à tapper un message. Dès la première lettre, une liste de mots va vous être proposée. " +
                        "Une fois que vous voyez des suggestions de mots, vous pouvez les sélectionner avec les flèches du bas (\u2193) et du haut (\u2191). Quand vous avez choisi le mot souhaité, entrez le avec la flèche vers la droite (\u2192). En appuyant sur Entrer (\u21B5), vous pouvez envoyer le message. \n" +
                        "Vous pouvez rencontrer plusieurs problèmes : Si le programme ne propose pas de mots, cela peut avoir deux origines. Si vous n'avez pas encore commencer à rédiger le message, le programme n'a pas de contexte pour vous proposer des mots. Sinon cela est dû au fait qu'il ne connait aucun mot qui commence par la suite de lettres que vous êtes en train de tapper. Pour cette raison, il ne peut pas vous proposer le mot que vous voulez écrire. " +
                        "De plus, notre programme ne peut pas lire dans vos pensées. Il fait de son mieux pour vous proposer des mots basés sur la fréquence d'utilisation. Mais parfois il est possible que votre mot cherché ne figure pas parmi les propositions. " +
                        "Et si vous voyez des mots avec des fautes d'orthogrphe, ceci est dû aux fautes présentes dans les données d'entrainement de notre programme. Conçu pour l'aide à la saisie de SMS, il n'est pas un correcteur orthographique, mais vous y trouverez des abbréviation et du langage familier.")

    parser = argparse.ArgumentParser(description=help_description)

    args = parser.parse_args()

