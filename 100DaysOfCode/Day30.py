#Winner of the circular game
def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    index = 0
    
    while len(friends) > 1:
        index = (index + k - 1) % len(friends)
        friends.pop(index)
    
    return friends[0]


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle: list[int] = [num for num in range(1, n + 1, 1)]
        cur_ind: int = 0

        while len(circle) != 1:
            next_to_remove: int = (cur_ind + k - 1) % len(circle)
            circle.pop(next_to_remove)
            cur_ind = next_to_remove

        return circle[0]