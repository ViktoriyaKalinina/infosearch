import nltk
import pymorphy2
import re, string
morph = pymorphy2.MorphAnalyzer()
i = 1

stop_words = ['так', 'но', 'у', 'с', 'а', 'что', 'это', 'так', 'вот', 'быть', 'как', '—', 'к', 'на', 'и', 'я', 'в', 'из', 'он']
stop_words = ["на", "в", "с", "но", "а", "что", "это", "к", "у", "по", "под", "над", "и", "так", "из", "он", "я", "как", "не", "от"] 

while i < 5:
    f = open("/Users/visqas/infosearch/inf_dotnet/web_pages/%dpage.txt" % i)
    text = f.read()

    tokens = nltk.word_tokenize(text)
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    tokens = re.sub(r'\W', " ", tokens)
    #tokens = re.sub(" +", " ", tokens)
    #words = tokens.split(' ')

    o = open("/Users/visqas/infosearch/inf_py/result_files/%doutput.txt" % i, "w")
    
    for token in tokens:
        p = morph.parse(token)[0]
        print(p.normal_form)
        #o.write(p.normal_form + "\n")

        f.close()
    
    i = i + 1