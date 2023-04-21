def remove_brackets(string):
    result = ""
    i = 0
    deep_brackets = 0
    for i in range(len(string)):
        if string[i] == '(':
            deep_brackets += 1

        elif string[i] == ')':
            deep_brackets -= 1

        elif deep_brackets <= 0:
            result += string[i]

    return result


string = input("Введите строку: ")
print(remove_brackets(string))
