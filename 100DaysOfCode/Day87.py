def make_good(s: str) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def countBalancedSubarrays(N, K, arr, a, b):
    count_a = 0
    count_b = 0
    result = 0

    # Initialize first window
    for i in range(K):
        if arr[i] == a:
            count_a += 1
        elif arr[i] == b:
            count_b += 1

    if count_a == count_b and count_a > 0:
        result += 1

    # Slide the window
    for i in range(K, N):
        # Remove left element
        if arr[i - K] == a:
            count_a -= 1
        elif arr[i - K] == b:
            count_b -= 1

        # Add right element
        if arr[i] == a:
            count_a += 1
        elif arr[i] == b:
            count_b += 1

        # Check balance
        if count_a == count_b and count_a > 0:
            result += 1

    return result


# Driver code for testing
if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    a, b = map(int, input().split())
    print(countBalancedSubarrays(N, K, arr, a, b))
