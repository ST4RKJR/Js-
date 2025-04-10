#Richest Customer Width
# Function to calculate the wealth of the richest customer
def richest_customer(accounts):
    # Calculate the wealth of each customer and find the maximum wealth
    max_wealth = max(sum(customer) for customer in accounts)
    return max_wealth

# Input
m, n = map(int, input().split())
accounts = []
for _ in range(m):
    accounts.append(list(map(int, input().split())))

# Output the richest customer's wealth
print(richest_customer(accounts))


class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for account in accounts:
            current_wealth = sum(account)
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth