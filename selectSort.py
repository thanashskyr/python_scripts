import bubbleSort
import quickSort
import insertionSort
import selectionSort
import time

yourList=input("type a list of numbers you want to sort separated by spaces:")
inputList=list(map(int, yourList.split()))
sort= input("wich sort algorithm you prefer? bubbleSort, quickSort, insertionSort, selectionSort?"  )

start_time=time.time()
if   sort=="bubbleSort":
     print (bubbleSort.bubble(inputList))
elif sort=="quickSort":    
     print (quickSort.quick_sort(inputList))
elif sort=="insertionSort":
     print (insertionSort.insertion_sort(inputList))
elif sort=="selectionSort":     
     print (selectionSort.selection_sort(inputList))
else:
    print("Not such a sorting algorithm available")     
end_time=time.time()
print("The script took", round((end_time - start_time)*1000, 2), "milliseconds to run.")