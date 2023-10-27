def flatten_and_sort(array):
    array = []
    for j in array:
        for i in j:
            array.append(i)
    return sort(array)