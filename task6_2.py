def replace_colons_with_percent(s):
    updated_string = s.replace(':', '%')
    count = s.count(':')
    return updated_string, count

input_string = input("Введите строку: ")
result, replacements = replace_colons_with_percent(input_string)

print("Обновленная строка:", result)
print("Количество замен:", replacements)
