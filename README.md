# Experiment 05 – Longest Common Subsequence (LCS)

## Aim
Apply dynamic programming to determine the longest common subsequence between two sequences.

## Description
This program finds the Longest Common Subsequence (LCS) of two input sequences using the bottom-up dynamic programming approach. A subsequence keeps the original order of elements, but the elements do not need to be adjacent.

The program displays one LCS and its length.

## Files
- `lcs.py` – Main Python implementation.
- `test_lcs.py` – Unit tests for the LCS function.
- `sample_input.txt` – Example input.
- `sample_output.txt` – Expected output for the example.
- `requirements.txt` – External dependencies (none required).

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:

```bash
python lcs.py
```

Enter each sequence when prompted. Enter characters together (such as `ABCBDAB`) or enter separate items with spaces (such as `A B C D`).

## Sample
First sequence: `ABCBDAB`  
Second sequence: `BDCABA`

One valid LCS is `BCBA` (another valid LCS may also be produced). Its length is `4`.

## Algorithm
1. Create a two-dimensional DP table.
2. Fill the table from the end of both sequences toward the beginning.
3. If the current elements match, add 1 to the diagonal value.
4. Otherwise, take the maximum of the value below and the value to the right.
5. Trace through the table to reconstruct one LCS.

## Complexity
- **Time Complexity:** `O(m × n)`
- **Space Complexity:** `O(m × n)`

Here, `m` and `n` are the lengths of the two input sequences.
