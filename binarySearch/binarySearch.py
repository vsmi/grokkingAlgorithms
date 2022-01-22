import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Arguments for binary search: list and item')
    parser.add_argument("--list", nargs="*", default= [1, 3, 5, 7, 9], type = int, help='List for search')
    parser.add_argument("--item", type = int, help='item - we need to find it')
    args = parser.parse_args()
    return args



def binary_search(list, item):
    low = 0
    high = len(list)-1 

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]      

        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1  
        elif guess == item:
            return(mid)
        else:
            return None

def main():
    args = get_args()
    print(binary_search(args.list, args.item))

if __name__ == '__main__':
    main()
            


