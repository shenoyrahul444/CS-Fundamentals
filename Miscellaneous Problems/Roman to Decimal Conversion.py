"""
Converting Roman Numerals to Decimal lying between 1 to 3999
Given a Romal numeral, find its corresponding decimal value.

Example:

Input : IX
Output : 9

Input : XL
Output : 40

Input : MCMIV
Output :  1904
M is a thousand, CM is nine hundred
and IV is four
"""

def romanToDecimal(roman):

    roman = roman.strip()   # For removing empty spaces in string

    if roman == None or len(roman) == 0:    # Edge Case check
        return False

    res = 0     # Result variable

    values = {
        "I": 1,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
    }

    n = len(roman)

    i = 0
    while i < n:

        v1 = values[roman[i]]

        if i+1 < n:

            v2 = values[roman[i+1]]

            if v1 < v2 :
                res += v2 - v1
                i += 2
            elif v1 >= v2:
                res += v1
                i += 1
        else:
            res += v1
            i += 1

    return res

print(romanToDecimal("IX") == 9)
print(romanToDecimal("XXXV") == 35)






