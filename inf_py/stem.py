from nltk.corpus import stopwords
import nltk
import pymorphy2
import re, string
 
def tokenize_me(file_text):
    #firstly let's apply nltk tokenization
    tokens = nltk.word_tokenize(file_text)
 
    #let's delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]
 
    #deleting stop_words
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
    tokens = [i for i in tokens if ( i not in stop_words )]
 
    #cleaning words
    tokens = [i.replace("«", "").replace("»", "").replace("-.", "") for i in tokens]
 
    return tokens

f = open("/Users/visqas/infosearch/inf_dotnet/web_pages/1page.txt")
text = f.read()
f.close()

kk_tokens = re.sub(r'\W', " ", text)
kk_tokens = tokenize_me(text)

print(kk_tokens)


