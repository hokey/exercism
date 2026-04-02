"""
Luhn Number Utility 
"""
class Luhn:
    """
    Class for Luhn numbers
    """

    
    def __init__(self, card_num: str) -> None:
        """
        Initializer for Luhn

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
        parity = len(digits) % 2
        for index, digit in enumerate(digits):
            if index % 2 == parity:
                digit *= 2
                if digit > 9:
                    digit -= 9
            card_number_check += digit
        return card_number_check % 10 == 0