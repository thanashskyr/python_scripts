def selection_sort(list_b):
    indexing_length= range(0, len(list_b) - 1)
    for i in indexing_length:
         min_value_index = i
         for j in range(i+1, len(list_b)):
            if list_b[j]<list_b[min_value_index]:
                min_value_index=j

         if min_value_index !=i:
                   list_b[min_value_index], list_b[i] = list_b[i], list_b[min_value_index]

    return list_b

        