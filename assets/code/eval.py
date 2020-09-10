# run this with "python3 eval.py"
# visualize it: https://bit.ly/3mfCb6T

def operator():
    print("Operator evaluated")
    def func(operand1, operand2):
        print("Final Result:", operand1 + operand2)
    return func

def operand1():
    print("Operand1 evaluated")
    return 23

def operand2():
    print("Operand2 evaluated")
    return 38

operator()(operand1(), operand2())
