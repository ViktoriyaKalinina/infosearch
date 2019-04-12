import pymorphy2
import re, string
import os
morph = pymorphy2.MorphAnalyzer()
counter = 100
i = 1

READ_FILE_PATH = "/Users/visqas/infosearch/1/web_pages/"
WRITE_FILE_PATH = "lemmatisation_files/"

def remove_punctuation(text):
  text = re.sub(r'\W|\d', " ", text)
  processed_txt = re.sub(" +", " ", text)
  return processed_txt

while i <= counter:
  read_file = open(READ_FILE_PATH + "%dpage.txt" % i)
  write_file = open(WRITE_FILE_PATH + "%doutput.txt" % i, "w")

  text = read_file.read()
  txt_wo_punctuation = remove_punctuation(text)
  words = txt_wo_punctuation.split(' ')

  for word in words:
      p = morph.parse(word)[0]
      write_file.write(p.normal_form + "\n")
      read_file.close()
  
  i += 1