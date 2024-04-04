

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nltk.download('punkt')
nltk.download('stopwords')

# Load the French language model for spaCy
nlp_fr = spacy.load("fr_core_news_sm")

def remove_stopwords(text, languages=['en']):
    result = {}
    for lang in languages:
        if lang == 'en':
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(text)
            filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
            result['en'] = ' '.join(filtered_text)
        elif lang == 'fr':
            doc = nlp_fr(text)
            filtered_text = [token.text for token in doc if not token.is_stop]
            result['fr'] = ' '.join(filtered_text)
        else:
            raise ValueError("Unsupported language. Only 'en' (English) and 'fr' (French) are supported.")
    return result