# Здесь должна быть реализация декоратора
def print_result(func_to_decorate):
    def decorated_func(*args, **kwargs):
        print(func_to_decorate.__name__)
        res = func_to_decorate(*args, **kwargs)
        if type(res) == list:
            for i in res:
                print(i)
        elif type(res) == dict:
            for key in res:
                print(key, ' = ', res[key])
        else:
            print(res)
        return res

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
