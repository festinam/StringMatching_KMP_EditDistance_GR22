# KMP Search function
def kmp_search(text, pattern):
    prefix_table = compute_prefix_table(pattern)
    matches = []
    j = 0  # Index for pattern

    for i in range(len(text)):  # Index for text
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = prefix_table[j - 1]
    return matches
