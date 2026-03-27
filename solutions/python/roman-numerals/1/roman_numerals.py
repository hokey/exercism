"""
Roman Numeral 
"""
NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def roman(number):
    """
    Given an Arabic number, produce the Roman Numeral

    Assumptions: Concerned about traditional Roman numerals, in which the largest number is MMMCMXCIX (or 3,999)
    :param int number: Arabic number
    :return str: Roman Numeral
    """
    roman_parts = []
    for arabic, roman_part in NUMERALS.items():   
        roman_parts.append((number // arabic) * roman_part)
        number %= arabic
    return "".join(roman_parts)