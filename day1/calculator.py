def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is your first number: "))
   
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation symbol: ")
        num2 = float(input("What is your second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue with {answer}, or type 'no' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
