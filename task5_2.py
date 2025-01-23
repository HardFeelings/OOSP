def find_smallest_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

number = int(input("Введите число, не меньше 2: "))
if number >= 2:
    print("Наименьший делитель, отличный от 1:", find_smallest_divisor(number))
else:
    print("Число должно быть не меньше 2.")