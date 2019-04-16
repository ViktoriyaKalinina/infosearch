import collections
import math
import psycopg2

conn = psycopg2.connect(database="infosearch", user="visqas", password="0012", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("DELETE FROM tf_idf")
#RESULT_OUTPUT_PATH = "/Users/visqas/infosearch/4/res_tf_idf"
TEXT_PATH = "/Users/visqas/infosearch/2/lemmatisation_files/"

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

def compute_idf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

i = 1
corpus = []
while i <= 100:
    o = open(TEXT_PATH + "%doutput.txt" % i)
    text = o.read().split('\n')
    corpus.append(text)
    
    tf_text = compute_tf(text)
    i+=1

k = 1
while k <= 100:
    for word, tf in tf_text.items():
        idf = compute_idf(word, corpus)
        tf_idf = (tf * idf)
        format_word = (str(word))
        #format_tf = str(tf)
        doc_id = str(k)
        cur.execute("INSERT INTO tf_idf(word, doc_id, tf, idf, tf_idf) VALUES(%s, %s, %s, %s, %s)", (format_word, doc_id, tf, idf, tf_idf))
    k+=1

conn.commit()
cur.close()
conn.close()
