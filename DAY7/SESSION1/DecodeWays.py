def decodeways(s):
    # If string is empty or starts with 0
    if not s or s[0] == '0':
        return 0

    n = len(s)

    # DP array
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Fill DP array
    for i in range(2, n + 1):

        # Single digit check
        one_digit = int(s[i - 1:i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        # Two digit check
        two_digit = int(s[i - 2:i])

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# Driver code
string = input("Enter numeric string: ")

result = decodeways(string)

print("Number of ways to decode:", result)