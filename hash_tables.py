import sys
from collections import defaultdict


# Find sequence which sum is equal to `s`
def find_sequence_equal_sum(array: list, n: int, s: int):
    """
    Parameters
    ----------
    array: list
        Array
    n: int
        Array size
    s: int
        Sum

    """
    hash_table, current_sum = {}, 0

    for i in range(0, n):
        current_sum += array[i]

        if current_sum == s:
            print(f"Start: 0 | End: {i}")
            return

        if (diff := current_sum - s) in hash_table:
            print(f"Start: {hash_table[diff] + 1} | End: {i}")
            return

        hash_table[current_sum] = i
    else:
        print("No subarray was found")


# Find length of the longest increasing subsequence whose 
# adjacent element differ by 1
def longest_subseq(array: list, n: int):
    mp = {}
    dp = [0 for _ in range(n)]

    maximum = -sys.maxsize
 
    for i in range(n):
        # if a[i]-1 is present before i-th index
        if (prev := array[i] - 1) in mp:
            # Last index of a[i]-1
            dp[i] = 1 + dp[mp[prev] - 1]
        else:
            dp[i] = 1

        mp[array[i]] = i + 1
 
        # Stores the longest length
        maximum = max(maximum, dp[i])

    return maximum


# Find the length of largest subarray with 0 sum
def longest_subarr_0_sum(arr):
    hash_map, max_len, curr_sum = {}, 0, 0

    for i in range(len(arr)):
        # Add the current element to the sum
        curr_sum += arr[i]
 
        if curr_sum == 0: max_len = i + 1
 
        # Look if current sum is seen before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
 
    return max_len


# Find the most frequent element in array
def most_frequent(arr: list):
    # Insert all elements in Hash.
    hash = {}

    for i in range(len(arr)):
        if arr[i] in hash.keys():
            hash[arr[i]] += 1
        else:
            hash[arr[i]] = 1

    # Find the max frequency
    max_count = 0
    res = -1

    for i in hash:
        if max_count < hash[i]:
            res = i
            max_count = hash[i]

    return res


if __name__ == "__main__":
    array = [10, -2, 3, 2, -20, 10]
    find_sequence_equal_sum(array, len(array), -10)
    print()

    array = [10, 3, 7, 4, 5, 6, 11, 12, 13, 14, 15, 7]
    len_max = longest_subseq(array, len(array))
    print(len_max)
