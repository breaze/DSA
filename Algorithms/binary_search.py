def binary_search(list, target):
    max = len(list) - 1
    min = 0
    # while(min<len(list)-1 and max >0):
    while min <=max:
        target_position = round((max+min)/2)
        if list[target_position] == target:
            return target_position
        elif target > list[target_position]:
            min = target_position + 1
        else:
            max = target_position - 1
    return None

list = list(range(38,100))
target_position = binary_search(list=list, target=40)
print(target_position)