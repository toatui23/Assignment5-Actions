import math


def firstrun():
    return "success"


def CircleArea(radius):
    return round(math.pi*(radius*radius), 2)


def firstandlast(list):
    first = list[0]
    last = list[-1]
    return first, last


def numberofdays(date1, date2):
    answer = date2 - date1
    return answer.days
