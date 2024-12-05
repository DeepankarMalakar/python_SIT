# Binary search 
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid      # Element found
        elif arr[mid] < target:
            left = mid + 1    # Search in right
        else:
            right = mid - 1   # Search in left
    return -1

arr = [1, 2, 8, 3, 9, 20, 5, 4]
arr.sort()
target = int(input("Enter a target number: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the array")