import json
import cm_timer
from print_result import print_result
from gen_random import gen_random
from unique import Unique

path = 'data_light.json'

with open(path, encoding='UTF8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(sorted(Unique([x["job-name"] for x in arg], ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(x + f', зарплата {y} руб' for y, x in zip(gen_random(len(arg), 100000, 200000), arg))


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
