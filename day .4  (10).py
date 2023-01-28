def isScramble(s1: str, s2: str) -> bool:
    if s1 == s2: return True
    if sorted(s1) != sorted(s2): return False
    n, m = len(s1), len(s2)
    dp = [[[False] * (n + 1) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][1] = s1[i] == s2[j]
    for k in range(2, n + 1):
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                for p in range(1, k):
                    if dp[i][j][p] and dp[i + p][j + p][k - p] or dp[i][j + k - p][p] and dp[i + p][j][k - p]:
                        dp[i][j][k] = True
                        break
    return dp[0][0][n]

s1 = "great"
s2 = "rgeat"
if (isScramble(s1, s2)): 
	print("true") 
else: 
	print("false")	 
s1 = "abcde"
s2 = "caebd"
if (isScramble(s1, s2)): 
	print("true") 
else: 
	print("false")	 
s1 = "a"
s2 = "a"
if (isScramble(s1, s2)): 
	print("true") 
else: 
	print("false")	 
s1="ab"
s2="ad"
if (isScramble(s1, s2)): 
	print("true") 
else: 
	print("false")
s1=10
s2=-5
if (isScramble(s1, s2)): 
	print("true") 
else: 
	print("false")
