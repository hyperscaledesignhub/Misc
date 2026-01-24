def susbets_new_approach(s:list[str]):
    
    result = []
    
    def helper(slate:list[str],i:int):
        
        #Also i am adding result as is
        result.append(slate[:])
        
        #recursive case
        for k in range(i,len(s)):
            slate.append(s[k])
            helper(slate,k+1)
            slate.pop()
    helper([],0)
    return result
input=['1','5','9','7']
r=susbets_new_approach(input)
print(f"new approach subsets of {input} are {r}")