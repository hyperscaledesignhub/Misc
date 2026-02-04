

def NQueens_two(n:int):
    
    result = []
    
    def check_right_pos(col:int, slate:list[int]):
        
        #Go through all the rows from 0 to len(slate)
        # and find out that there is no coflict of the 
        #current queen's intended position len(slate),col
        #with the all existing slots from row = 0 to len(slate)
        #if slate[rowindex] has some value then that  rowindex,value (col) there
        # is already a queen
        #Now we need to check for a given row, the value of slate[rowindex] which is
        # columns suppose row-3, index of slate 3 has value 4, 
        # that means there queen present in col-4, if a queena lready present
        #in col 4 that means its ruling all columns. We can't
        #place another queen there. It doesn't matter which row
        #this queen is present. We row-0, 1 or 2or 23.. if its preesnt in col=5
        # that means we can't place any queen there
        for rowindex in range(len(slate)):
            if slate[rowindex] == col:
                return False
            #Now check intended position (len(slate),col) and current position (rowindex,slate[rowindex])
            # diagonal match of the queen
            #For diagonal match we should be checking the rowdiff and coldiff
            rowdiff = abs(len(slate) - rowindex)
            coldiff = abs(col - slate[rowindex])
            if rowdiff == coldiff:
                return False
        return True
    
    def helper(slate:list[int],i:int):
        
        #First define the base case 
        #Check we finished all the queens
        if i == n:
            result.append(slate[:])
            return
        #Now check that we filled the slate with 
        #all the values 
        
        
        #Now define the recursive case
        for col in range(0,n):
            if check_right_pos(col,slate):
                #There is no queen present in len(slate),col
                #Hence add queen to the slate
                slate.append(col)
                #Now call subordinate to fill the i+1'st queen in the slate
                helper(slate,i+1)
                #Subordinate has filled the i+1'st queen. 
                #Now i am cleaning the slate
                slate.pop()
    helper([],0)
    return result
n=4
r=NQueens_two(n)
print(f" For the given N queens of the size {n} result is {r}")

n=2
r=NQueens_two(n)
print(f" For the given N queens of the size {n} result is {r}")
                
            