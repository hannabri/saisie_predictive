import pandas as pd
from sklearn.model_selection import train_test_split

# Charger le fichier ODS en utilisant pandas
sms_df = pd.read_excel('88milSMS_88522.ods')

# Diviser le corpus en ensemble de train et test
train_df, test_df = train_test_split(sms_df, test_size=0.05, random_state=42)

# Enregistrer les ensembles de train et test en fichiers distincts
train_df.to_excel('train_sms.xlsx', index=False)
test_df.to_excel('test_sms.xlsx', index=False)
