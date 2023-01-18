def is_armstrong_number(number):
    digits_in_number = []
    for digits in str(number):
        digits_in_number.append(int(digits))

    value_of_number = 0
    for digits in digits_in_number:
        value_of_number += digits**len(digits_in_number)

    return number == value_of_number


is_armstrong_number(10)