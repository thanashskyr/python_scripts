import bubbleSort
import quickSort
import insertionSort
import selectionSort
import time

yourList=input("Type a list of numbers you want to sort separated by spaces: ")
inputList=list(map(int, yourList.split()))
sort= input("Which sort algorithm you prefer? 1. bubbleSort , 2. quickSort, 3. insertionSort , 4. selectionSort ? Choose a number: "  )

start_time=time.time()
if   sort=="1":
     print (bubbleSort.bubble(inputList))
elif sort=="2":    
     print (quickSort.quick_sort(inputList))
elif sort=="3":
     print (insertionSort.insertion_sort(inputList))
elif sort=="4":     
     print (selectionSort.selection_sort(inputList))
else:
    print("Not such a sorting algorithm available")     
end_time=time.time()
print("The script took", round((end_time - start_time)*1000, 2), "milliseconds to run.")