# recursive way to search the array  
def binary_search(arr, low, high, item):
   if low <= high:
      mid = (low + high) // 2

      if arr[mid] == item:
         return mid
      elif arr[mid] > item:
         return binary_search(arr, low, mid - 1, item)
      else:
         return binary_search(arr, mid+1, high, item)
   else:
      return -1

# without recursive to search array
def binary_search(l, key):
   sorted_array =  l.sort()
   low, high = 0, len(l) - 1
   while low <= high:
      mid = (low+high) // 2
      if key == l[mid]:
         return mid
      elif key > l[mid]:
         low = mid + 1
      elif key < l[mid]:
         high = mid - 1
   return "not found"
a = [3,5,6,7,8]
print(binary_search(a,8))
