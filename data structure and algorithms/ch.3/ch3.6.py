from pythonds3.basic import Stack

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    
    return s.is_empty()
print(par_checker("((()))"))  # expected True

def divide_by_2(decimal_num) :
    rem_stack = Stack()
    
    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num //2
    
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    
    return bin_string

def divide_by_8(decimal_num) :
    rem_stack = Stack()
    
    while decimal_num > 0:
        rem = decimal_num % 8
        rem_stack.push(rem)
        decimal_num = decimal_num //8
    
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    
    return bin_string
def base_converter(decimal, base):
    digits = "0123456789ABCDEF"
    rem_stacks = Stack()
    
    while decimal > 0:
        rem = decimal % base
        rem_stacks.push(rem)
        decimal = decimal // base
        
    new_string = ""
    while not rem_stacks.is_empty():
        new_string = new_string + digits[rem_stacks.pop()]
    
    return new_string
        
print(base_converter(26,26))
print(base_converter(256,16))