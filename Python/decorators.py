def new_decorator(func):
    def wrap_func():
        print("before calling")
        func()
        print("this func has been called")
    return wrap_func
@new_decorator
def func_needs_decorator():
    print("this function is need of decorators")

func_needs_decorator()
