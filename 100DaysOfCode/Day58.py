def subarraySumLL(head, K):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # Initialize with prefix_sum = 0 having count 1

    current = head
    while current:
        # Add the current node's value to the prefix sum
        prefix_sum += current.data

        # Check if (prefix_sum - K) exists in the map
        if (prefix_sum - K) in prefix_map:
            count += prefix_map[prefix_sum - K]

        # Update the map with the current prefix sum
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else:
            prefix_map[prefix_sum] = 1

        # Move to the next node
        current = current.next

    return count
