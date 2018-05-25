"""
The module contains the utilies for gui operations
"""


class Common(object):
    def __init__(self):
        pass

    def get_char_occurrence(self, req_str):
        char_num = {}
        [char_num.update({x: req_str.count(x)}) for x in set(list(req_str))]
        return char_num
