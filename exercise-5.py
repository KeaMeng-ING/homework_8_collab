"""
Create and return a new Iterable that contains the same elements as the given list items,
but with the reversed order of the elements inside every maximal strictly ascending subsequence. 
This function should not modify the contents of the original list.

"""

def reverse_ascending(numbers):
    result = [] # List to store the result
    subsequence = [] # List to store the subsequence

    # Iterate through the numbers
    for i in range(len(numbers)):
        # If the subsequence is empty or the current number is greater than the last number in the subsequence
        if len(subsequence) == 0 or numbers[i] > subsequence[-1]: #
            subsequence.append(numbers[i]) # Add the number to the subsequence
        else:
            result.extend(subsequence[::-1]) # Add the reversed subsequence to the result
            subsequence = [numbers[i]]
        if i == len(numbers) - 1: # If the current number is the last number in the list
            result.extend(subsequence[::-1]) # Add the reversed subsequence to the result

    return result
