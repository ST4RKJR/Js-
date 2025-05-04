def max_wealth(accounts):
    # Transpose the matrix to group by banks (columns)
    transposed = list(zip(*accounts))
    
    # Calculate the sum of each bank (column) and find the max
    return max(sum(bank) for bank in transposed)
