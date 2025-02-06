# def find(arr, t):
#     left, right = 0, len(arr) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == t:
#             result = mid
#             left = mid + 1  # Move right to find the last occurrence
#         elif arr[mid] < t:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result

# arr = [1, 2, 2, 3, 3, 5, 5, 5, 6]
# t = 5
# print(find(arr, t))


# def code(arr, x):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == x:
#             return arr[mid]
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return arr[left] if left < len(arr) else -1
# arr = [1, 2, 8, 10, 10, 12, 19]
# x = 5
# print(code(arr, x))


def sample_function(arr, y):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == y:
            return arr[mid]
        elif arr[mid] < y:
            left = mid + 1
        else:
            right = mid - 1
    return arr[right] if right >= 0 else -1

arr = [1, 2, 8, 10, 10, 12, 19]
y = 5
print(sample_function(arr, y))
