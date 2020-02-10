import re


# mut.py --target normalize_sentences --unit-test test_normalize_sentences
# --runner pytest --show-mutant --coverage --colored-output
def normalize_sentences(text):
    return re.sub(r'([\S][^\.]\S[?.!]) +', r'\1  ', text)
