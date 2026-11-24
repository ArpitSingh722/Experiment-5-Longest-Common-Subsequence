def longest_common_subsequence(seq1, seq2):
    """Return the LCS and its length using bottom-up dynamic programming."""
    m, n = len(seq1), len(seq2)

    # dp[i][j] stores the LCS length of seq1[i:] and seq2[j:].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if seq1[i] == seq2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # Reconstruct one longest common subsequence.
    lcs = []
    i = j = 0

    while i < m and j < n:
        if seq1[i] == seq2[j]:
            lcs.append(seq1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return lcs, dp[0][0]


def read_sequence(prompt):
    """Read a sequence; space-separated input is treated as separate items."""
    value = input(prompt).strip()
    return value.split() if " " in value else list(value)


def main():
    print("LONGEST COMMON SUBSEQUENCE (DYNAMIC PROGRAMMING)")
    print("Enter characters together (e.g. ABCBDAB) or items separated by spaces.")
    sequence1 = read_sequence("Enter the first sequence: ")
    sequence2 = read_sequence("Enter the second sequence: ")

    lcs, length = longest_common_subsequence(sequence1, sequence2)

    print("\nLongest Common Subsequence:", " ".join(lcs) if lcs else "(empty)")
    print("Length of LCS:", length)


if __name__ == "__main__":
    main()
