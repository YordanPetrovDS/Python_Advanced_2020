def get_subexpressions(expression):
    s = []
    result = []
    for index in range(len(expression)):
        ch = expression[index]
        if ch == "(":
            s.append(index)
        elif ch == ")":
            start_index = s.pop()
            result.append(expression[start_index:index+1])
    return result


for subexpressions in get_subexpressions(input()):
    print(subexpressions)
# print(get_subexpressions("1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"))
