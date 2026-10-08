"""les fonctions pour la casse du texte"""


def capitalize_words(text):
    """Met une majuscule au debut de chaque mot.

    Parameters
    ----------
    text : str or None
        Le texte a transformer.

    Returns
    -------
    str
        Le texte avec chaque mot capitalise, chaine vide si le
        texte est ``None``.

    Examples
    --------
    >>> capitalize_words("hello world")
    'Hello World'
    """
    #met une majuscule au debut de chaque mot
    if text == None:
        return ""
    # j'utilise title() c'est plus simple
    return text.title()


def snake_case(text):
    """Convertit le texte en snake_case.

    Les tirets et underscores servent de separateurs et les
    majuscules deviennent des minuscules.

    Parameters
    ----------
    text : str or None
        Le texte a convertir.

    Returns
    -------
    str
        Le texte en snake_case, chaine vide si le texte est ``None``.

    Examples
    --------
    >>> snake_case("Hello World")
    'hello_world'
    """
    #convertit en snake_case (avec des underscores)
    if text == None:
        return ""
    result = text.replace("-", " ").replace("_", " ")
    # gere les majuscules dans les mots
    mots = []
    mot = ""
    for c in result:
        if c == " ":
            if mot:
                mots.append(mot)
            mot = ""
        elif c.isupper() and mot:
            mots.append(mot)
            mot = c.lower()
        else:
            mot += c.lower() if c.isupper() else c
    if mot:
        mots.append(mot)
    return "_".join(mots)


def camel_case(text):
    """Convertit le texte en camelCase.

    Le premier mot reste en minuscules et chaque mot suivant
    commence par une majuscule.

    Parameters
    ----------
    text : str or None
        Le texte a convertir.

    Returns
    -------
    str
        Le texte en camelCase, chaine vide si le texte est vide ou
        ``None``.

    Examples
    --------
    >>> camel_case("open source dev")
    'openSourceDev'
    """
    #convertit en camelCase
    if text == None:
        return ""
    mots = text.replace("-", " ").replace("_", " ").split()
    if not mots:
        return ""
    result = mots[0].lower()
    for m in mots[1:]:
        result += m.capitalize()
    return result
