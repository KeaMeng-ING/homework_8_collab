def chunking_by(numbers, chunck):
    
    result = []
    
    for i in range(0, len(numbers), chunck):
        result.append(numbers[i:i + chunck])

    return result

