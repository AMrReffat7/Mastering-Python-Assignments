def decorator(my_function):
    def decorator_mess():
        print("Sugar Added From Decorators")
        my_function()
        print("#" * 50)
    return decorator_mess

@decorator
def make_tea():
    print("Tea Created")

@decorator
def make_coffee():
    print("Coffee Created")

make_tea()
make_coffee()
