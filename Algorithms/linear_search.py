def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

list = [30, 25, 2, 15, 29, 5, 4, 36]
target_position = linear_search(list=list, target=59)
print(target_position)