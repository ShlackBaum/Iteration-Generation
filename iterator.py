nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, iterable_list):
        self.iterable_list = iterable_list
        self.list_cursor = -1
        self.element_cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        len_index1=len(self.iterable_list[self.list_cursor])-1
        len_index2=len(self.iterable_list)-1
        len_index3=len(self.iterable_list[self.list_cursor])-1

        if self.list_cursor == len_index2 and self.element_cursor == len_index3:
            raise StopIteration
        if self.list_cursor == -1 or self.element_cursor == len_index1:
            self.list_cursor += 1
            self.element_cursor = -1
        if self.element_cursor == -1 or self.element_cursor < len_index1:
            self.element_cursor += 1
        if self.list_cursor == len_index2 and self.element_cursor == len_index3:
            return self.iterable_list[self.list_cursor][self.element_cursor]
        return self.iterable_list[self.list_cursor][self.element_cursor]


for item in FlatIterator(nested_list):
    print(item)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)
