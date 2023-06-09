def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for items in lst:
        if not isinstance(items, list):
            return False
    return True

# ! Another solution with- all()
    # Alternate possibilities: use all() with a generator comprehension,
    # though that isn't something we've covered yet:
    #
    # return all(isinstance(item, list) for item in lst)
