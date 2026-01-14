def subset_generate(S:list[int]):
    result = []
    def helper(S:list[int],i:int,subsets:list[int]):
        result.append(subsets[:])
        for k in range(i,len(S)):
            subsets.append(S[k])
            helper(S,k+1,subsets)
            subsets.pop()
        return result
    return helper(S,0,[])
S=[1,2,3]
r=subset_generate(S)
print(f"final result = {r}")
        
            
        
        
        
    