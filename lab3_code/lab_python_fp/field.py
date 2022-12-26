def field(items, *args):
    assert len(args) > 0, "len <= 0!!!"
    for item in items:
        if len(args) == 1:
            yield item[args[0]] * (item[args[0]] is not None)
        else:
            yield {x: item[x] for x in args if item[x] is not None}


if __name__ == '__main__':
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
    for i in field(goods, 'title'):
        print(i)
    for i in field(goods, 'price', 'title'):
        print(i)
