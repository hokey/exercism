def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """
    Converts a list of digits representing the base number system given to a given new base number system

    :param int input_base: base number system given
    :param list[int] digits: list of digits in base number system given
    :param int output_base: base number system requested

    :return list[int]: list of digits in requested base number system
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    output_number = []
    
    decimal_number = 0
    for digit_index in range(0, len(digits)):
        decimal_number += digits[digit_index] * (input_base ** (len(digits) - 1 - digit_index))
    if(decimal_number < output_base):
        return [decimal_number]
        
    largest_pow = 0
    for index in range(0, decimal_number):
        if output_base ** index > decimal_number:
            largest_pow = index -1
            break;

    digit = 0
    for pow_index in range(largest_pow, -1, -1):
        digit = decimal_number / (output_base**pow_index)
        output_number.append(int(digit))
        decimal_number = decimal_number % (output_base**pow_index)
    return output_number