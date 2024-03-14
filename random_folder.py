import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


if __name__ == '__main__':
    random_string = generate_random_string()
    print(random_string)
