import random


def gen_random(num_count, begin, end):
    for i in range(0, num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    print(list(gen_random(5, 1, 3)))
