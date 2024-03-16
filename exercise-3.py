def remove_all_after(numbers, n):
    new_list = []
    if len(numbers) == 0:
        return []
    for num in numbers:
        new_list.append(num)
        if num == n:
            break
    return new_list


print(remove_all_after([1, 2, 3, 4, 5], 3))
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))
print(remove_all_after([], 2))
print(remove_all_after([1, 1, 3, 3], 2))


