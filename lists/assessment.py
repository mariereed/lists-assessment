
"""List Assessment
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_indices(items):
    """Print each item in the list, followed by its index.

    Takes one argument, a list, and returns the item and it's index.
    """

    # Use range() to iterate over a list of indices, for each index
    # call its corresponding value within items.
    for index in range(len(items)):
        print items[index], index


def words_in_common(words1, words2):
    """Find words in common.

    Given 2 lists of words, words1 and words2, return the words that are in
    common between the two, sorted alphabetically.
    """

    #This is how I did it the first time
        # common_set = set([])
        # words1_set = set(words1)
        # words2_set = set(words2)

        # for item in words1_set:
        #     if item in words2_set:
        #         common_set.add(item)
        # return list(common_set)

    # This is how I ultimately chose to do this.
    # Convert my lists into sets so that I can do set-math.
    words1_set = set(words1)
    words2_set = set(words2)

    # Create the intersection set of the two sets and turn this into a list.
    # Then sort the list alphabetically out of place.
    in_common = list(words1_set & words2_set)
    return sorted(in_common)


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    Takes a single argument of type list, returns a list slice.
    """

    # Uses list slicing to skip every other item by having a step of 2.
    return items[::2]


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order.

    Takes two arguments, a list and a non-negative digit. The list is sorted and then sliced
    so that only the smallest n items are returned in reverse order.
    """

    # Items is sorted in place.
    # n of zero is treated differently to avoid unintended splicing.
    # Starting from the nth item, the list is retured in reverse.
    items = sorted(items)
    if n != 0:
        return items[n-1::-1]
    else:
        return []


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
