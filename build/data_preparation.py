import pandas as pd
import string

# translation table that replaces punctuation (except "'") and digits with spaces
translator = str.maketrans(string.punctuation.replace("'", "") + string.digits, ' ' * (len(string.punctuation) + len(string.digits) - 1))

def clean_and_tokenize(text):
    text = text.lower()
    text = text.translate(translator)
    tokens = text.split()
    return tokens

def tokenize_file(nameFile):
    
    sms_df = pd.read_excel(nameFile)
    sms_df['SMS_ANON'] = sms_df['SMS_ANON'].astype(str)
    sms_df['tokens'] = sms_df['SMS_ANON'].apply(clean_and_tokenize)
    list_tokens = sms_df["tokens"].tolist()
    return list_tokens

def tokenize_corpus():
    return tokenize_file('src/train_sms.xlsx')

def tokenize_test():
    return tokenize_file('src/test_sms.xlsx')
