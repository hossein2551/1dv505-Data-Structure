

def selection_sort(array):

    for i in range(len(array)):

        min_index = i

        for j in range(i + 1, len(array)):

            if array[j] < array[min_index]:

                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array




def bubble_sort(array):

    n = len(array)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:

            break

    return array



def insertion_sort(array):

    for i in range(1, len(array)):

        key = array[i]

        j = i - 1

        while j >= 0 and array[j] > key:

            array[j + 1] = array[j]

            j -= 1

        array[j + 1] = key
        
    return array