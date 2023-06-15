"""
Nom du fichier : command_parse.py
Auteurs : Anna Barnay, Hanna Brinkmann, Clara Rosina Fernandez
Date de création : mai 2023
Description : Ce fichier contient un script qui utilise le module `argparse` pour afficher l'aide en ligne.
"""
import argparse
from build.tests_prediction_completion import *

# -h: Aide plus options avec ce qu'ils font
def aide_en_ligne():
    help_description = ("Le but du programme est de vous proposer une liste des mots probables pour constituer la suite d'un message. \n" +
                        "Pour utiliser le programme, veuillez ouvrir l'interface et commencer à taper un message. Dès la première lettre, une liste de mots va vous être proposée. " +
                        "Une fois que vous voyez des suggestions de mots, vous pouvez les sélectionner avec les flèches du bas (\u2193) et du haut (\u2191). Quand vous êtes positionné sur le mot souhaité, sélectionnez le avec la flèche vers la droite (\u2192). En appuyant sur Entrer (\u21B5), vous pouvez envoyer le message. \n" +
                        "Vous pouvez rencontrer plusieurs problèmes : Si le programme ne propose pas de mots, cela peut avoir deux origines. Si vous n'avez pas encore commencé à rédiger le message, le programme n'a pas de contexte pour vous proposer des mots. Sinon cela est dû au fait qu'il ne connait aucun mot qui commence par la suite de lettres que vous êtes en train de taper. Pour cette raison, il ne peut pas vous proposer le mot que vous voulez écrire. " +
                        "De plus, notre programme ne peut pas encore lire dans vos pensées. Il fait de son mieux pour vous proposer des mots basés sur la fréquence d'utilisation. Mais parfois il est possible que votre mot cherché ne figure pas parmi les propositions. " +
                        "Et si vous voyez des mots avec des fautes d'orthographe, ceci est dû aux fautes présentes dans les données d'entrainement de notre programme. Conçu pour l'aide à la saisie de SMS, il n'est pas un correcteur orthographique, mais vous y trouverez des abbréviation et du langage familier.")

    parser = argparse.ArgumentParser(description=help_description)

    parser.add_argument("-t", "--test", required=False, action = "store_true", help="Commande pour exécuter les tests")


    args = parser.parse_args()
    

    if args.test:
        tokens = load("build/data/corpus.pkl")
        tokens_test = load("build/data/test.pkl")
        trie = load("build/data/trie.pkl")
        dictio= load("build/data/dictio_trigrammes.pkl")

        #Infos sur le corpus
        print(f"Le taux de mots inconnus dans le corpus de test est {unkWords(tokens_test, dictio)}")

        #Prédiction 
        print("\nTest de la prédiction : ")
        max =0
        for i in range (1,11,1):
            for j in range (0,i+1,1):
                result = testPred(tokens_test, dictio, j, i-j)
                print(f"i : {i} -> nbB : {j} / nbT : {i-j} = {result}")
                if result>max:
                    max=result
        print(f"Le score maximal atteind est : {max}")

        # Complétion
        print("\nTest de la complétion : ")
        max=0
        for i in range(1,11,1):
            for j in range(1,6,1):
                result = testcompletion(trie,tokens_test, j, i)
                print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {result}')
                if result>max:
                    max=result
        print(f"Le score maximal atteind est : {max}")

        # Complétion enrichie par la complétion
        print("\nTest de la complétion enrichie par la complétion: ")
        for i in range(1,11,1):
            for j in range(1,6,1):
                result = testcompletionprediction(dictio, trie,tokens_test, i, 5, j)
                print(f'nb mots prédits : {i} , taille du prefixe : {j} , score = {result}')
                if result>max:
                    max=result
        print(f"Le score maximal atteind est : {max}")


aide_en_ligne()