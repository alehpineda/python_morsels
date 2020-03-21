from functools import total_ordering

number_to_numeral_mapping = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


@total_ordering
class RomanNumeral(object):
    def __init__(self, value):
        self.value = self._value_type(value)

    def __int__(self):
        return self._roman_to_int()

    def _value_type(self, value):
        return value.upper() if isinstance(value, str) else value

    @classmethod
    def from_int(cls, value):
        return cls(value)._int_to_roman()

    @staticmethod
    def _roman_to_int(value):
        i = result = 0
        for number, numeral in number_to_numeral_mapping.items():
            while value[i:i + len(numeral)] == numeral:
                result += number
                i += len(numeral)
        return result

    @staticmethod
    def _int_to_roman(value):
        result = ''
        for number, numeral in number_to_numeral_mapping.items():
            while value >= number:
                result += numeral
                value -= number

        return result

    def __repr__(self):
        return f"RomanNumeral('{self.value}')"

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            value = self._roman_to_int() + other._roman_to_int()
            return RomanNumeral(self.from_int(value))
        elif isinstance(other, int):
            value = self._roman_to_int() + other
            return RomanNumeral(self.from_int(value))
        else:
            NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self._roman_to_int() == other._roman_to_int()
        elif isinstance(other, int):
            return self._roman_to_int() == other
        elif isinstance(other, str):
            return self.value == other
        else:
            NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self._roman_to_int() < other._roman_to_int()
        elif isinstance(other, int):
            return self._roman_to_int() < other
        elif isinstance(other, str):
            raise TypeError
        else:
            NotImplemented
