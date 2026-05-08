"""
NANP Phone Number
"""
from string import punctuation

class PhoneNumber:
    """
    Phone number representing the NANP format
    """
    valid_punctuation = "+()-. _"
    valid_punctuation_table = str.maketrans("", "", valid_punctuation)
    invalid_punctuation = punctuation.translate(valid_punctuation_table)

    
    def __init__(self, number: str) -> None:
        self.area_code: str
        self.exchange: str
        self.local: str
        self.number: str
        self.process(number)


    def process(self, number: str) -> None:
        """
        Process and validates the phone number

        :param str: the number to clean up and validate
        """
        candidate = []
        for character in number:
            if character.isalpha():
                raise ValueError("letters not permitted")
            if character in self.invalid_punctuation:
                raise ValueError("punctuations not permitted")
            if character.isdigit():
                candidate.append(character)
        if len(candidate) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(candidate) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(candidate) == 11 and candidate[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(candidate) == 11:
            candidate = candidate[1:]
        if candidate[0] == "0":
            raise ValueError("area code cannot start with zero")
        if candidate[0] == "1":
            raise ValueError("area code cannot start with one")
        if candidate[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if candidate[3] == "1":
            raise ValueError("exchange code cannot start with one")
        self.area_code = "".join(candidate[:3])
        self.exchange = "".join(candidate[3:6])
        self.local = "".join(candidate[6:10])
        self.number = "".join(candidate)
        
        
    def pretty(self) -> str:
        """
        Pretty prints number in (XXX)-XXX-XXXX format

        :return str: prettified number
        """
        return f"({self.area_code})-{self.exchange}-{self.local}"