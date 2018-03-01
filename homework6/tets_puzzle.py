
"""
Условие провекрки взято из википедии. Этот тест подходит только под игру,
где поле cделано при помощи словаря


"""

class Testing(object):
    def __init__(self, field):
        self.field = field

    def test_field(self):
        k = 0
        e = 0
        for key in sorted(self.field.keys()):
            n = 0
            for key1 in sorted(self.field.keys())[key:]:
                try:
                    if self.field[key] > self.field[key1]:
                        n += 1
                except TypeError:
                    continue
                k += n
        for key, values in self.field.items():
            if isinstance(values, str):
                if key/4 <= 1:
                    e = 1
                elif 1 < key/4 <= 2:
                    e = 2
                elif 2 < key/4 <= 3:
                    e = 3
                elif 3 < key/4 <= 4:
                    e = 4
        print(k, e)
        if (e + k) % 2 == 0:
            return True
        else:
            return False


START_FIELD = {
        1: 1, 2: 2, 3: 3, 4: 4,
        5: 5, 6: 6, 7: 7, 8: 8,
        9: 9, 10: 10, 11: 11, 12: 12,
        13: 13, 14: 15, 15: 14, 16: "X"
    }

field = START_FIELD
test = Testing(field)
print(test.test_field())


