def combinations(n:int,k:int):
    result=[]
    def helper(slate:list[int],i:int):
        #Base case
        if len(slate) == k:
            result.append(slate[:])
            return  
        if i == n+1:
            return
        #Recursive case
        #Exclude adding to slate
        helper(slate,i+1)
        #include adding to slate
        slate.append(i)
        helper(slate,i+1)
        slate.pop()
    helper([],1)
    return result
input=4
k=2
r=combinations(input,k)
print(f"combinations of input = {input} with chosing {k} at a time are {r}")
    