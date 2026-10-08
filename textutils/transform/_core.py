"""module de transformation de texte"""


def word_count(text):
    """Compte le nombre de mots dans le texte.

    Parameters
    ----------
    text : str or None
        Le texte a analyser, ``None`` equivaut a une chaine vide.

    Returns
    -------
    int
        Le nombre de mots separes par des espaces.

    Examples
    --------
    >>> word_count("Hello World")
    2
    """
    #compte le nombre de mots
    if text == None or text == "":
        return 0
    mots = text.split()
    return len(mots)


def character_count(text):
    """Compte le nombre de caracteres dans le texte.

    Parameters
    ----------
    text : str or None
        Le texte a analyser, les espaces sont comptes.

    Returns
    -------
    int
        Le nombre de caracteres, 0 si le texte est ``None``.

    Examples
    --------
    >>> character_count("Hello")
    5
    """
    #compte les caracteres
    if text == None:
        return 0
    return len(text)


def reverse(text):
    """Inverse l'ordre des caracteres du texte.

    Parameters
    ----------
    text : str or None
        Le texte a inverser.

    Returns
    -------
    str
        Le texte inverse, chaine vide si le texte est ``None``.

    Examples
    --------
    >>> reverse("Hello")
    'olleH'
    """
    #inverse le texte
    if text == None:
        return ""
    resultat = ""
    for i in range(len(text)-1, -1, -1):  #du dernier au premier
        resultat += text[i]
    return resultat


def slugify(text):
    """Transforme le texte en slug utilise pour les urls.

    Le texte est mis en minuscules, les espaces deviennent des
    tirets, les caracteres non alphanumeriques sont supprimes et
    les tirets doubles sont reduits a un seul.

    Parameters
    ----------
    text : str or None
        Le texte a transformer.

    Returns
    -------
    str
        Le slug correspondant, chaine vide si le texte est ``None``.

    Examples
    --------
    >>> slugify("Open Source!")
    'open-source'
    """
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
    """Compte la frequence de chaque mot dans le texte.

    Parameters
    ----------
    text : str or None
        Le texte a analyser.

    Returns
    -------
    dict
        Un dictionnaire mot -> nombre d'apparitions, dans l'ordre
        de premiere apparition. Les mots sont compares sans tenir
        compte de la casse et sans ponctuation. Renvoie un
        dictionnaire vide si le texte est vide ou ``None``.

    Examples
    --------
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
