
class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer_counter = 0
        self.inner_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_counter < len(self.list_of_lists):
            current_list = self.list_of_lists[self.outer_counter]
            if self.inner_counter < len(current_list):
                item = current_list[self.inner_counter]
                self.inner_counter += 1
                return item
            self.outer_counter += 1
            self.inner_counter = 0
        raise StopIteration


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





