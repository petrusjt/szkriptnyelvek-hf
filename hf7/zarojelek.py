#!/usr/bin/env python3

BRACKET_TYPES = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def is_between(value, lower_limit, upper_limit):
    return lower_limit < value and value < upper_limit


def create_bracket_list(expression):
    brackets = []
    for i in range(len(expression)):
        if expression[i] in BRACKET_TYPES:
            opening_bracket = expression[i]
            closing_bracket = BRACKET_TYPES[opening_bracket]
            depth = 0
            for j in range(i + 1, len(expression)):
                if expression[j] == closing_bracket:
                    if depth == 0:
                        brackets.append((i, j))
                        break
                    else:
                        depth -= 1
                elif expression[j] == opening_bracket:
                    depth += 1
            else:
                if (i, j) not in brackets:
                    return []
    return brackets
                

def is_valid_expression(expression):
    bracket_list = create_bracket_list(expression)
    if bracket_list == []:
        return False
    
    for item in bracket_list:
        for other_bracket in bracket_list:
            if item != other_bracket:
                if (is_between(item[0], other_bracket[0], other_bracket[1])
                    != is_between(item[1], other_bracket[0], other_bracket[1])):
                    return False

    return True


def main():
    expressions = [
        "((5+3)*2+1)",
        "{[(3+1)+2]+}",
        "(3+{1-1)}",
        "[1+1]+(2*2)-{3/3}",
        "(({[(((1)-2)+3)-3]/3}-3)"
    ]

    for expression in expressions:
        print(f"{expression} -> {is_valid_expression(expression)}")


if __name__ == "__main__":
    main()
