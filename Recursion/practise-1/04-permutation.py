def permutation(nums:list[int]):
    
    result = []
    
    def helper(slate:list[int], i:int):
        #Base case
        if i == len(nums):
            result.append(slate[:])
            return
        
        #Recursive case
        for k in range(i,len(nums)):
            nums[i],nums[k] = nums[k],nums[i]
            slate.append(nums[i])
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input=[1,2,3]
r=permutation(input)
print(f"Permutation of {input} is {r}")
        