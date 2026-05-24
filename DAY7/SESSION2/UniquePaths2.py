def unique_paths2(arr):
    m = len(arr)
    n = len(arr[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    if arr[0][0] == 1:
        return 0
    dp[0][0] = 1

    # First row
    for j in range(1, n):
        if arr[0][j] == 0:
            dp[0][j] = dp[0][j - 1]

    # First column
    for i in range(1, m):
        if arr[i][0] == 0:
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j]==1:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[m-1][n-1]


# Sample Input
arr = [
    [0,0, 0],
    [0,1,0],
    [0,0, 0]
]
print(unique_paths2(arr))