#!/usr/bin/env python3
from datetime import datetime, timedelta
from dateutil.parser import parse

def main():

    s = '2020-01-27 01:12:34'
    dt = parse(s)
    print(dt)
    print(dt.year)
    print(dt.month)
    print(dt.day)
    print(dt.hour)
    print(dt.minute)
    print(dt.second)

    s = '2020/02/29'
    dt = parse(s)
    print(dt)
    print(dt.year)
    print(dt.month)
    print(dt.day)
    print(dt.hour)
    print(dt.minute)
    print(dt.second)


if __name__ == '__main__':
    main()
