import unittest
from unique import Unique
from gen_random import gen_random


def sort1(data):
    return sorted(data, key=abs, reverse=True)


def sort2(data):
    return sorted(data, key=lambda x: -abs(x))


def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            yield item[args[0]] * (item[args[0]] is not None)
        else:
            yield {x: item[x] for x in args if item[x] is not None}


class FieldTest(unittest.TestCase):
    def test_field(self):
        goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
                 {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
        self.assertEqual(list(field(goods, 'title')), ["Ковер", "Диван для отдыха"])
        self.assertEqual(next(field(goods, 'title', 'price')), {'title': 'Ковер', 'price': 2000}
                         and next(field(goods, 'title', 'price')), {'title': 'Диван для отдыха'})

    def test_sort(self):
        data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
        self.assertEqual(sort1(data), [123, 100, -100, -30, 30, 4, -4, 1, -1, 0])
        self.assertEqual(sort2(data), [123, 100, -100, -30, 30, 4, -4, 1, -1, 0])

    def test_unique(self):
        data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        data2 = gen_random(10, 1, 3)
        data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        self.assertEqual(list(Unique(data3)), ['a', 'A', 'b', 'B'])
        self.assertEqual(list(Unique(data3, ignore_case=True)), ['a', 'b'])
        self.assertEqual(list(Unique(data1)), [1, 2])
        self.assertTrue(len(list(Unique(data2))) > 0)

