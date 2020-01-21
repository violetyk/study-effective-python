#!/usr/bin/env python3

#  https://rinatz.github.io/python-book/ch03-04-properties/

import math

class Point():

    def __init__(self, x, y):
        #  _をつけて隠蔽していることを示す
        self._x = x
        self._y = y


    #  @で始まるキーワードはデコレータという
    @property
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


    #  x, y を隠蔽して、プロパティにすると
    #  代入ができなくなるので安全、がメリット
    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

def main():
    point = Point(10, 20)

    #  AttributeError: can't set attribute
    #  point.x = 1000

    #  @y.setterを書けば代入できる
    point.y = 2000 

    #  @propertyをつけるとpoint.distance()のように参照できる
    print(point.distance)
    #  もとのpoint.distance()のようには呼べなくなる
    #  TypeError: 'float' object is not callable
    #  print(point.distance())

if __name__ == '__main__':
    main()
