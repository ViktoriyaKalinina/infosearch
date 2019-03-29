import pymorphy2
import re, string
morph = pymorphy2.MorphAnalyzer()
counter = 10
i = 1

def remove_punctuation(text):
  text = re.sub(r'\W', " ", text)
  processed_txt = re.sub(" +", " ", text)
  return processed_txt

while i < counter:
  read_file = ("/Users/visqas/infosearch/inf_dotnet/web_pages/%dpage.txt" % i)
  write_file = ("/Users/visqas/infosearch/inf_py/lemmatisation_files/%doutput.txt" % i)

  f = open(read_file)
  text = f.read()
  txt_wo_punctuation = remove_punctuation(text)
  words = txt_wo_punctuation.split(' ')

  o = open(write_file, "w")
    
  for word in words:
      p = morph.parse(word)[0]
      o.write(p.normal_form + "\n")
      f.close()
  i += 1