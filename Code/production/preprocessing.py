import re
import html
from unidecode import unidecode
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('popular')

def _get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN 

def _decontracted(phrase):
    phrase = re.sub(r"\bcan\'t\b", "cannot", phrase)
    phrase = re.sub(r"\bwon\'t\b", "will not", phrase)
    phrase = re.sub(r"\bdon\'t\b", "do not", phrase)
    phrase = re.sub(r"\bdoesn\'t\b", "does not", phrase)
    phrase = re.sub(r"\bwasn\'t\b", "was not", phrase)
    phrase = re.sub(r"\bisn\'t\b", "is not", phrase)
    phrase = re.sub(r"\baren\'t\b", "are not", phrase)
    phrase = re.sub(r"\bweren\'t\b", "were not", phrase)
    phrase = re.sub(r"\bhasn\'t\b", "has not", phrase)
    phrase = re.sub(r"\bhaven\'t\b", "have not", phrase)
    phrase = re.sub(r"\bshouldn\'t\b", "should not", phrase)
    phrase = re.sub(r"\bwouldn\'t\b", "would not", phrase)
    phrase = re.sub(r"\bcouldn\'t\b", "could not", phrase)
    phrase = re.sub(r"\b\'t", " not", phrase)
    phrase = re.sub(r"\b\'re", " are", phrase)
    phrase = re.sub(r"\b\'s", " is", phrase)
    phrase = re.sub(r"\b\'d", " would", phrase)
    phrase = re.sub(r"\b\'ll", " will", phrase)
    phrase = re.sub(r"\b\'ve", " have", phrase)
    phrase = re.sub(r"\b\'m", " am", phrase)
    return phrase.strip()

def clean_tweet(tweet):

    tweet = str(tweet).lower()

    urlPattern = 'https?://\S+|www\.\S+'
    usernamePattern = '@([A-Za-z0-9_]+)' #From https://help.x.com/en/managing-your-account/x-username-rules 
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    alphaNumeric = r'[^A-Za-z0-9\s]'
    spacePattern = r'\s+'

    lemmatizer = WordNetLemmatizer()
    auxiliary_verbs = {"am", "is", "are", "was", "were"}

    # Remove URLs
    tweet = re.sub(urlPattern, '', tweet)
    # Remove usernames
    tweet = re.sub(usernamePattern, '', tweet)
    # Clean HTML texts like &lt; (<) or &amp; (&)
    tweet = html.unescape(tweet)
    # Convert accented characters to ASCII
    tweet = unidecode(tweet)
    # Decontract words I'm => I am, Don't => Do not
    tweet = _decontracted(tweet)
    # Remove special characters
    tweet = re.sub(alphaNumeric, ' ', tweet)
    # Removes extra spaces
    tweet = re.sub(spacePattern, ' ', tweet).strip()
    # Removes 3 or more consecutive letters by two letters. (e.g. Hiiiii!!!!)
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)

    # Tokenize and lemmatize
    tokens = word_tokenize(tweet)
    # print(tokens)
    pos_tags = pos_tag(tokens)
    
    # tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    tokens = [
        word if word in auxiliary_verbs else lemmatizer.lemmatize(word, _get_wordnet_pos(tag))
        for word, tag in pos_tags
    ]

    # print(tokens)
    tweet = ' '.join(tokens)
    
    return tweet



