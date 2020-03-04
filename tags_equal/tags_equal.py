from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag = None
        self.attrs = None

    def handle_starttag(self, tag, attrs):
        self.tag = tag
        self.attrs = self._convert(attrs, {})

    def _convert(self, tup, dic):
        for key, value in tup:
            if key not in dic:
                dic.setdefault(key, []).append(value)
        return dic


def tags_equal(tag_a, tag_b):
    parser_a = MyHTMLParser()
    parser_a.feed(tag_a)
    parser_b = MyHTMLParser()
    parser_b.feed(tag_b)
    return parser_a.tag == parser_b.tag and parser_a.attrs == parser_b.attrs
