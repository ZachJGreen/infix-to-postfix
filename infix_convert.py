def check_parentheses(infix: str):
    balanced = True
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    bracket_stack = []
    for i in infix:
        for j in open_brackets:
            if i == j:
                bracket_stack.append(i)

        for j in range(0, 3):
            if i == close_brackets[j]:
                if bracket_stack[-1] == open_brackets[j]:
                    bracket_stack.pop(-1)
                else:
                    balanced = False
        if not balanced:
            break

    return balanced


def is_operand(iterator: str):
    try:
        int(iterator)
        return True
    except Exception as e:
        return False


def which_operator(iterator: str):
    if iterator == "+" or iterator == "-":
        return 1
    elif iterator == "*" or iterator == "/" or iterator == "%":
        return 2


def operator_check(iterator: str):
    operators = ["+", "-", "/", "*", "%"]
    for i in operators:
        if i == iterator:
            return True

    return False

def open_bracket_check(iterator: str):
    open_brackets = ['(', '[', '{']

    for i in open_brackets:
        if iterator == i:
            return True
    return False

def close_bracket_check(iterator: str):
    close_brackets = [')', ']', '}']

    for i in close_brackets:
        if iterator == i:
            return True
    return False

def infix_to_postfix(infix: str):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    operators = ["+", "-", "/", "*", "%"]

    if not check_parentheses(infix):
        return "This equation is not balanced properly"

    op_stack = []
    postfix_list = []
    top = len(op_stack) - 1
    for token in infix.split():
        if is_operand(token):
            postfix_list.append(token)

        elif operator_check(token):
            while top > -1 and not open_bracket_check(op_stack[top]) and which_operator(token) <= which_operator(op_stack[top]):
                postfix_list.append(op_stack[top])
                op_stack.pop(top)
                top = len(op_stack) - 1
            
            op_stack.append(token)
            
        else:
            if open_bracket_check(token):
                op_stack.append(token)
            elif close_bracket_check(token):
                while not open_bracket_check(op_stack[top]) and top > 0:
                    postfix_list.append(op_stack[top])
                    op_stack.pop(-1)
                op_stack.pop(-1)
        top = len(op_stack) - 1
    while top > -1:
        postfix_list.append(op_stack[top])
        op_stack.pop(top)
        top = len(op_stack) - 1

    postfix_out = ' '.join(postfix_list)
    return postfix_out
