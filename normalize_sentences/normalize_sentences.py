import re
from textwrap import dedent


def normalize_sentences(text):
    replace = {
        r'(\.)(?=[^\n])': '. ',
        r'(\!)(?=[^\n])': '! ',
        r'(\?)(?=[^\n])': '? '
    }

    for key, value in replace.items():
        text = (re.sub(key, value, text))

    return text


if __name__ == "__main__":
    sentences = dedent("""
            This is a paragraph. With two sentences in it.

            And this is one. With three. Three short sentences.
        """).strip()
    expected = dedent("""
            This is a paragraph.  With two sentences in it.

            And this is one.  With three.  Three short sentences.
        """).strip()
    print(expected)
    print(normalize_sentences(sentences))
