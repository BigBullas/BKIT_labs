# import random
#
#
# def gen_random(num_count, begin, end):
#     for i in range(0, num_count):
#         yield random.randint(begin, end)
#
#
# def sort1(data):
#     return sorted(data, key=abs, reverse=True)
#
#
# def sort2(data):
#     return sorted(data, key=lambda x: -abs(x))
#
#
# class Unique(object):
#     def __init__(self, items, **kwargs):
#         self.index = 0
#         self.used_elements = set()
#         self.data = []
#         if len(kwargs) != 0 and kwargs["ignore_case"]:
#             for i in items:
#                 self.data.append(i.lower())
#         else:
#             for i in items:
#                 self.data.append(i)
#
#     def __next__(self):
#         while True:
#             if self.index >= len(self.data):
#                 raise StopIteration
#             else:
#                 current = self.data[self.index]
#                 self.index = self.index + 1
#                 if current not in self.used_elements:
#                     self.used_elements.add(current)
#                     return current
#
#     def __iter__(self):
#         return self

# def field(items, *args):
#     assert len(args) > 0, "len <= 0!!!"
#     for item in items:
#         if len(args) == 1:
#             yield item[args[0]] * (item[args[0]] is not None)
#         else:
#             yield {x: item[x] for x in args if item[x] is not None}

import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        while True:
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                break
            except:
                print('Ошибка')
    return coef


def get_roots(a, b, c):
    result = []
    if a == 0 and b == 0:
        if c == 0:
            return False

    elif a == 0 and b != 0:
        if c == 0:
            result.append(0)
        elif -c / b > 0:
            root1 = -math.sqrt(-c / b)
            root2 = math.sqrt(-c / b)
            result = [root1, root2]
        elif -c / b == 0:
            result.append(0)
    elif a != 0 and b == 0:
        if c == 0:
            result.append(0)
        elif -c / a > 0:
            root1 = -math.sqrt(math.sqrt(-c / a))
            root2 = math.sqrt(math.sqrt(-c / a))
    elif a != 0 and b != 0:
        if c == 0:
            if - b / a > 0:
                root1 = 0
                root2 = -math.sqrt(- b / a)
                root3 = math.sqrt(- b / a)
                result = [root1, root2, root3]
            else:
                result.append(0)
        else:
            D = b ** 2 - 4 * a * c
            if D > 0:
                D = math.sqrt(D)
                c1 = (-b - D) / (2 * a)
                c2 = (-b + D) / (2 * a)
                if c1 > 0 and c2 > 0:
                    root1 = -math.sqrt(c1)
                    root2 = math.sqrt(c1)
                    root3 = -math.sqrt(c2)
                    root4 = math.sqrt(c2)
                    result = [root1, root2, root3, root4]
                elif c1 > 0 and c2 < 0:
                    root1 = -math.sqrt(c1)
                    root2 = math.sqrt(c1)
                    result = [root1, root2]
                elif c1 < 0 and c2 > 0:
                    root1 = -math.sqrt(c2)
                    root2 = math.sqrt(c2)
                    result = [root1, root2]

            elif D == 0:
                if - b / (2 * a) > 0:
                    root1 = math.sqrt(- b / (2 * a))
                    root2 = -math.sqrt(-b / (2 * a))
                    result = [root1, root2]
                elif - b / (2 * a) == 0:
                    root1 = 0
                    result.append(0)
    return sorted(result)


def main():
    a = get_coef(1, 'Введите коэффициент A:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    if roots != False:
        len_roots = len(roots)

    if roots == False:
        print('Бесконечное количество корней')
    elif len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()