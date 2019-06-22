import docx2txt
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer(r'\w+')


def readFile(input):
    text = docx2txt.process(input)
    values = tokenizer.tokenize(text.lower())
    english = set(stopwords.words('english'))
    ready = [word for word in values if word not in english]
    print(ready)
    return ready
