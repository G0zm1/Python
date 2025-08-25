from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    first_number = float(input("What's your first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_input = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = operations[operation_input](first_number, second_number)
        print(f"{first_number} {operation_input} {second_number} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if should_continue == "n":
           should_continue = False
           print("\n" * 20)
           calculator()

        elif should_continue == "y":
            first_number = result

calculator()
