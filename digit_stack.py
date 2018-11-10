
def digit_stack(operations):
    global ans 
    global stack 
    ans = 0
    stack = []
    
    def pop(n):
        global ans
        try:
            ans += stack.pop()
        except IndexError:
            pass
        
    def push(n):
        global stack
        stack.append(int(n))
        
    def peek(n):
        global ans
        try:
            ans += stack[-1]
        except IndexError:
            pass
        
    commands = {'POP': pop, 'PUSH': push, 'PEEK': peek}
    for op in operations:
        current = op.split()
        commands[current[0]](current[-1])
    return ans
        
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print('all good')
   
    
    
    
