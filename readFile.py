import docx2txt
import fnmatch
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')


def readFile():
    name = [f for f in os.listdir() if fnmatch.fnmatch(f, '*.docx')]
    name = name[0]
    text = docx2txt.process(name)

    values = tokenizer.tokenize(text.lower())
    english = set(stopwords.words('english'))
    ready = [word for word in values if word not in english]
    print(ready)
    return ready
