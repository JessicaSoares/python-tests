def find_brackets():
    
    text = input("input the text: ")
    array = list(text)
    print(array)

    brack_stack = []

    for array in array:
        if array in '{([':
            brack_stack.append(array)
        elif array in ')]}':
            if not brack_stack:
                return False
            last_opening = brack_stack.pop()
            if (array == ')' and last_opening != '(') or \
               (array == '}' and last_opening != '{') or \
               (array == ']' and last_opening != '['):
                return False

    return len(brack_stack) == 0



print(find_brackets())  


