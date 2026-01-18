def generate_parenthesis(n:int):
    
    result=[]
    
    def helper(leftnum:int, rightnum:int,slate:list[str]):
        
        if leftnum > rightnum or leftnum < 0 or rightnum < 0:
            return
        if leftnum == rightnum == 0:
            #print(f"slate value is {slate}")
            result.append(slate[:])
            return
        slate.append("(")
        helper(leftnum-1,rightnum,slate)
        slate.pop()
        
        slate.append(")")
        helper(leftnum,rightnum-1,slate)
        slate.pop()
    helper(n,n,[])
    return result
input=3
r=generate_parenthesis(input)
print(f"result of generate_parenthesis of {input}, count of parenthesis \
      is {len(r)},value is {r}")

        
    
    