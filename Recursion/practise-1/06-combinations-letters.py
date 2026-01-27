def letter_combination(s:str):
    digit_to_letters = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
    result = []
    def helper(slate:str,i:int):
        #Base case, we will come here after
        #recursive case
        
        # As a leaf node element i do the following
        # Once i see slate length is  equal to the 
        # input digit 's' length, i will add the result
        # to the output
        
        if len(slate) == len(s):
            result.append(slate[:])
            return
        
        
        #Recursive case
        
        #1. find the current digit index and get the
        #corresponding letters of the index
        
        digit = s[i]
        letters = digit_to_letters[digit]
        
        #2. Now with each letter as the begining at the index
        # creating 3 subordinates takes care of filling the remaining
        #parts with letters of remaining digits
        #that means for ex: abc input letters: 3 subordinates
        # starts with "a"->s1; "b" ->s2 and "c"->s3;
        # so that each of them takes care of filling the slate
        #with next index letters. i don't care i will handover
        for letter in letters:
            helper(slate+letter,i+1)
    helper("",0)
    return result
input="478"
r=letter_combination(input)
print(f"For the given input {input} output is :{r}")
        
        