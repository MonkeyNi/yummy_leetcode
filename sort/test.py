## Ref: https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

from selection_sort import selection_sort
from bubble_sort import bubble_sort

if __name__ == "__main__":
   nums = [5,1,3,6,3,2,7,9,5,3]
   print("Selection sort: {}".format(selection_sort(nums)))
   print("Bubble sort: {}".format(bubble_sort(nums))) 