import psycopg2
import re

conn = psycopg2.connect(database="infosearch", user="visqas", password="0012", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT * FROM inverted_index")
records = cur.fetchall()
pattern = re.compile(r'\d')

def remove_excess(word):
    word = word.replace("'", "").replace("}", "").replace("{", "").replace(",", "").split(' ')
    return word

inv_words = {}
for record in records:
    word = record[0]
    docs = record[1]

    inv_words[word] = docs

print("input 4 words to search")
in_a = str(input("1: "))
in_b = str(input("2: "))
in_c = str(input("3: "))
in_d = str(input("4: "))

if (in_a or in_b or in_c or in_d) not in inv_words:
    print("Unavailable word found")
else:
    a = remove_excess(inv_words.get(in_a))
    #print(a)
    b = remove_excess(inv_words.get(in_b))
    #print(b)
    c = remove_excess(inv_words.get(in_c))
    #print(c)
    d = remove_excess(inv_words.get(in_d))
    #print(d)

    expression = str((set(a) & set(b) | set(c)) - set(d))
    res = pattern.findall(expression)
    print("docs list: ", expression)
