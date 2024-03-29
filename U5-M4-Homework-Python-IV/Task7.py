def validParenthesesSequence(s):
    stackOfParenth = []
    for char in s:
        if char in ["(", "{", "["]:
            stackOfParenth.append(char)
        else:
            if not stackOfParenth:
                return False
            current_char = stackOfParenth.pop()
            if current_char == '(':
                if char != ")":
                    return False
    if stackOfParenth:
        return False
    return True

print(validParenthesesSequence("()()(())"))
print(validParenthesesSequence("()()())"))
