# Compute the KMP prefix table
def compute_prefix_table(pattern):
    n = len(pattern)
    prefix_table = [0] * n
    j = 0  # Length of the previous longest prefix suffix

    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table