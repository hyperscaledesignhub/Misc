def palindrome_partition(s:str):
    result = []
    
    #Checking here whether the given 
    #string is a palindrome or not
    def ispalindrome(st:str):
        i = 0
        while i <= len(st)/2:
            if st[i] != st[len(st)-1 -i]:
                return False
            i +=1
        return True
    
    def helper(array:str,i:int,slate:list[str]):
        
        #Back tracking cases
        #If we keep the backtracking case after the 
        # Based case below we won't get the correct
        #result 
        if len(slate) > 0 and not ispalindrome(slate[-1]):
            return
        
        #Base cases
        if i == len(array):
            result.append(slate[:])
            return
        
        
        
        
        #Recursive case
        #i am starting from position 'i' up to len(array)
        #i am adding to the slate from 'i' to pick+1
        #where pick is index from i tp len(array)
        #That means i am adding to the slate for ex: i have string
        #  aabddd, i =2, i am adding to slate: b, bd, bdd,bddd
        #so for every iteration of the pick i am doing the 
        #following
        #adding to slate from i to pick. After that 
        #calling my subordinate to start from pick+1 and find any
        #palindromes 
        #once my subordinate comes back, then i am erasing 
        #from slate and again calling from next pick value
        for pick in range(i,len(array)):
            slate.append(array[i:pick+1])
            helper(array,pick+1,slate)
            slate.pop()
    helper(s,0,[])
    return result
input = "aabaa"
r = palindrome_partition(input)
print(f" For the given input {input} palindrome partition is {r}")
    
        