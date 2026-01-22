def palindrome_partition(s:str):
    
    n = len(s)
    if n == 0:
        return [[]]
    #Pre compute Palindrome table
    is_palindrome = [[False]*n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        is_palindrome[i][i] = True
    #Check for palindrome of length 2
    for i in range(n-1):
        is_palindrome[i][i+1] = (s[i]== s[i+1])
    #Check for palindrome of length 3 or more
    
    for length in range(3,n+1):
        for i in range(n-length+1):
            j = i+length-1
            #For ex: i,j = (0,3) => s[i] == s[j] and s[i+1][j-1]
            #, i.e., the string s[1:4] must be palndrome, which 
            # is given by our table s[i+1][j-1] = True
            is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i+1][j-1]
    result = []
    def backtrack(start:int, current_partition:list):
        #base case, reached end of the string
        if start == n:
            result.append(current_partition[:])
            return
        # Try all substrings starting from start
        for end in range(start,n):
            if is_palindrome[start][end]:
                current_partition.append(s[start:end+1])
                backtrack(end+1,current_partition)
                current_partition.pop()
    backtrack(0,[])
    return result
input='aba'
r=palindrome_partition(input)
print(f"For a given value input={input} partitioned palindrome is {r}")
        