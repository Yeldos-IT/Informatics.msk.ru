x = int(input())


roman_number = ""

if x >= 100:
    roman_number += "C"
    x -= 100
if x >= 90:
    roman_number += "XC"
    x -= 90
if x >= 50:
    roman_number += "L"
    x -= 50
if x >= 40:
    roman_number += "XL"
    x -= 40
if x >= 10:
    roman_number += "X" * (x // 10)
    x %= 10
if x >= 9:
    roman_number += "IX"
    x -= 9
if x >= 5:
    roman_number += "V"
    x -= 5
if x >= 4:
    roman_number += "IV"
    x -= 4
if x >= 1:
    roman_number += "I" * x

print(roman_number)