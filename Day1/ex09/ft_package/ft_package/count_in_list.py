"""Test file or package"""


def count_in_list(lst: list, cmp):
    """Parse list elements and compare them with the comparator,
return the number of positive comparisons"""
    ct = 0
    for i in lst:
        if i == cmp:
            ct += 1
    return ct
