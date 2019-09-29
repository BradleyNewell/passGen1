import string
from secrets import choice


class Password:

    def __init__(self, a_file, length, name):
        self.a_file = a_file
        self.length = length
        self.name = name

    data = {}
    data['Passwords'] = []

    def p_gen(self):
        chars = string.ascii_letters + string.digits
        ext = '!$%^&*()_-+=@#~[],.<>?/|`'
        combo = chars + ext
        pw = ''.join([choice(combo) for i in range(self.length)])
        return pw

    def to_dict(self):
        pw_dict = {}
        pw_dict.update({self.name: self.p_gen()})
        return pw_dict

    def p_store(self):
        with open(self.a_file, 'a') as a_file:
            a_file.write(self.p_gen())


''' Example initialisation of the class, this will create a file called passwordfile and generate a 28 character
password stored in a dictionary with github being the key and the password as the value

password1 = Password('passwordfile.txt', 28, Github) '''