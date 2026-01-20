def palindrome_partition(s:str):
    result = []
    
    def ispalindrome(st:str):
        i=0
        while i<=len(st)/2:
            if st[i] != st[len(st)-1-i]:
                return False
            i +=1
        return True
    def helper(array:str,i:int,slate:list[str]):
        #If the last string of the slate is not palindrome then backtrack
        if len(slate) > 0 and not ispalindrome(slate[-1]):
            return
        #Base case
        if i == len(array):
            result.append(slate[:])
            return
        #Recursive case
        for pick in range(i, len(array)):
            slate.append(array[i:pick+1 ])
            helper(array,pick+1,slate)
            slate.pop()
    helper(s,0,[])
    return result
input = "aabaa"
r=palindrome_partition(input)
print(f"For the given input = {input}, result of palindrome partition is {r}")

            
            
            
            