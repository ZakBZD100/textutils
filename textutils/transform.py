"""module for text transformations"""

#some functions to work with text

def word_count(text):
    #count the number of words in a text
    if text is None:
        return 0
    mots = text.split()
    return len(mots)


def character_count(text):
    #count the characters in the text
    #TODO: add docstring
    if text == None:
        return 0
    return len(text)


def reverse(text):
    #reverse a text string
    if text == None:
        return ""
    resultat = text[::-1]
    print(resultat) #debug
    return resultat
