from SentenceSpliter.sentence_analysis import Analyzer

def splitCaption(str) :
	analyzer = Analyzer(str)
	words = analyzer.findCriticalWords()
	return words