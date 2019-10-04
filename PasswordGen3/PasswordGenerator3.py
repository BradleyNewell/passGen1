import string
from secrets import choice

data = {}
a_file = open('saved_passwords.txt', 'a+')


class Password:

    def __init__(self, length, name):
        self.length = length
        self.name = name

    def p_gen(self):
        chars = string.ascii_letters + string.digits
        ext = '!$%^&*()_-+=@#~[],.<>?/|`'
        combo = chars + ext
        pw = ''.join([choice(combo) for i in range(self.length)])
        return pw

    def to_dict(self):
        data.update({self.name: self.p_gen()})
        a_file.write(str(data))


password1 = Password(28, 'Github')
password1.p_gen()
password1.to_dict()
