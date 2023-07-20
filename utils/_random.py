"""随机数据"""
import random
import string


def generate_random_string(length:int):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    random_string = generate_random_string(31)
    print(random_string)
