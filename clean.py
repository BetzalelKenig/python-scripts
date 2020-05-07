import re
import string
import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
#nltk.download('stopwords')
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))


text = '''<p>I,m not and no Go dog dogs ,
 but if the bal and $%# 5nt and to doc
 so go and went store<p>	haa		is a fun story
 so we want the key cry cried <p>'''


def split_paragraphs(text):
	return text.split('<p>')


def basic_clean(paragraphs):
	words = paragraphs.split(' ')
	clean_text = [re.sub(r'[%s]' % re.escape(string.punctuation), '', word) for word in words]
	#remove words with digits 
	clean_text = [re.sub(r'\w*\d\w*', '', word) for word in clean_text]
	return ' '.join(clean_text)


def stem_para(text):
	
	return ' '.join([stemmer.stem(word) for word in text.split(' ')])


def remove_stop_words(text):
	print(text)
	return ' '.join([word for word in text.split(' ') if word not in stopWords])


print(stem_para(','.join([remove_stop_words(basic_clean(word)) for word in split_paragraphs(text)])))




