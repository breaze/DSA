def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the midpoint of the list and divide into sublist
    Conqueror: Recursovely sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    l += left[i:]
    l += right[j:]
    return l


alist = [95, 54,62,93,17,77,31,44,55,20]
sorted_list = merge_sort(alist)
print(sorted_list)