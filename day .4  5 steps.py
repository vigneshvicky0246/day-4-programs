def min_jumps(arr): 
    n = len(arr)
    jumps = [0 for i in range(n)] 
    if (n == 0) or (arr[0] == 0): 
        return -1
    jumps[0] = 0
    for i in range(1, n): 
        jumps[i] = float('inf') 
        for j in range(i): 
            if (i <= j + arr[j]) and (jumps[j] != float('inf')): 
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
    return jumps[n-1] 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] 
print("Minimum number of jumps to reach the end:", min_jumps(arr)) 
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
print("Minimum number of jumps to reach the end:", min_jumps(arr)) 
arr = [2,3,1,1,4] 
print("Minimum number of jumps to reach the end:", min_jumps(arr)) 
arr = [1, 3, 6, 1, 0, 9] 
print("Minimum number of jumps to reach the end:", min_jumps(arr)) 
arr = [2,3,0,1,4] 
print("Minimum number of jumps to reach the end:", min_jumps(arr))
