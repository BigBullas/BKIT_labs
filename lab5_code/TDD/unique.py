from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.index = 0
        self.used_elements = set()
        self.data = []
        if len(kwargs) != 0 and kwargs["ignore_case"]:
            for i in items:
                self.data.append(i.lower())
        else:
            for i in items:
                self.data.append(i)

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(10, 1, 3)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    t = Unique(data3, ignore_case=True)
    print(next(t), end=' ')
    print(next(t))
    # print(next(t))
    t = Unique(data3)
    print(next(t), end=' ')
    print(next(t), end=' ')
    print(next(t), end=' ')
    print(next(t))
    # print(next(t))
    t = Unique(data1)
    print(next(t), end=' ')
    print(next(t))

    t = Unique(data2)

    print(next(t), end=' ')
    print(next(t))
    # print(next(t))
