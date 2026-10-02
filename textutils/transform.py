"""module de transformation de texte"""


def word_count(text):
    #compte le nombre de mots
    if text == None or text == "":
        return 0
    mots = text.split()
    return len(mots)


def character_count(text):
    #compte les caracteres
    if text == None:
        return 0
    return len(text)


def reverse(text):
    #inverse le texte
    if text == None:
        return ""
    resultat = ""
    for i in range(len(text)-1, -1, -1):  #du dernier au premier
        resultat += text[i]
    return resultat


def slugify(text):
    #fait un slug pour les urls
    if text == None:
        return ""
    result = text.lower()
    #remplace les espaces par des tirets
    result = result.replace(" ", "-")
    #enleve les caracteres chelous
    result = "".join(c for c in result if c.isalnum() or c == "-")
    #evite les tirets doubles
    while "--" in result:
        result = result.replace("--", "-")
    return result.strip("-")


def word_frequency(text):
    #compte combien de fois chaque mot apparait
    if text == None or text == "":
        return {}
    mots = text.lower().split()
    freq = {}
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1
    return freq
