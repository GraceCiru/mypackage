def top_n (items, n):
    """
    Returns the top n items in an array in descending order.

    Args:
        items (obj) : list or array-like object
        n (int) : number of items to return

    Returns:
        top n items in descending order

    Egs:
        >>> top_n([8, 3, 2, 7, 9], 3)
        [9, 8, 7]
    """
    for i in range(n): # Keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):

            if items[j] > items[i]: # if this items is greater than the next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two!

    #get the last two items
    top_n = items[-n:]    

    # return in ascending order
    return items[::-1]