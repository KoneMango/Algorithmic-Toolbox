def dfs(num_str, key):
    if key >= len(num_str):
        return 0
    if num_str[key] == '1':
        return 1 + dfs(num_str, key+1)
    else:
        return dfs(num_str, key+1)
    return dfs(bin(n)[2:], 0)

        
