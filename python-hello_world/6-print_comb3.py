#!/usr/bin/python3
combinations = []
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        combinations.append("{:02d}".format(tens_digit * 10 + ones_digit))

result = ", ".join(combinations)
print(result)

