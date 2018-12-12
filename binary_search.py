def binary_search(input_array, value):
    start = 0
    end = len(input_array)
    
    while start <= end:
        search = int( (end+start) / 2)
        search_value = input_array[search]
        if input_array[search] == value: return search
        elif input_array[search] < value: start = search+1
        elif input_array[search] > value: end = search-1

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))
