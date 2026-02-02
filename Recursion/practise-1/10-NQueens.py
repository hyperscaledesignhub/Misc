def NQueens(n:int):
    #Store the result
    
    result =[]
    
    def check_conflict(col:int,slate:list[int]):
        #Currently  queen is at the position of 
        #(len(slate),col) 
        #For this position of the queen we are checking
        #for existing queen at the (rowindex,slate[rowindex])
        #using 2 conditions, 
        # First condition is existing queen at slate[rowindex] and col where we want to place
        # the new queen are same, then return immediately
        #Next second condition is:
        #Checking existing queen position, (rowindex,slate[rowindex]) and 
        #new queen position (len(slate),col), check for the rowdiff and coldiff values
        #if both are same then this position doesn't suite for the new queen
        for rowindex in range(0,len(slate)):
            
            if slate[rowindex] == col:
                return False
            #existing queen's pos: (rowindex,slate[rowindex])
            #new queen where we want to place:  (len(slate),col)
            rowdiff = abs(rowindex - len(slate))
            coldiff = abs(col - slate[rowindex])
            if rowdiff == coldiff:
                return False
        return True
    def helper(slate,i,n):
        #i is the index of the current queen
        #if i'th index equal to total queen count, then 
        #return, we are done
        if i == n:
            result.append(slate[:])
            return
        #Now check for each col where we can
        #place the current queen 'i'
        for col in range(0,n):
            if check_conflict(col,slate):
                #There is no queen present at the position (len(slate),col)
                #hence we are adding to the slate
                slate.append(col)
                helper(slate,i+1,n)
                slate.pop()
    helper([],0,n)
    return result
n=4
r= NQueens(n)
print(f" for the given {n} queens result = {r}")

                
        
        
    