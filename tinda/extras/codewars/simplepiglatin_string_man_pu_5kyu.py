# Simple Pig Latin

'''
MOVE THE FIRST LETTER OF EACH WORD TO THE END OF IT,
THEN ADD "AY" TO THE END OF THE WORD.
LEAVE PUNCTUATION MARKS UNTOUCHED.
'''

def pig_it(text):
    # dont touch punctuation marks.
    # split the text into a list of words.
    # for each word, move the first letter to the end,
    # then add "ay" to the end of the word.
    # join the list back into a string.
    # return the string.
    y = []
    x = text.split()
    for i in x:
        if i in "!@#$%^&*()-_=+[];:'\,<.>/?":
            y.append(i)
        else:
            y.append(i[1:] + i[0] + "ay")
    return " ".join(y)


def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())


import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)

from string import punctuation
def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )
    

def pig_it(text):
    piggy = []
    for word in text.split():
        if word.isalpha():
            piggy.append(word[1:]+ word[0] + "ay")
        else:
            piggy.append(word)
    return ' '.join(piggy)


def pig_it(text):
    return __import__("re").sub(r'\b\w+\b', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)

import re

def pig_it(text):
    return re.sub(r'(\w)(\w*)( ?)', r'\2\1ay\3', text)

import re
def pig_it(text):
    return re.sub(r'([A-Za-z])([A-Za-z]*)', r'\2\1ay', text)

pig_it = lambda text: ' '.join(list(map(lambda x: x[1:]+x[:1]+'ay' if x.isalpha() else x,text.split())))


