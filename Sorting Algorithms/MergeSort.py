def Mergesort(array):
    if len(array) > 1:
        m = len(array) // 2
        L = array[:m]
        R = array[m:]

        Mergesort(L)
        Mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

def printarray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    A = [9, 8, 7, 6, 5]
    Mergesort(A)
    printarray(A)
