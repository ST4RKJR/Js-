def maxStreak(s, X):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(s)):
        if s[right] == '0':
            zero_count += 1

        while zero_count > X:
            if s[left] == '0':
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
