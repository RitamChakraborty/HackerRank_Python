# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
import collections

if __name__ == '__main__':
    n = int(input().strip())
    cols = input().strip().split()
    Student = collections.namedtuple('Student', " ".join(cols))
    students = []

    for _ in range(n):
        inputs = input().strip().split()
        student = Student(inputs[0], inputs[1], inputs[2], inputs[3])
        students.append(student)

    s = 0
    for student in students:
        s += int(student.MARKS)

    print(s / n)

    # One liner solution
    # print([[a / b] for a, b in [(sum(a), len(a)) for a in [[int(Student(*input().split()).MARKS) for _ in range(n)] for n, Student in [(int(input()), __import__('collections').namedtuple('Student', input().split()))]]]][0][0])
