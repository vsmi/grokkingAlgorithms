def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)): # начинаем поиск с первого элемента, т к нулевой уже записали в smallest_index
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def sort(arr):
    newarr = []
    for i in range(len(arr)): # Поиск по всему массиву
        smallest = find_smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


arr = [5, 4, 6, 1]
print(sort(arr))