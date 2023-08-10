#!/usr/bin/python3
output = ""
for number in range(100):
    output += "{:02}".format(number)
    if number != 99:
        output += ", "
        
print(output + "")