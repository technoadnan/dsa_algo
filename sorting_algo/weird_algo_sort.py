# Monkey sort
import time, random
def is_sorted(arr):

   sorted = True
   for i in range(len(arr) - 1):
      if arr[i]>arr[i+1]:
         sorted = False
   
   return sorted

def monkey_sort(arr):

   while not is_sorted(arr):
      # time.sleep(1)
      random.shuffle(arr)
      # print(arr)
   print(arr)

monkey_sort([2, 1, 3, 4])

# Sleep sort

# the concept given a array the numbers will print based on the time. So, the less the number is the less the earlier it will print. 