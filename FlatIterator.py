class FlatIterator():

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list

    def __iter__(self):

        self.list_i = 0
        self.item_i = -1
        self.iterated_list = self.list_of_list[self.list_i]

        return self
    
    def __next__(self):

        self.item_i += 1

        if self.item_i >= len(self.iterated_list):
            self.list_i += 1
            if self.list_i >= len(self.list_of_list):
                raise StopIteration
            self.item_i = 0
            self.iterated_list = self.list_of_list[self.list_i]

        return self.iterated_list[self.item_i]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()