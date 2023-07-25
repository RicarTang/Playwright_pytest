from pydantic import validate_arguments,StrictInt


@validate_arguments
def func(a:StrictInt):
    print(a)


func(1.0001212)