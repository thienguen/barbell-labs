def calculate(expression: str) -> int:
    """
    Evaluates a basic arithmetic expression string containing non-negative integers and the operators +, -, *, and /.

    Args:
        expression (str): The arithmetic expression to be evaluated.

    Returns:
        int: The result of the evaluation.

    Raises:
        ValueError: If the expression is invalid.
    """
    num, stack, sign = 0, [], "+"
    
    # Function to perform operation based on the current operator
    def perform_operation():
        if sign == '+':
            stack.append(num)
        elif sign == '-':
            stack.append(-num)
        elif sign == '*':
            stack[-1] = stack[-1] * num
        elif sign == '/':
            stack[-1] = int(stack[-1] / num)
    
    for char in expression:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in "+-*/":
            perform_operation()
            num, sign = 0, char
        elif char != ' ':
            raise ValueError("Invalid character '{}' in expression.".format(char))
    
    # Perform the last operation
    perform_operation()
    
    return sum(stack)
