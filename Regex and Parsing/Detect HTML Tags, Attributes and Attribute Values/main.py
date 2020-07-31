from html.parser import HTMLParser


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

        for i in attrs:
            print('->', i[0], '>', i[1])


if __name__ == '__main__':
    n = int(input())
    html = '\n'.join([input() for _ in range(n)])
    parser = Parser()
    parser.feed(html)
