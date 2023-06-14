#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    else:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(roman_string)):
            len_rm = len(roman_string)
            rmi = rom[roman_string[i]]
            if i + 1 < len_rm and rmi < rom[roman_string[i + 1]]:
                res -= rom[roman_string[i]]
            else:
                res += rom[roman_string[i]]
        return res
