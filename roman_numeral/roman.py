from functools import total_ordering


@total_ordering
class RomanNumeral(object):

    number_to_numeral_mapping = {
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
        1: "I",
    }

    def __init__(self, value):
        self.value = self._roman_to_int(value)

    def __int__(self):
        return self.value

    @classmethod
    def from_int(cls, value):
        return cls(cls._int_to_roman(value))

    @staticmethod
    def _roman_to_int(value):
        i = result = 0
        for number, numeral in RomanNumeral.number_to_numeral_mapping.items():
            while value[i : i + len(numeral)] == numeral:
                result += number
                i += len(numeral)
        return result

    @staticmethod
    def _int_to_roman(value):
        result = ""
        for number, numeral in RomanNumeral.number_to_numeral_mapping.items():
            while value >= number:
                result += numeral
                value -= number

        return result

    def __repr__(self):
        return f"RomanNumeral('{self._int_to_roman(self.value)}')"

    def __str__(self):
        return self._int_to_roman(self.value)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return self.from_int(self.value + other.value)
        elif isinstance(other, int):
            return self.from_int(self.value + other)
        else:
            NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        elif isinstance(other, str):
            return self._int_to_roman(self.value) == other
        else:
            NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        elif isinstance(other, str):
            raise TypeError
        else:
            NotImplemented
