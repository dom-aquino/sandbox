def sample_decorator(func):
    def inner_func():
        print("Inner func")
        func()
    return inner_func

# @sample_decorator
def my_func():
    print("My func")

my_func()