
def bsearch_rc (arr, start, end, key):
    if end >= start :
        mid = start + (end-start)/2 

        if arr[mid] == key :
            return mid
        elif arr[mid] > key :
            return bsearch_rc(arr, start, mid-1, key)
        else :
            return bsearch_rc(arr, mid+1, end, key)
    else: 
        return -1


def bsearch_it (arr, start, end, key):
    while end >= start  :
        mid = start + (end-start)/2;

        if arr[mid] == key :
            return mid
        elif arr[mid] > key :
            end = mid-1
        else :
            start = mid+1
            
    return -1

def main():
    arr = [0, 1, 4, 7, 8, 9, 10, 12, 35, 56]

    idx = bsearch_it(arr, 0, len(arr)-1, 10)
    print(idx)

    idx = bsearch_rc(arr, 0, len(arr)-1, 9)
    print(idx)

if __name__ == "__main__": main()



        
