class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self                   # Return the updated set

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()