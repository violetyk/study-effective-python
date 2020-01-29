import sys
 
def func_test():
    print('function')
 
 
class ClassTest():
    def f():
        pass

 
 
str_test = 'str'
 
 
print(callable(sys))
print(callable(func_test))
print(callable(ClassTest))
print(callable(str_test))
print(callable(ClassTest().f))
