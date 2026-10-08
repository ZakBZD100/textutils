"""les fonctions pour la casse du texte"""


def capitalize_words(text):
    #met une majuscule au debut de chaque mot
    if text == None:
        return ""
    # j'utilise title() c'est plus simple
    return text.title()


def snake_case(text):
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
