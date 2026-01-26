def permutation_mutable(S:list[int]):
    
    result = []
    
    def helper(i:int):
        #Base case
        if i == len(S):
            result.append(S[:])
            return
        
        #Recursive case
        for k in range(i,len(S)):
            S[i],S[k]=S[k],S[i]
            helper(i+1)
            S[i],S[k] = S[k],S[i]
    helper(0)
    return result
input=[1,2,3]
r=permutation_mutable(input)
print(f"For the given input {input} output is {r}")

        
        