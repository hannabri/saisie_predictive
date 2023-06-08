import pandas as pd
import string

# Define emojis 
emojis = {"'",":-)", "<3", ":]", ";)", ";-)", ":D", ":-D", ";P", ";-P", ":P", ":-P", "8)", "8-)", ":|", ":-|", ":(", ":-(", "o_O", "o.O", ":/", ":-/", ":O", ":-O", "O_O", "O.O", "o_o"}

# Define a translation table that replaces punctuation (except the apostrophe) and digits with spaces
translator = str.maketrans(string.punctuation.replace("'", "") + string.digits, ' ' * (len(string.punctuation) + len(string.digits) - 1))

def clean_and_tokenize(text):
    """
    Function to clean and tokenize a text string
    """
    # Convert to lower case
    text = text.lower()

    # Replace punctuation and digits with spaces
    text = text.translate(translator)
    
    # Tokenize the text based on spaces
    tokens = text.split()

    return tokens

def tokenize_file(nameFile):
    """
    Function to tokenize a dataframe from an Excel file
    """
    # Read the Excel file into a pandas DataFrame
    sms_df = pd.read_excel(nameFile)

    # Convert 'SMS_ANON' column to string
    sms_df['SMS_ANON'] = sms_df['SMS_ANON'].astype(str)

    # Apply clean_and_tokenize function to 'SMS_ANON' column
    sms_df['tokens'] = sms_df['SMS_ANON'].apply(clean_and_tokenize)

    # Convert 'tokens' column into a list of lists of tokens
    list_tokens = sms_df["tokens"].tolist()
    
    return list_tokens

def tokenize_corpus():
    return tokenize_file('train_sms.xlsx')

def tokenize_test():
    return tokenize_file('test_sms.xlsx')
