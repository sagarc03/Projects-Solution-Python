def bubbleSort(arr):
  for i in range(len(arr)):
    swaped = False
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swaped = True
    if not swaped:
      break

arr = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(arr)
print(arr)
