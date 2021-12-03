def binary_search(list, target):
    max = len(list)
    min = 0
    i = 0
    while(min<len(list)-1 and max >0):
        target_position = round((max+min)/2)
        if list[target_position] == target:
            return target_position
        elif target > list[target_position]:
            min = target_position
        else:
            max = target_position
        i = i + 1
    return -1


list = list(range(0,100))
target_position = binary_search(list=list, target=80)
print(target_position)