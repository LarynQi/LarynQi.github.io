def operator():
    print("evaluated operator")
    return lambda x, y: x + y
    
def operand1():
    print("evaluated operand 1")
    return 5
    
def operand2():
    print("evaluated operand 2")
    return 10

operator()(operand1(), operand2())