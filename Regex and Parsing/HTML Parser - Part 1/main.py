from html.parser import HTMLParser


class Parser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        print('Start :', tag)

        for i in attrs:
            print('->', i[0], '>', i[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)

        for i in attrs:
            print('->', i[0], '>', i[1])

    def handle_comment(self, data):
        pass


if __name__ == '__main__':
    n = int(input())
    html = ""

    for _ in range(n):
        line = input()
        html += line

    parser = Parser()
    parser.feed(html)
