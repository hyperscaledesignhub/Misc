def permute_duplicates(s:list[int]):
    result = []
    def helper(slate:list[int],i:int):
        #Base case
        if len(s) == i:
            result.append(slate[:])
            return
        #Recursive case
        hmap={}
        for k in range(i,len(s)):
            if s[k] not in hmap:
                hmap[s[k]] = 1
                s[i],s[k] = s[k],s[i]
                slate.append(s[i])
                helper(slate,i+1)
                slate.pop()
    helper([],0)
    return result
input=[1,3,3,4]
r=permute_duplicates(input.copy())
print(f"permutation with duplicates of input {input} is {r}")

    
                
        