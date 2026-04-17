





def merge_sort(lst):
    
    if len(lst) <= 1:

        return lst

   
    mid = len(lst) // 2

    left = merge_sort(lst[:mid]) 

    right = merge_sort(lst[mid:])  

    
    return merge(left, right)



def merge(left, right):

    sorted_list = []  

    i = j = 0 

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            sorted_list.append(left[i])  

            i += 1

        else:
            sorted_list.append(right[j])  

            j += 1

    
    sorted_list.extend(left[i:])

    sorted_list.extend(right[j:])

    return sorted_list





def quick_sort(lst):


    if len(lst) <= 1:  

        return lst


    pivot = lst[-1]

    left = [x for x in lst[:-1] if x <= pivot]  

    right = [x for x in lst[:-1] if x > pivot]  

    
    return quick_sort(left) + [pivot] + quick_sort(right)




