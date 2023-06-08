from nltk.tokenize import word_tokenize
from nltk.stem.snowball import FrenchStemmer

# Initialize the stemmer
stemmer = FrenchStemmer()

sentence = "Les chats c'est mignon et qu'ils aiment jouer."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Stem the tokens
stemmed_tokens = [stemmer.stem(token) for token in tokens]

print(stemmed_tokens)
