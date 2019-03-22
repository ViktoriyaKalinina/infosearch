import pymorphy2
import re, string
morph = pymorphy2.MorphAnalyzer()

f = open("text.txt")
text = f.read()

txt_wo_punctuation = re.sub(r'\W', " ", text)
txt_wo_punctuation = re.sub(" +", " ", txt_wo_punctuation)
words = txt_wo_punctuation.split(' ')

o = open("output_text", "w")
for word in words:
    p = morph.parse(word)[0]
    o.write(p.normal_form + "\n")
