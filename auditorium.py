# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35,
# then the output should be 3 + 5 = 8

two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit + second_digit
print(two_digit_number)