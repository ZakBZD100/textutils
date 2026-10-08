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
    """compte la frequence de chaque mot dans le texte

    Args:
        text (str): le texte a analyser

    Returns:
        dict: un dictionnaire mot -> nombre d'apparitions, dans
        l'ordre de premiere apparition. Les mots sont compares
        sans tenir compte de la casse et sans ponctuation.
        Renvoie un dictionnaire vide si le texte est vide ou None.

    Examples:
        >>> word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    if text == None or text == "":
        return {}
    compte = {}
    for mot in text.lower().split():
        mot = "".join(c for c in mot if c.isalnum())
        if mot:
            compte[mot] = compte.get(mot, 0) + 1
    return compte
