import psycopg2
import re

conn = psycopg2.connect(database="infosearch", user="visqas", password="0012", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("DELETE FROM doc_table")
READ_DOC_PATH = "/Users/visqas/infosearch/2/lemmatisation_files/"
i = 1

while i <= 100:
    o = open(READ_DOC_PATH + "%doutput.txt" % i)
    text = o.read().split("\n")
    
    for word in text:
        word = (str(word))
        doc_id = (str(i))
        cur.execute("INSERT INTO doc_table(doc_id, word) VALUES(%s, %s)", (doc_id, word))
    i+=1

conn.commit()

cur.execute("DELETE FROM inverted_index")
cur.execute("SELECT * FROM doc_table")
records = cur.fetchall()
#print(records)

term_docs = {}

for item in records:
    word = item[2]
    doc_id = item[1]
    #print(word, doc_id)
    if not word in term_docs:
        term_docs[word] = set()
    term_docs[word].add(doc_id)

for word, doc_id in term_docs.items():
    word = (str(word))
    doc_id = (str(doc_id))
    cur.execute("INSERT INTO inverted_index(word, doc_list) VALUES(%s, %s)", (word, doc_id))

#print(term_docs)

conn.commit()

cur.close()
conn.close()


