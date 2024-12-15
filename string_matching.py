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

# Rabin-Karp Search function
def rabin_karp_search(text, pattern):
    prime = 101  # A prime number for hashing
    m, n = len(pattern), len(text)
    base = 256  # Base for ASCII characters
    pattern_hash = 0
    text_hash = 0
    window_start = 0
    matches = []

    # Calculate the hash for the pattern
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime

    # Calculate the initial hash for the first window of text
    for i in range(m):
        text_hash = (text_hash * base + ord(text[i])) % prime

    # Rolling hash: slide the window across the text
    for window_end in range(m, n + 1):
        if pattern_hash == text_hash and text[window_start:window_end] == pattern:
            matches.append(window_start)

        # Slide the window: calculate the hash for the next window
        if window_end < n:
            text_hash = (base * (text_hash - ord(text[window_start]) * (base ** (m - 1))) + ord(text[window_end])) % prime
            text_hash = text_hash if text_hash >= 0 else text_hash + prime
            window_start += 1

    return matches

# Edit Distance 
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Insert all characters of s2
            elif j == 0:
                dp[i][j] = i  # Remove all characters of s1
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n];
