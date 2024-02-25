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
    
    for char in expression:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in "+-*/":
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            num, sign = 0, char
    
    if sign == '+':
        stack.append(num)
    elif sign == '-':
        stack.append(-num)
    
    return sum(stack)
