def is_sorted(lst, starting_index):
    l = len(lst)
    if l == starting_index or l-1 == starting_index:
        return True
    elif lst[starting_index] > lst[starting_index+1]:
        return False
    return is_sorted(lst, starting_index+1)
print(is_sorted([1,2,3,4,4,6],0))
print(is_sorted([24,25,1,2,99],0))