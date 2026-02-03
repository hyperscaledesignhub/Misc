def NQueens_two(n:int):
    
    result =[]
    
    def has_matching(slate,col):
        return True
    
    def helper(slate:list[int],i:int):
        #Base case
        #If the current queen count is 'n',
        # that means we are done
        if i == n:
            return
        #If slate length equal to n then that means
        # we are done
        if len(slate) == n:
            result.append(slate[:])
            return
        
        # Now check the recursive case
        #assume that ith queen position we are searching
        
        for col in range(0,n):
            if has_matching(slate,col):
                #There is no old queen present which 
                #conflict the current position in the 
                #slate
                # now we can add to the slate
                # here row position is indicated by the index 
                # of the col
                slate.append(col)
                
            