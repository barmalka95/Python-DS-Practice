def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # *Create an empty set called duplicate to store the numbers that have been encountered so far.
    duplicate = set()

    # *Iterates over each element, num, in the input list nums.
    for num in nums:

        # *For each num, it checks if it already exists in the duplicate set using the in operator.
        if num in duplicate:

            # *If a duplicate is found, the function immediately returns that number using the return statement, effectively stopping the iteration and exiting the function.
            return num

    # *If the number is not found in the duplicate set, it is added to the set using the add() method.
        duplicate.add(num)

    # *If the loop completes without finding any duplicates, the function implicitly returns None,
