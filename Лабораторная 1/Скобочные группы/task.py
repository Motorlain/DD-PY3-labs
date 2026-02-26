def check_brackets(brackets_row: str) -> bool:
    stack = []

    for bracket in brackets_row:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets(""))  # True
    print(check_brackets("((()))"))  # True
    print(check_brackets("(()"))  # False