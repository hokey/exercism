"""
Utilities for calling out numbers
"""
PERIODS = {
    1: "",
    1_000: "thousand",
    1_000_000: "million",
    1_000_000_000: "billion"
}
TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}
TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
ONES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

def say(number: int) -> str:
    """
    Given a positive number less than a trillion, produce how to say it.

    :param int number: The number to say
    :return str: The proununcation of the number
    """
    limit = 1_000_000_000_000
    if number == 0:
        return ONES[number]
    if number < 0 or number >= limit:
        raise ValueError("input out of range")

    parts = []
    for period in sorted(PERIODS.keys(), reverse=True):
        label = PERIODS[period]
        if number // period > 0:
            parts.append(hundreds_say(number // period))
            if period > 1:
                parts.append(label)
        number %= period
    return " ".join(parts)

def hundreds_say(number: int) -> str:
    """
    Given a three digit number, produce how to say it.

    :param int number: A number between 0 and 999
    :return str: The pronunciation of the number
    """
    response = ""
    if number == 0:
        return  response
    if number // 100 > 0:
        response += ONES[number // 100] + " hundred"
    if number % 100 == 0:
        return response
    number = number % 100
    if response and number > 0:
        response += " "
    if number // 10 > 1:
        response += TENS[number // 10]
        if number % 10 > 0:
            response += "-" + ONES[number % 10]
    elif number // 10 == 1:
        response += TEENS[number]
    elif number % 10 > 0:
        response += ONES[number]
    return response
        
        
        
        
    

    