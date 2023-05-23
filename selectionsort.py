def selection_sort(array):
  for i in range(len(array) - 1):
    smallest = i
    for j in range(i + 1, len(array)):
      if array[j] < array[smallest]:
        smallest = j
    array[i], array[smallest] = array[smallest], array[i]


# Get the user input
array = list(map(int, input("Enter a list of numbers: ").split()))

# Sort the array
selection_sort(array)

# Print the sorted array
print("The sorted array is:", array)