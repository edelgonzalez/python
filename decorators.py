

def my_decorator(some_func):
    """
    help text my_decorator
    """
    def wrapper():
        """
        this is the actual function
        """
        print "before some func"
        some_func()
        print "after some func"
    return wrapper


@my_decorator
def foo():
    """
    help text for foo
    """
    print "this is the foo/some func"

#foo = my_decorator(foo)
foo()
print(foo.__doc__)


# def my_function():
#     """Do nothing, but document it.
#
#     No, really, it doesn't do anything.
#     """
#     pass
#
# print(my_function.__doc__)
