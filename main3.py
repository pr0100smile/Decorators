"""
3. Применить написанный логгер к приложению из любого предыдущего д/з.
"""

from main2 import logger

@logger('main3.log')
def flat_generator(list_of_list):
    for listing in list_of_list:
        if type(listing) is list:
            yield from flat_generator(listing)
        else:
            yield listing

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print(list(flat_generator(list_of_lists_2)))


if __name__ == '__main__':
    test_3()