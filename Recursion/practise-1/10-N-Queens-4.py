def Nqueens(n:int):
    
    result = []
    def check_conflict(slate:list[int],col:int):
        #Here we are traversing only from 0 to len(slate)
        for row in range(len(slate)):
            #First check col 
            if slate[row] == col:
                return False
            #i'th queen pos = (len(slate),col)
            #Existing queen pos at row = (row,slate[row])
            rowdiff = abs(len(slate) - row)
            coldiff = abs(slate[row]-col)
            if rowdiff == coldiff:
                return False
        return True
    def helper(slate:list[int],i:int):
        
        #Base case
        if i == n:
            result.append(slate[:])
            return
        
        #Recursive case
        for col in range(n):
            if check_conflict(slate,col):
                slate.append(col)
                helper(slate,i+1)
                slate.pop()
    helper([],0)
    return result
board = 4
r=Nqueens(board)
print(f"For the given board of size {board}, queens are {r} ")
        