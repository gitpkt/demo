from guioperations.common import Common as Cm


def count_char(s):
    obj = Cm()
    result = obj.get_char_occurrence(s)
    print(result)


if __name__ == '__main__':
    print("The number of character in the strings are: "
    count_char("I am living in a beautiful world")
    count_char("madam")

