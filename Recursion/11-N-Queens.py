def n_queens(n:int):
    result =[]
    
    def non_conflict(slate,col):
        # Return True If an new queen placed at row = len(slate)
        # and col is attacking
        #Or being attacked by existing queen
        #Row numbers are clearly different already
        
        # If any other queen is alraedy lying in that row return false
        for queenrow in range(len(slate)):
            if slate[queenrow] == col:
                return False
            #If any other queen lies in diagonal, then return false
            rowdiff = abs(len(slate)- queenrow)
            coldiff = abs(col - slate[queenrow])
            if rowdiff == coldiff:
                return False
        return True
    def helper(slate,i,n):
        
        if i == n:
            #all N queens have been placed. So Append here
            result.append(slate[:])
            return
        #Recursive case
        for col in range(0,n):
            if non_conflict(slate,col):
                slate.append(col)
                helper(slate,i+1,n)
                slate.pop()
    helper([],0,n)
    return result
n=4
r=n_queens(n)
print(f"The result of {n} rows chess board is {r} ")

        
       
                