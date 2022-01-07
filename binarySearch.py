def binary_search(list, item):
    low = 0
    high = len(list)-1 
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        #print(mid)
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1  
        if guess == item:
            return(guess)
        else:
            return None


test_list = [1, 3, 5, 7, 9, 11]

print(binary_search (test_list, 3))
print(binary_search (test_list, -1))

