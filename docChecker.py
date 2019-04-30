# from grammarChecker import grammarMatcher
from spellcheck import is_spelled_correctly


def checkThis(ready):
    # spellcheck
    i = 0
    for value in ready:
        if not is_spelled_correctly(value):
            print("NOT SPELLED CORRECTLY: " + value)
            i = i + 1
    if(i == 0):
        print("Checked Done! Nothing wrong.")
