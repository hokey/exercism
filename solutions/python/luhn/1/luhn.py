"""
Luhn Number Utility 
"""
class Luhn:
    """
    Class for Luhn numbers
    """
    card_number = None
    def __init__(self, card_num: str) -> None:
        """
        Initilizer for Luhn

        :param str card_num: Luhn number
        """
        self.card_number = card_num.replace(" ", "")
    def valid(self) -> bool:
        """
        Determines the validity of the Luhn number
        """
        card_number_check = 0
        if len(self.card_number) <= 1:
            return False
        if not self.card_number.isdigit():
            return False
        digits = [int(digit) for digit in self.card_number]
        if len(digits) % 2:
            for digit in digits[1::2]:
                if (digit * 2) > 9:
                    card_number_check += ((digit * 2) - 9)
                else:
                    card_number_check += (digit * 2)
            card_number_check += sum(digits[::2])
        else:
            for digit in digits[::2]:
                if (digit * 2) > 9:
                    card_number_check += ((digit * 2) - 9)
                else:
                    card_number_check += (digit * 2)
            card_number_check += sum(digits[1::2])
        return False if card_number_check % 10 else True