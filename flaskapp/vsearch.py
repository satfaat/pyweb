def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ Returns set of letters from phrase """
    return set(letters).intersection(set(phrase))