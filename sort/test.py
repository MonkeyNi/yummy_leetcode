## Ref: https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from hill_sort import hill_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

if __name__ == "__main__":
   nums = [5,1,3,6,3,2,7,9,5,3]
   print("Selection sort: {}".format(selection_sort(nums)))
   print("Bubble sort: {}".format(bubble_sort(nums))) 
   print("Insertion sort: {}".format(insertion_sort(nums))) 
   print("Hill sort: {}".format(hill_sort(nums))) 
   print("Merge sort: {}".format(merge_sort(nums))) 
   print("Quick sort: {}".format(quick_sort(nums))) 