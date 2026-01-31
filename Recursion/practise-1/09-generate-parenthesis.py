def generate_parenthesis(n:int):
    
    result = []
    #We need to define left paranthesis and rightparenthesis
    #these counts define that we have got proper
    #combinations or not and there by getting result 
    def helper(leftnum:int, rightnum:int,slate:list[str]):
        #Base case-1
        #While decrementing the leftnumber we face the case 
        #Where suppose the left paranthesis count greater than
        #right means, that we shouldn't allow this scenario
        #We have to prune this
        #Why we are not checking: rightnum > leftnum: Because
        #First we have to add leftparanthesis not the right
        #hence we are checking left, suppose right paranthesis
        #greater than left wouldn't we arrive this? 
        if leftnum >  rightnum or leftnum < 0 or rightnum < 0:
            return 
        #Base case 2: Result case, when leftnum=rightnum =0 
        #That means we added all parenthesis evenly
        if leftnum == rightnum == 0:
            result.append(slate[:])
            return
        #Recursive case
        
        #1. we append left parenthesis to the slate
        # We call the sub ordinate to finish adding
        # the remaining right paranthesis to the slate
        
        slate.append("(")
        # we decrease the count of left paranthesis and call 
        # the subordinate
        helper(leftnum-1,rightnum,slate)
        
        #Subordinate came back by adding first sufficient 
        #number of right paranthesis, now we clean the slate
        #whatever i have added.
        #So that i call next suordinate to add the right paranthesis
        slate.pop()
        
        slate.append(")")
        
        #Now call the subordinate to add the remaining left
        #subordinates 
        
        helper(leftnum,rightnum-1,slate)
        slate.pop()
    helper(n,n,[])
    return result
input=2
r=generate_parenthesis(input)
print(f"Output of the {input} parenthesis is {r}")
input=3
r=generate_parenthesis(input)
print(f"Output of the {input} parenthesis is {r}")
        