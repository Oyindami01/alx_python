number = -98
last_digit = abs(number) % 10

if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
else:
    if last_digit == 0:
        print("Last digit of", number, "is", last_digit, "and is 0")
    else:
        print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
