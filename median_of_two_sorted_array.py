#! /usr/bin/python
import pdb


def search_median(a1, a2):
    n = len(a1)
    l = 0
    h = n - 1 
    while l < h:
        #pdb.set_trace()
        mid = (l + h)/2
        if n - mid < n:
            if a2[n-mid-1] <= a1[mid] <= a2[n-mid]:
                return a1[mid]
            elif a1[mid] < a2[n-mid-1]:
                l = mid + 1
            else:
                h = mid - 1
        else:
            if a2[n-mid-1] <= a1[mid]:
                return a1[mid]
            else:
                l = mid + 1
    return None

def get_median(a1, a2):
    """Search for the median of the union of two sorted array of the same length"""
    # First do a binary search in a1.
    x = search_median(a1, a2)
    if x is None:
        x = search_median(a2, a1)
    return x

if __name__ == "__main__":
    a1 = [1, 2, 5, 6, 8]
    a2 = [3, 4, 17, 30, 45]
    print get_median(a1, a2)

