import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Analyzer:
    def findCriticalWords(self):
        critical_words = []
        for tk in self.tokens:
            if (tk not in self.stop): ## remove stop words
                if nltk.pos_tag([tk])[0][1] in self.verb_tags: ## change to present verb
                    changed_verb = str(WordNetLemmatizer().lemmatize(tk,'v'))
                    critical_words.append(changed_verb)
                else:
                    critical_words.append(tk)
        return critical_words
    def __init__(self, sentence):
    	nltk.data.path.append('../libs/nltk_data/')
        self.sentence = sentence
        # split sentence
        self.tokens = nltk.word_tokenize(self.sentence)
        self.stop = set(stopwords.words('english'))
        self.verb_tags = ['VBG','VBD','VBZ','MD','NN$','NNS']