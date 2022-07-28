from itertools import chain

print('-------Task 1--------')


class FlatIterator(list):
    def __iter__(self):
        self.element = iter(self.copy())
        return self

    def __next__(self):
        next_element = next(self.element)
        if isinstance(next_element, list):
            self.element = chain(next_element, self.element)
            return next(self.element)
        return next_element


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('-------Task 2--------')


def flat_generator(lst):
    for i in chain.from_iterable(nested_list):
        yield i


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in flat_generator(nested_list):
    print(item)
