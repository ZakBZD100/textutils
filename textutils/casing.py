"""text casing functions"""

def capitalize_words(text):
    #capitalize the first letter of each word
    if text == None:
        return ""
    #uses the title() method
    return text.title()
