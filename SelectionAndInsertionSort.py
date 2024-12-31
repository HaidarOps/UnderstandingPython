



# Selection Sort


def selectionSort(A):

    # First looks at the initial number, checks the entire array tto see if smaller

    print("Entered")

    for i in range(0, len(A)):
        min_index = i

        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp

    return A

#Time to test

print(selectionSort([1, 5, 10, 6, 7, 9]))
        
        
def insertionSort(A):

    for i in range(1, len(A)):

        key = A[i]
        j = i - 1

        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1


        A[j+1] = key
    return A


print(insertionSort([1, 5, 10, 6, 7, 9]))
        
