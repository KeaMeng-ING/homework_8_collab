def replace_last(numbers):
    if len(numbers) > 1:
        numbers.insert(0, numbers.pop())
    return numbers
