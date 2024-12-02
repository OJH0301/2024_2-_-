from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from HeapSort import heapSort
from MergeSort import merge_sort_with_stats
from QuickSort import quick_sort_with_stats
from RadixSort import radix_sort
from ShellSort import shell_sort

array_input = input("* Please input a data list : ")
array = [int(num.strip()) for num in array_input.split(",")]

print("* Target Sorting Algorithm List\nSelection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),\nHeap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
command = input("* Select sorting algorithm : ")

if command == 'SEL':
    data = list(array)
    selection_sort(data)

elif command == 'INS':
    data = list(array)
    insertion_sort(data)

elif command == 'BUB':
    data = list(array)
    bubble_sort(data)

elif command == 'SHE':
    data = list(array)
    shell_sort(data)

elif command == 'HEA':
    data = list(array)
    heapSort(data)

elif command == 'MER':
    data = list(array)
    merge_sort_with_stats(data)

elif command == 'QUI':
    data = list(array)
    quick_sort_with_stats(data)

elif command == 'RAD':
    data = list(array)
    radix_sort(data)
