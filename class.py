#!/usr/bin/env python3

#  https://rinatz.github.io/python-book/ch03-01-classes/
#  Pythonにはインターフェースがない
class Rectangle:

    #  コンストラクタ
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


#  Square extends Rectangle
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


class A():

    def __init__(self):
        pass

    def greet(self):
        print('This is class A')


class B():

    def __init__(self):
        pass

    def greet(self):
        print('This is class B')

class C():

    def __init__(self):
        pass

    def hello(self):
        print('This is class C')

    #  public
    #  method()

    #  protected
    #  _method()

    #  private
    #  __method()

def call(x):
    x.greet()


def main():
    rectangle = Rectangle(10, 20)
    print(type(rectangle))

    print(f'The value of width is {rectangle.width}')
    print(f'The value of height is {rectangle.height}')

    area = rectangle.area()
    print(f'The area is {area}')

    square = Square(10)
    area = square.area()
    print(f'The area is {area}')

    call(A())
    call(B())
    #AttributeError: 'C' object has no attribute 'greet'
    #  call(C())

    #  動的にメソッドを呼ぶ
    c = C()
    method_name = 'hello'
    method = getattr(c, method_name)
    method()

if __name__ == '__main__':
    main()
