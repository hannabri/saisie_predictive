import pandas as pd
import re
from nltk.tokenize import word_tokenize

# Charger le fichier Excel en DataFrame
sms_df = pd.read_excel('/home/clara/Documentos/LI/projet TAL/test_sms.xlsx')

# Convertir la colonne qui contient les sms en chaîne de caractères (je sais pas pq sinon ça ne marche pas, alors que normalemnet c'est tout des strings)
sms_df['SMS_ANON'] = sms_df['SMS_ANON'].astype(str)

emojis = [":-)", ":]", ";)", ";-)", ":D", ":-D", ";P", ";-P", ":P", ":-P", "8)", "8-)", ":|", ":-|", ":(", ":-(", "o_O", "o.O", ":/", ":-/", ":O", ":-O", "O_O", "O.O", "o_o"]

# Nettoyer et tokeniser le texte
def clean_and_tokenize(text):
    for emoji in emojis:text = text.replace(emoji, "")
    text = re.sub(r'[^\w\s]', '', text.lower())  # Supprimer les caractères non alphanumériques et mettre en minuscules
    tokens = word_tokenize(text)  # Tokeniser le texte
    return tokens

sms_df['tokens'] = sms_df['SMS_ANON'].apply(clean_and_tokenize)



print(sms_df['tokens'].head())

#Cŕeer un nouveau fichier excel

sms_df.to_excel('test_sms_transformed.xlsx', index=False)
