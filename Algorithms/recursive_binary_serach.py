def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        target_position = round(len(list)/2)
        if list[target_position] == target:
            return True
        elif list[target_position] < target:
            return recursive_binary_search(list[target_position+1:], target)
        else:
            return recursive_binary_search(list[:target_position], target)

list = list(range(38,100))
target_position = recursive_binary_search(list=list, target=40)
print(target_position)