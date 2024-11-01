import random
import string


class GenRandomString:

    @staticmethod
    def gen_by_len(len_string):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=len_string))
