def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()

# different solution:
    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]
