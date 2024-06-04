def find_largest(arr):
    if len(arr) == 0:
        return None
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

 
arr = [10, 20, 4, 45, 99]
print(f"The largest element in the array is {find_largest(arr)}")

