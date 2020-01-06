import unicodedata


class FuzzyString(object):
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self._normalize(self.text) == self._normalize(other)

    def __lt__(self, other):
        return self._normalize(self.text) < self._normalize(other)

    def __gt__(self, other):
        return self._normalize(self.text) > self._normalize(other)

    def __le__(self, other):
        return self._normalize(self.text) <= self._normalize(other)

    def __ge__(self, other):
        return self._normalize(self.text) >= self._normalize(other)

    def __add__(self, other):
        return FuzzyString(self.text + other)

    def __contains__(self, other):
        return self._normalize(other) in self._normalize(self.text)

    def _normalize(self, text):
        return unicodedata.normalize("NFKD", text.casefold())

    def __repr__(self):
        return repr(self.text)

    def __str__(self):
        return self.text
