from guioperations.common import Common as Cm


def count_char(s):
    obj = Cm()
    result = obj.get_char_occurrence(s)
    print(result)


if __name__ == '__main__':
    count_char("I am living in a beautiful world")


