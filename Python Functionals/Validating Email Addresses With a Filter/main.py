# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
def fun(s):
    if len(s.split('@')) == 2 and len(s.split('.')) == 2:
        username, url = s.split("@")
        website, extension = url.split(".")

        return username.replace("-", "").replace("_", "").isalnum() and website.isalnum() and len(extension) <= 3

    return False


def filter_mail(emails):
    return filter(fun, emails)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
