import pandas as pd
import re
from nltk.tokenize import word_tokenize
import pickle

emojis = [":-)", "<3", ":]", ";)", ";-)", ":D", ":-D", ";P", ";-P", ":P", ":-P", "8)", "8-)", ":|", ":-|", ":(", ":-(", "o_O", "o.O", ":/", ":-/", ":O", ":-O", "O_O", "O.O", "o_o"]

def clean_and_tokenize(text):
    for emoji in emojis:
        text = text.replace(emoji, "")
    text = re.sub(r'[^\w\s]', '', text.lower())  # Supprimer les caractères non alphanumériques et mettre en minuscules
    tokens = word_tokenize(text)  # Tokeniser le texte
    return tokens

def tokenize():
    # Charger le fichier Excel en DataFrame
    sms_df = pd.read_excel('train_sms.xlsx')

    # Convertir la colonne qui contient les sms en chaîne de caractères
    sms_df['SMS_ANON'] = sms_df['SMS_ANON'].astype(str)

    # Nettoyer et tokeniser le texte
    sms_df['tokens'] = sms_df['SMS_ANON'].apply(clean_and_tokenize)

    # Convertir la colonne 'tokens' en une liste de listes de tokens
    list_tokens = sms_df["tokens"].tolist()
    
    return list_tokens

# Appeler la fonction tokenize et enregistrer les tokens dans un fichier pickle
list_tokens = tokenize()
with open("tokens.pkl", "wb") as file:
    pickle.dump(list_tokens, file)
