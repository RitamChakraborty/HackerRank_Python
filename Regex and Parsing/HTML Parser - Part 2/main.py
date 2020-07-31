from html.parser import HTMLParser


class Parser(HTMLParser):
    def error(self, message):
        pass

    def handle_comment(self, data):
        lines = data.split("\n")

        if len(lines) == 1:
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")

        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


if __name__ == '__main__':
    n = int(input())
    html = '\n'.join([input() for _ in range(n)])
    parser = Parser()
    parser.feed(html)
